#GIL - Global Interface Lock 
#파이썬은 인터프리터 차원에서 쓰레드가 동시에 돌아가지 못하게 해놓음.

import threading

x = 0 # global variable shared by threads

def increment():
    global x
    x += 1

def thread_task():
     for _ in range(300000):
        increment()

def main_task():
    global x
    x = 0 # initialize x as 0
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
for i in range(10):
    main_task()
    print('Iteration {0}: x = {1}'.format(i, x))