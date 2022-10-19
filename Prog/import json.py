import json
'''import json
book = { 'title': 'Let Us C',
'_type': 'short',
'Authors' : ['Yaswanth Kanetkar', 'sahani'],
'Pages': 230,
'price': 560.0,
'published': True,
'solution_booklet': None}
s = json.dumps(book)
with open('book.json', 'w') as f:
 f.write(s)'''

'''
b = {}
with open('book.json', 'r') as f:
 s = f.read()
 b = json.loads(s)
print (b)'''

'''book=[{'title':'C++','type':'short','auther':{'auther1':'kanatkar','auther2':'sahani'},
        'bubliser':['bpp','wrox','pearson'],'pages':'250',
        'price':'Rs.750.90'},{
        'title':'python programing',
        'type':'text'},
        {'auther':{'auther1':'kanatkar','auther2':'bose'},
        #'price':{'Rs.560','$.10'},
        #'weight':('120gm','0.12kg'),
        'published':'False',
        'Softcopy':'None'}]
f= open ('books.json', 'w')
json.dump(book, f)
f.close()'''
f= open('books.json', 'r')
d = json.load(f)
print(d)