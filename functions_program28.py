def add(x,y):
    print("add function : x={} + y={} = {}".format(x,y,x+y))

def volume(h,l,b):
    print('volume = {} * {} * {} = {} '.format(h,l,b,h*l*b))


def compute(work,*args,**karg):
    print('aaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(work)
    print(args)
    print(karg)
    work(*args,**karg)         # add(12,34)          /      volume(b=2,h=8,l=5)
    print('bbbbbbbbbbbbbbbbbbbbbb')


compute(add,12,34)
print('-------------------')
compute(volume,b=2,h=8,l=5)
