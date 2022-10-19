def factrl(a):
    f=1
    for x in range(1,a+1):
        f=f*x
    print('factorial of {} = {}'.format(a,f))
    return f

n=5
r=3
res= (factrl(n)/ factrl(n-r)) * factrl(r)
print(res)