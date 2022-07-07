import sys

from PySide2.QtWidgets import QLineEdit, QPushButton, QWidget, QApplication


class MyApp(QWidget):
    count = 0
    num_str = ""
    num_int = 0
    num_save = 0
    state = 'none'
    result = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.widget()
        self.setWindowTitle('app')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def widget(self):
        self.line_edit = QLineEdit(" ", self)
        self.line_edit.move(180, 20)
        self.line_edit.setEnabled(False)

        bt1 = QPushButton('1', self)
        bt2 = QPushButton('2', self)
        bt3 = QPushButton('3', self)
        bt4 = QPushButton('4', self)
        bt5 = QPushButton('5', self)
        bt6 = QPushButton('6', self)
        bt7 = QPushButton('7', self)
        bt8 = QPushButton('8', self)
        bt9 = QPushButton('9', self)
        bt0 = QPushButton('0', self)

        plus = QPushButton('+', self)
        mins = QPushButton('-', self)
        double = QPushButton('*', self)
        dot = QPushButton('.', self)
        clear = QPushButton('c', self)
        end = QPushButton('=',self)

        bt1.setGeometry(20, 20, 30, 30)
        bt2.setGeometry(60, 20, 30, 30)
        bt3.setGeometry(100, 20, 30, 30)
        bt4.setGeometry(20, 60, 30, 30)
        bt5.setGeometry(60, 60, 30, 30)
        bt6.setGeometry(100, 60, 30, 30)
        bt7.setGeometry(20, 100, 30, 30)
        bt8.setGeometry(60, 100, 30, 30)
        bt9.setGeometry(100, 100, 30, 30)
        bt0.setGeometry(60, 140, 30, 30)

        plus.setGeometry(140, 20, 30, 30)
        mins.setGeometry(140, 60, 30, 30)
        double.setGeometry(140, 100, 30, 30)
        dot.setGeometry(100, 140, 30, 30)
        end.setGeometry(180, 140, 30, 30)
        clear.setGeometry(140, 140, 30, 30)

        bt1.clicked.connect(self.one)
        bt2.clicked.connect(self.two)
        bt3.clicked.connect(self.three)
        bt4.clicked.connect(self.four)
        bt5.clicked.connect(self.five)
        bt6.clicked.connect(self.six)
        bt7.clicked.connect(self.seven)
        bt8.clicked.connect(self.eight)
        bt9.clicked.connect(self.nine)
        bt0.clicked.connect(self.zero)

        plus.clicked.connect(self.plus)
        mins.clicked.connect(self.minus)
        clear.clicked.connect(self.clear)
        end.clicked.connect(self.end)

    def one(self):
        self.number('1')

    def two(self):
        self.number('2')

    def three(self):
        self.number('3')

    def four(self):
        self.number('4')

    def five(self):
        self.number('5')

    def six(self):
        self.number('6')

    def seven(self):
        self.number('7')

    def eight(self):
        self.number('8')

    def nine(self):
        self.number('9')

    def zero(self):
        self.number('0')

    def number(self, i):
        self.line_edit.insert(i)
        self.num_str += i
        self.num_int = int(self.num_str)

    def plus(self):
        self.result += self.num_int
        print(self.result)
        self.state = 'plus'
        self.num_int = 0
        self.num_str = ""
        self.line_edit.insert('+')

    def minus(self):
        self.result -= self.num_int
        self.state = 'mim'
        print(self.result)
        self.num_int = 0
        self.num_str = ""
        self.line_edit.insert('-')

    def end(self):
        self.line_edit.clear()
        self.line_edit.insert(str(self.result))
        self.num_str = ""
        self.num_int = 0
        self.result = 0

    def clear(self):
        self.line_edit.clear()
        self.num_str = ""
        self.num_int = 0
        self.result = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    
    
    #주석입니다
    # THIS IT TESTff
