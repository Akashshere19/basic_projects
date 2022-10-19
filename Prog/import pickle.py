import pickle
'''
d={}
d['name']='akash'
d['salary']=7879.78
d['address']='akola'
d['mob']=9766
print(d)
print(type(d))
pf=pickle.dumps(d) # python data converts into byte format that is called pickle
print(pf)
print(type(pf))
f=open('employee.pickle','wb')
f.write(pf)
print('file created') # for check ----> write in terminal cat employee.pickle
f.close() '''
'''
# for read pickle file
f=open('employee.pickle','rb')
b =f.read()
d1=pickle.loads(b)
print(d1)
f.close()'''
d={}
d['id']=123
d['name']='shoham'
d['salary']=1232.90
pf=pickle.dumps(d)
f=open('emp.pickle','wb')
#pickle.dump(d,f,pickle.HIGHEST_PROTOCOL) # it is showing security
f.write(pf)
f.close()