print('MAIN PROGRAM START')
v1 = 100
v2 = 200

def func1(i,j):
    print(' starting function 1')
    global v1, v2
    x=1
    y=2
    print(' i = ', i)
    print(' j = ', j)
    v1=1188
    v2=2299
    print(locals())
    print(globals())
    print(' x = ', x)
    print(' y = ', y)
    print(' v1 = ', v1)
    print(' v2 = ', v2)
    print(' ending function 1')

def func2(a,b):
    print('starting function 2')
    global v1, v2
    m=111
    n=222
    print(locals())
    print(globals())
    print(' a = ', a)
    print(' b = ', b)
    print(' m = ', m)
    print(' n = ', n)
    print(' v1 = ', v1)
    print(' v2 = ', v2)
    print(' ending function 2')

func1(88,99)
func2(55,77)
print(globals())
print(' v1 = ', v1)
print(' v2 = ', v2)
