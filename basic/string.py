
#capitalize
#casefold
#center
#count
#encode
#endswith
#startswith
#replace
#format
#format_map
#index
#join
#lower
#upper
#partition
#title
#swapcase
#strip
#split


#isalnum
#isalalpha
#isascii
#isdigit
#isnumeric
#isprintable
#islower
#isupper
#istitle
#isspace
#ljust
#lstrip



#maketrans
#removeprefiix
#removesuffix

#rfind
#rindex
#rfind
#rpartition
#rstrip

#translate
#splitlines
#zfill

'''
s='akash shere'
print(s.index('s',5))
#print(s.casefold())
print(s.format_map('a'))
#print(s.center(s))
print(s.swapcase())
print(s.lstrip())

s= str("hello this is akash shere")
print(max(s))
print(min(s)) '''
'''
s=['akash','rahul','rohit',23]
a=s.sort()
print(a) '''


'''
s="python learn and burn"
for leaf in [*range(10)]+[2]:
    #print(leaf)
    print(f'{"*"*(leaf*2+1):30}')


print(reversed(s),sep ='')'''

'''
# replace 's' by 'S'

s="akash"
s=s[0:3]+'S'+s[4:]
print(s)

s="Akash"
print(s.replace('s','D')) 

s='akash shere santaji nagar'


s=s[0:6]+'SHERE'+ s[11:]
print(s) '''

'''
s='akash shere santaji nagar'

s1=[1,2,3,4,5]
for i in s:
     s1[i]=s1[i]+i
     print(s1[i])'''


'''
s= 'galaxy'

print(s[:-2]+s[-3::-1])
print(s[:-2]+s[-2:]) '''

'''
def func(a,*args):
     print(a)
     #print(*args)
     print('\n')
     for arg in args:
          
          print(arg)
func("A","B","C",'d','e','f','g')
#print(args) '''

'''
def ping(i):
     if i > 0:
          return pong(i-1)
     return "0"

def pong(i):
     if i>0:
          return ping(i-1)
     return '1'
print(ping(29)) '''





