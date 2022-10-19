print('**** PROGRAM BEGIN *******')
g=9.8
def fun3(x):
    global g
    print('fun3 start')

    print('stack frame of fun3: ', locals())

    print('fun3 end')

def fun2(n):
    print('fun2 start')
    y = 30
    n = n + 1
    print('stack frame of fun2: ', locals())
    print('fun2 end')

def fun1(n):
     print('fun1 start')
     n = n + 1
     x = 20
     print('stack frame of fun1: ', locals())
     print('fun1 end')

def main():
     print('Main starts here')
     a = 100
     b = 200
     print('stack frame of main: ', locals())
     print('Main ends here')

main()
fun1(40)
fun2(50)
fun3(60)
print('**** PROGRAM END *******')