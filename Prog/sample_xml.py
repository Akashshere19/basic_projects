import xml.etree.ElementTree as ET
root=ET.Element('book')
title = ET.Element('title')
title.attrib = {'type':'short'}
title.text = 'Lest Us C'

auther1 = ET.Element('auther')
auther1.text='yaswant Kanetkar'
auther2 = ET.Element('auther')
auther2.text = 'venu Gopal'
pages =ET.Element('pages')
pages.attrib = {'size':'A5','color':'white'}
pages.text  ='230'
pages.tail = '5'

_id = ET.Element('id')
isbn = ET.Element('isbn')
isbn.text = '1234465263'
isbn12=ET.Element('isbn12')
isbn12.text = '121312123'
_id.append(isbn)
_id.append(isbn12)

root.append(title)
root.append(auther1)
root.append(auther2)
root.append(pages)
root.append(_id)
for item in root:
    print(item.tag, item.attrib, item.text, item.tail)
s = ET.tostring(root, encoding='utf8', method='xml')
print (s,sep='\n')
print(type(s))
with open('book.xml', 'w') as f:   
    f.write(s)