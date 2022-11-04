from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import preview

class UIWidget(QDialog):
    def __init__(self, parent=None):
        super(UIWidget, self).__init__(parent)
        loadUi("camera.ui", self)
        self.display = preview.PlayStreaming()
        self.preview.addWidget(self.display, stretch=1)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = UIWidget()
    w.show()
    sys.exit(app.exec_())