import multiprocessing

def task():
    print(name)
    file_obj.write('alax\n')
    file_obj.flush()


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')

    name = []
    file_obj = open('x1.txt',mode='a+',encoding='utf-8')
    file_obj.write('zzz\n')


    p1 = multiprocessing.Process(target=task)

    p1.start()
