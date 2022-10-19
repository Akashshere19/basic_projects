def factrl(n):
    if n>1:
        return n * factrl(n-1)
    else:
        return 1

r = factrl(5)
print(r)