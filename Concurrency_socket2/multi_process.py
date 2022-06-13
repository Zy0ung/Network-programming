from multiprocessing import Process
import os

def info(title):
    print(title) #제목을 print
    print('parent process:', os.getppid()) #부모 process id
    print('process id:', os.getpid()) # 현재 process id

def f(name): 
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line') 
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()