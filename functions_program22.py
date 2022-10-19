import copy

def modify(p):
    p[1][1] = 999
    print(p, ' p in modify function')

def main():
    l = [7, [4, 3, 5], 9]
    print(l)
    modify(copy.copy(l))
    print(l, ' l in main')

if __name__ == '__main__':
    main()