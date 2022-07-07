class Human:
    def cry(self, cry):
        for i in range(len(cry)):
            print(cry[i])

    def call(self, human, number):
        print("{}에게 {} 발신중".format(human, number))

    def gugu(self, num1, num2):
        print(num1 * num2)

    def sign(self, name):
        label = "X" * (len(name)-2)
        print(name[0] + label + name[-1])

class 구구단:
    def print(self, num):
        for i in range(1, 10):
            print("{}X{}={}".format(i, num, i*num))

man = Human()
man.call("김철수", "0109123287")
man.gugu(3,1)
man.sign("어아아아아")

m=구구단()
m.print(6)

