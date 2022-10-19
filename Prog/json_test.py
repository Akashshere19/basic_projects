import json
new=[{
    'book':'c++','auther':'soham',
    'price':{'Rs':'2250','$':'15'},
    'softcopy':None,
    'published':False,
    'copies':123,
    'country':'india'   
}]
s=json.dumps(new)
with open('book.json', 'w') as e:
    e.write(s)
''''    
b = {}
with open('book.json', 'r') as f:
 s = f.read()
 b = json.loads(s)
print (b)    
print(type(new[0]))'''

with open ('book.json','r') as e:
    d=e.read()
print(d,type(d))    