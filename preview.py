from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


class Thread(QtCore.QThread):
    changePixmap = QtCore.pyqtSignal(QtGui.QImage)
    scaled_size = QtCore.QSize(800, 480)

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if ret:
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QtGui.QImage.Format_RGB888)
                p = convertToQtFormat.scaled(self.scaled_size, QtCore.Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

    def scaled(self, scaled_size):
        self.scaled_size = scaled_size


class PlayStreaming(QtWidgets.QLabel):
    reSize = QtCore.pyqtSignal(QtCore.QSize)

    def __init__(self):
        super(PlayStreaming, self).__init__()
        self.initUI()

    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def initUI(self):
        # create a label
        self.label = QtWidgets.QLabel(self)
        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        self.reSize.connect(th.scaled)
        th.start()
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.label, alignment=QtCore.Qt.AlignCenter)