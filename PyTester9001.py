import sys
from typing import List
from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox
from UI.MainForm import Ui_PyTester9001
from SQLiteModel import SQLiteModel


class PyTester9001(QMainWindow, Ui_PyTester9001):
    combo_holding_string = "....Please Select"

    def __init__(self):
        super(PyTester9001, self).__init__()
        self.setupUi(self)

        # Connect to Database
        self.model = SQLiteModel("SelfTestOTron.sqlite")
        self.update_ComboBox("moduleComboBox", self.model.modulelist())

        # Connect signals to slots
        self.selectDatabaseButton.clicked.connect(self.holding_slot)  # Select Database
        self.startQuizButton.clicked.connect(self.holding_slot)  # Start Quiz
        self.moduleComboBox.currentIndexChanged.connect(
            lambda: self.moduleComboBox_index_changed(self.moduleComboBox))  # On Module Select
        self.partComboBox.currentIndexChanged.connect(self.holding_slot)  # On Part Select
        self.chapterCombBox.currentIndexChanged.connect(self.holding_slot)  # On Chapter Select
        self.revealAnswerButton.clicked.connect(self.holding_slot)  # Reveal Answer
        self.answerCorrectButton.clicked.connect(self.holding_slot)  # Answer Correct
        self.answerIncorrectButton.clicked.connect(self.holding_slot)  # Answer Incorrect
        self.stopQuizButton.clicked.connect(self.holding_slot)  # Stop Quiz

    def update_ComboBox(self, combo_box_name: str, modules: List[str]):
        if combo_box_name == "moduleComboBox":
            self.partComboBox.clear()
            self.chapterCombBox.clear()
        elif combo_box_name == "partComboBox":
            self.chapterCombBox.clear()

        combo_box = getattr(self, combo_box_name) # type: QComboBox
        combo_box.clear()

        combo_box.addItem(self.combo_holding_string)
        for x in modules:
            combo_box.addItem(x.capitalize())


    # Slots
    def holding_slot(self):
        print("holding")


    def moduleComboBox_index_changed(self, i):
        if i != 0:
            self.update_ComboBox("partComboBox", self.model.partlist(self.moduleComboBox.currentText()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myGui = PyTester9001()
    myGui.show()
    sys.exit(app.exec_())
