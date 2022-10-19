def add(x, y=0, z=0):
    r=x+y+z
    return r

print('-------------------')
sum1=add(22)
print(sum1)
print('-------------------')
sum=add(22,33)
print(sum)
print('-------------------')
sum1=add(22,43,5)
print(sum1)
print('-------------------')
sum1=add(22,z=43,y=5)
print(sum1)
print('-------------------')
a=5
b=7
sum2=add(y=a,z=20,x=b)
print(sum2)
print('-------------------')