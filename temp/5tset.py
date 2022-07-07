import random


class Account:
    account = 0

    # 이름 초기 돈, 기타 base
    def __init__(self, name, mount):

        self.name = name
        self.mount = mount

        self.mount_log = []
        self.withdraw_log = []
        self.bank = "SC 은행"

        # 계좌 생성~
        A = ""
        for hjh in range(11):
            hjh = random.randint(1, 10)
            A += str(hjh)

        self.code = A[:3] + "-" + A[3:5] + "-" + A[5:]
        # ~계좌 생성

        Account.account += 1
        self.deposit_count = 0

    # 계좌 번호 출력
    def get_account_num(self):

        print(self.account)

    # 입금
    def deposit(self, money):

        if money > 1:
            self.mount_log.append(money)
            self.deposit_count += 1
            self.mount += money
            if self.deposit_count % 5 == 0:
                self.mount = self.mount * 1.01
            else:
                pass

    # 입금 내역
    def deposit_history(self):

        for lk in self.mount_log:
            print(lk)

    # 출금
    def withdraw(self, mount):

        self.withdraw_log.append(mount)

        if self.mount < mount:
            pass
        else:
            self.mount -= mount

    # 출금 내역
    def withdraw_history(self):

        for lh in self.withdraw_log:
            print(lh)

    # 정보 출력
    def display_info(self):
        print("은행 이름 : ", self.bank)
        print("예금주 : ", self.name)
        print("계좌 번호 : ", self.code)
        print("잔고 :{0:,} ".format(self.mount))


ev_account = []

p = Account("피이", 10000)
o = Account("오이", 20000)
f = Account("아이", 50)

p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(3)
o.deposit(10)
o.deposit(10)
o.deposit(10)
o.deposit(10)
o.deposit(10)

ev_account.append(p)
ev_account.append(o)
ev_account.append(f)

for q in range(len(ev_account)):
    if ev_account[q].mount > 100:
        ev_account[q].display_info()

# 함수를 알지 못하면 길어짐...
a = input()
z = list(a)
for i in range(len(a), 0, -1):
    if i > 2:
        if len(a) % 3 == 1:
            if i % 3 == 0:
                z.insert(i - 2, ",")
        if len(a) % 3 == 2:
            if i % 3 == 1:
                z.insert(i - 2, ",")
        if len(a) % 3 == 0:
            if i % 3 == 2:
                z.insert(i - 2, ",")
print("".join(z))
# 3자리 이상 숫자 단위 표시는 {0:,}.format() 으로 한번에 됨
# ex) print("잔고 :{0:,} ".format(self.mount))
