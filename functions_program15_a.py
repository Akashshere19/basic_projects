print('**** PROGRAM BEGIN *******')
g1=9.8
def myfun1():
    print('~~~~~~ myfunc1 begin ~~~~~~~')
    global g1
    #print("in function 1 before",g1)
    g1=999
    print(locals())
    print("in function 1 after", g1)
    print('~~~~~~ myfunc1 end ~~~~~~~')

def myfun2():
    print('--- myfunc2 begin ------')
    global g1
    print("in function 2 before " ,g1)
    myfun1()
    print("in function 2 After ", g1)
    print('--- myfunc2 end ------')

myfun2()
print(g1)
print('**** PROGRAM END *******')