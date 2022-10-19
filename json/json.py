import json
book = [{ 'title': 'Let Us C',
    'type': 'short',
    'Authors' : {'author1' : 'Yaswanth Kanetkar',
    'author2' : 'sahani'},
    'publisher': ['bpb', 'wrox', 'pearson', 'appress'],
    'Pages': 230,
    'price': 560.0,
    'published': True,
    'solution_booklet': None},
    { 'title': 'Python Programming', 
    'type': 'long',
    'Authors' : {'author1' : 'Narendra Allam'},
    'publisher': ['bpb', 'wrox', 'pearson', 'appress'],
    'Pages': 650,
    'price': 750.0,
    'published': False,
    'solution_booklet': None}
]
f = open('books.json', 'w')
json.dump(book, f, encoding='utf-8')
f.close()
