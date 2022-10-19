def modify(p):
    print(' IN MODIFY before :',p,id(p))
    p = [44, 55, 66]
    print(' IN MODIFY after :', p, id(p))


def main():
    l = [11, 22, 33]
    print('BEFORE in main :',l, id(l))
    modify(l)
    print('AFTER in main :', l, id(l))
    print(l)

main()
