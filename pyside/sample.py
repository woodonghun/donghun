import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QLabel, QComboBox, QApplication, QPushButton, QLineEdit, QCheckBox, QRadioButton, \
    QButtonGroup


class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.widget()
        self.setWindowTitle('Title')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def widget(self):

        self.label1 = QLabel('First', self)
        self.label1.resize(300, 20)
        self.label2 = QLabel('second', self)
        self.label2.resize(300, 20)

        self.line = QLineEdit(self)
        self.line.move(30, 200)

        self.label1.move(100, 30)
        self.label2.move(100, 60)

        rbtn1 = QRadioButton('First Button',self)
        rbtn1.move(30, 150)
        rbtn1.setChecked(True)
        rbtn1.toggled.connect(self.radio1)

        rbtn2 = QRadioButton('Second Button', self)
        rbtn2.move(130, 150)
        rbtn2.toggled.connect(self.radio2)

        rbtn3 = QRadioButton(' third button', self)
        rbtn3.move(230, 150)
        rbtn3.toggled.connect(self.radio3)

        radioG = QButtonGroup()
        radioG.addButton(rbtn1)
        radioG.addButton(rbtn2)
        radioG.addButton(rbtn3)

        cb1 = QComboBox(self)
        cb1.addItem('1')
        cb1.addItem('2')
        cb1.addItem('3')
        cb1.addItem('4')
        cb1.addItem('5')
        cb1.setGeometry(30, 30, 70, 20)

        cb2 = QComboBox(self)
        cb2.addItem('option1')
        cb2.addItem('option2')
        cb2.addItem('option3')
        cb2.addItem('option4')
        cb2.addItem('option5')
        cb2.setGeometry(30, 60, 70, 20)

        self.imp = QPushButton('import', self)
        self.exp = QPushButton('export', self)

        self.exp.clicked.connect(self.exp_clicked)
        self.imp.clicked.connect(self.imp_clicked)

        self.imp.move(30, 100)
        self.exp.move(100, 100)

        cb1.activated[str].connect(self.onActivated_1)
        cb2.activated[str].connect(self.onActivated_2)

        cbb = QCheckBox('show title', self)
        cbb.move(180, 100)
        cbb.toggle()
        cbb.stateChanged.connect(self.changeTitle)

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

    def onActivated_1(self, text):
        self.label1.setText(text)
        self.label1.adjustSize()

    def onActivated_2(self, text):
        self.label2.setText(text)
        self.label2.adjustSize()

    def exp_clicked(self):
        self.label2.clear()
        text = self.line.text()
        print(text)
        self.label2.setText(text)

    def imp_clicked(self):
        text = self.label1.text()
        print(text)
        self.line.setText(text)

    def radio1(self):
        text1 = self.label1.text()
        self.line.setText(text1)

    def radio2(self):
        text2 = self.label2.text()
        self.line.setText(text2)

    def radio3(self):
        text1 = self.label1.text()
        text2 = self.label2.text()
        text = text1 + text2
        self.line.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())
# test