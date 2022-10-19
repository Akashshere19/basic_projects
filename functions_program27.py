print(' i am main program')
i = 40

def func():
    pi = 22/7.0
    def area(r):
        a=pi*r*r
        print('area =',a)
        return a
    return area

#x = func()
#print(x,type(x), id(x))
#print(x(4))
print(func()(5))


