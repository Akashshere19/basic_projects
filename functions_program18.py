def swap2vals(a, b):
    print('function start')
    print("a={} id is {} ,  b={} id is {}".format(a,id(a), b,id(b)))
    print('-------------------')
    a,b = b,a
    print("a={} id is {} ,  b={} id is {}".format(a, id(a), b, id(b)))
    print('function end')


x = 20
y = 30
print('x= {}--- id is {}'.format(x,id(x)))
print('y= {}--- id is {}'.format(y,id(y)))
swap2vals(x, y)
print('x = ', x, ' y = ', y)
print('x= {}--- id is {}'.format(x,id(x)))
print('y= {}--- id is {}'.format(y,id(y)))



