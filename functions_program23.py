import copy

def modify(p):
    print('inside function before ', p,id(p))
    p[2][1] = 999
    print('inside function after ', p, id(p))

def main():
    l = [7, 8, [4, 3, 5], 9]
    print(' in the main before ',l, id(l))
    modify(copy.deepcopy(l))
    print(' in the main after ', l, id(l))
    print(l)

main()
