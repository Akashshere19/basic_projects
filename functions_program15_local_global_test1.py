print('MAIN PROGRAM START')
v1 = 100
v2 = 200

def func1(a,b):
    print('FUNC1 START')
    i=10
    j=20
    print(' a = {} , b= {} , i= {} , j = {}'.format(a,b,i,j))
    v1=777
    v2=888
    print('GLOBAL v1 = {} ,v2 = {} '.format(v1,v2))
    print('.............................')
    print(locals())
    print(globals())
    print('FUNC1 END')

def func2(a,b):
    print('FUNC2 START')
    i=911
    x=44
    print(' a = {} , b= {} , i= {} , x = {}'.format(a,b,i,x))
    v1=29
    print('GLOBAL v1 = {} ,v2 = {} '.format(v1,v2))
    print('.............................')
    print(locals())
    print(globals())
    print('FUNC2 END')


func1(55,66)
func2(90,80)
print('GLOBAL v1 = {} ,v2 = {} '.format(v1,v2))

#print('MAIN PROGRAM END')
#print(func1)
#print(id(func1))
#print(type(func1))