def modify(p):
    print(' in the modify  before: ',p, '   ', id(p))
    p[1] = 555
    print(' in the modify  after: ',p, '   ', id(p))

def main():
    l = [11, 22, 33]
    print(' in main :',  l,'   ', id(l))
    modify(l)
    print(l)

main()