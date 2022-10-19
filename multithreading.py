'''import threading
import time
lk= threading.Lock()
data=[]
def fun(n):
    for i in range(1,n):
        lk.acquire()
        print('child:'+str(i))
        data.append(i)
        lk.release()
        time.sleep(1)
    print('child thread is done!')
if __name__=='__main__':
        th =threading.Thread(target=fun,args=(11,))
        th.start()
        for i in range(11,17):
            lk.acquire()
            print('main:'+str(i))
            data.append(i)
            lk.release()
            time.sleep(1)
        print('merging two lists and summation...')
        print(data)
        print('sum = ',sum(data))
        print('main thread is done..!') '''
from threading import Thread,current_thread,Lock
import time
lock = Lock()
balance = 0
def deposite(start,stop):
    for i in range(start,stop):
        global balance
        lock.acquire()
        balance+=20
        lock.release()
        print('father deposited,balance ={}\n'.format(balance))
        time.sleep(1)
    print('depositer ends')
def withdraw(start,stop):
    for i in range(start,stop):
        global balance
        lock.acquire()
        if balance>=10:
            print('bal = {},thread={}'.format(balance,current_thread))
            balance-=10
        else:
            print('Insufficent funds! for {},bal={}'.format(current_thread,balance))
        lock.release()
        time.sleep(1)
    print('withdrawer ends')

def main():
    th1=Thread(name='ramu',target=withdraw,args=(0,10))
    th2=Thread(name='samu',target=withdraw,args=(0,10))
    th3=Thread(name='gamu',target=withdraw,args=(0,10))
    
    th3.start()
    th1.start()
    th2.start()

    th1.join()
    th2.join()
    th3.join()
    print('end balance=',balance)
    
if __name__=='__main__':
    main()
              
