l=[]
for x in range(1,11):
    l.append(x)
print(l)    

l=[i for i in range(1,11)]
print(l)

c=[(x,y) for x in ['a','b'] for y in ['p','q']]
print(c)

temp=[98,93,92,97,99,96,97,100]
cel=[(f-32.0)/(9.0/5.0) for f in temp]
print(cel)     
