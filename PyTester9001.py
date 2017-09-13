import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI.MainForm import Ui_PyTester9001


class PyTester9001(QMainWindow, Ui_PyTester9001):
    def __init__(self):
        super(PyTester9001, self).__init__()
        self.setupUi(self)

        # Connect up signals
        self.startQuizButton.clicked.connect(self.update_text)

    def update_text(self):
        self.questionText.setText("Test")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myGui = PyTester9001()
    myGui.show()
    sys.exit(app.exec_())
