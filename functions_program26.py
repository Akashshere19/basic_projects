def greet():
    print('hello welcome')
    print(' i am greet function')


def func(f):
    print('~~~~~~~~~~~',f,type(f), id(f))
    f()
    print('*******')

print(greet, type(greet), id(greet))
print(func, type(func), id(func))
print('---------------------------------')
func(greet)
