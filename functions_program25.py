def func() :
    print(' hello i am function body')
    print(' hello friends')
    print(' function end')
    return  100

print(func)
print(type(func))
print(id(func))

func()


print('=======================================')

x= func
print(x)
print(type(x))
print(id(x))

x()

