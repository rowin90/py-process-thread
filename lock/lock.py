import threading

lock = threading.Lock()
class Account:
    def __init__(self, balance):
        self.balance = balance


def drawWithLock(account, amount):
    with lock:
        if (account.balance >= amount):
            print(threading.currentThread().name, '取成功')
            account.balance -= amount
            print(threading.currentThread().name, '余额', account.balance)
        else:
            print(threading.currentThread().name, '取失败，余额不足')
def draw(account, amount):
    if (account.balance >= amount):
        print(threading.currentThread().name, '取成功')
        account.balance -= amount
        print(threading.currentThread().name, '余额', account.balance)
    else:
        print(threading.currentThread().name, '取失败，余额不足')


if __name__ == '__main__':
    account = Account(1000)
    ta = threading.Thread(target=draw, args=(account, 800))
    tb = threading.Thread(target=draw, args=(account, 800))

    ta.start()
    tb.start()
