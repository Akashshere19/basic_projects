print('PROGRAM BEGIN') # global variable
v1 = 9.8 # global variable


def myfunc1(p1):
    print('myfunc1 begin')
    print('in side myfun1')
    x=50
    y=70
    p1=p1*10
    print("LOCALS")
    print(locals())
    print("GLOBALS")
    print(globals())
    print(' myfunc1 end')

def myfunc2():
    print(' myfunc2 begin')
    print('in side myfunc2')
    x=20
    y=30
    myfunc1(40)
    print("LOCALS")
    print(locals())
    print("GLOBALS")
    print(globals())
    print(' myfunc2 end')

myfunc2()
print(globals())
print('PROGRAM END')
