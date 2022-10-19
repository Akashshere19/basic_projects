'''for i in range(5):
    print(i)
    
i=1
while i<11:
    print(i)
    i+=1

for x in range(0,11,2):
    print(x)'''

'''
#sum
s=0    
for x in range(1,10):
    s+=x
print(s)    

#product
s=1    
for x in range(1,10):
    s*=x
print(s) 
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print('*',)
    print('')    

for i in range(1,6):
    for j in range(1,i+1):
        print(i)
    print('')'''    
n=int(input('enter a no:'))
r=int(n**0.5)
i=2
while i <=r:
    if n%i ==0:
        print('not prime')
        break
    i+=1
if i >r:
    print('prime')




    
