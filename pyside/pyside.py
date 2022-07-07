import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox, QRadioButton, QComboBox, QLineEdit, \
    QVBoxLayout, QGridLayout, QHBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignCenter)

        font1 = label1.font()
        font1.setPointSize(20)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        cb = QCheckBox('title', self)
        cb.toggle()
        cb.move(20, 10)
        cb.stateChanged.connect(self.changeTitle)

        rbtn1 = QRadioButton('First Button', self)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.setText('Second Button')

        Button = QVBoxLayout()
        layout.addWidget(cb)
        layout.addWidget(rbtn1)
        layout.addWidget(rbtn2)

        grid = QHBoxLayout()
        grid.addLayout(layout)
        grid.addLayout(vbox)
        grid.addLayout(Button)
        self.setLayout(grid)

        self.setWindowTitle('QPush')
        self.setGeometry(300, 300, 300, 200)

        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# test test