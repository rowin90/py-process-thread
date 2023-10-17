import threading

Rlock = threading.RLock()
class Account:
    def __init__(self, balance):
        self.balance = balance


def drawWithLockManual(account, amount):
    """
    手动加锁，释放锁
    :param account:
    :param amount:
    :return:
    """
    Rlock.acquire() # 加锁
    if (account.balance >= amount):
        print(threading.currentThread().name, '取成功')
        Rlock.acquire() # 加锁
        account.balance -= amount
        Rlock.release()
        print(threading.currentThread().name, '余额', account.balance)
    else:
        print(threading.currentThread().name, '取失败，余额不足')

    Rlock.release()

if __name__ == '__main__':
    account = Account(1000)
    ta = threading.Thread(target=drawWithLockManual, args=(account, 800))
    tb = threading.Thread(target=drawWithLockManual, args=(account, 800))

    ta.start()
    tb.start()
