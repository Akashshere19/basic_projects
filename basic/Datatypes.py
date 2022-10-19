# String, we can not str(character) convert into int or float bcoz str is upper and int,float is lower datatype

'''
a="Akash"
b="1234"
c='ak123'
print(a,b,c)
print(type(a),type(b),type(c))
s='akash'
print(s,type(s)
x='123'
x=int(x) # convert str into int
print(type(x),x)'''
'''
print(str(12132)) # convert int into str

a=('A')
b=('B')
print(a+b)
a='Akash'
print(a[1:3],type(a))
a=str(4572) # int convert into str
print(a)
print(type(a))
b='2626'
a=int(b) # str convert into int
print(type(b))
print("we convert here str into num:",a,type(a))
print('fun'+'trial'+'its'*3)'''

"""
x='''this is string'''
print(x)"""

'''
a='Akash' #A=0 k=1 a=2 s=3 h=4 h=-1 s=-2 a=-3 k=-4 A=-5
b=a
print(a[-1]) # last chr
print(b[2]) # 3rd chr
print(b[0]) # 1stchr
print(a[-5]) # 1st ch
print(a[0::]) #start:stop:step
print(a[-1::]) # start from last but step not define 
print(a[::-1])  # print reverse pattern
print(a[-2:3:]) # print  nothing becoz strat from -ve end at +ve but step not
print(a[3:-2:1]) # print(shs)
print(a[-1:4:-1])
print(a[1])
print(a[-4])
print(a[-6+2])# print after calculation
print(a[-1:-2:]) # print nothing becoz need to write step
print(a[1:5]) # when print +ve then need not write step '''

#integer
'''
a=10
print(a,type(a))
a=16172
print(a)
b=12.5
print(b,type(b))
c=int(b)
print('we convert 12.5 float into int',(c),type(b),type(c))

a=1
b=str(a) #convert int into str
print(b)
print(type(b))'''

#float
'''
a=12.9
print(a,type(a))
b=.6
print(b,type(b))

a=15
b=float(a)
print(b,type(b))

a=165.05
b=str(a) #convert float into string
print(b)
print(type(b))'''

#complex
'''
a=2+8j
print(a,type(a))


x=12
y=complex(x)
print(y)

a=2+5i #i is not complex value only j
print(a)
a=2+3j
b=3j
print(a+b)
a=2+3j
b=3
print(a+b)

a=2+3j
v=2j
print(a+v) '''

#Frozenset
'''
a="akash shere"
b=frozenset(a)
print(b,type(b)) ''' 


x='this is Python but we use java'

'''
print(x[0]) #print 0 index position character

print(x[5]) #print 5th index position character

print(x[1:7]) #print 1 to 6 index position character becoz for +ve string its doesnt print last 

print(x[1:7:2]) #print 1 to 6 index position character but use step by 2 becoz for +ve string its doesnt print last

print(x[-1]) #print -1 index position character becoz -ve start from -1 not for 0

print(x[-6]) #print -6 index position character becoz -ve start from -1 not for 0

print(x[-1:-9:-1]) # print -1 to -9 index position character  becoz for string its doesnt print last

print(x[::-1]) # print all string in reverse pattern

print(x[:-5]) #it start with 0 position but end with -5
print(x[::-5]) # print in reverse but step is 5

print(x[-4::])  #it start with -4 end end with +ve position

print(x[::]) #print all string

print(x[-22:14:]) # print only python but start with -ve index

print(x[-17:-23:-1]) #print only python in reverse pattern

print(x[:2],x[:-2],x[-2:])
print(x.replace('is','IS'))
print(x.replace(x[5],"I"))

st="Hello World"
print (st.replace(st[6],"#"))

x="Akash shere akash"

print(x.replace(x[0],x[0].upper()))'''




# example for 2 nd chacter delete in given string
'''
x='akash shere'
print("its original string:",x)
new_str =""
for i in range(len(x)):
    if i!=2 :
        new_str = new_str + x[i]
print("This is new string:",new_str)
# 2nd way
x="akash shere"
print("original string:"+x)
new_str = x[:2] + x[3:]
print(new_str)
#3rd way
x='akash shere'
new_str = ''.join([x[i] for i in range(len(x)) if i !=2])
print(new_str)'''  

# calculate only 'a' how many times come
'''
x='this is Python but we use java aaaaaaa'
print("its original string:",x)
new_str =""
for i in range(len(x)):
    if x[i]=='a':
        new_str = new_str+x[i]
        
print(len(new_str)) '''       



   


#1st character print Upper case
'''
x='akash shere'
y=x[0:1:].upper()+x[1:]
print(y)
#2nd way
print(x.title())'''

'''
s='abcdefghij'
print(s[0:4]+s[5:]) # e will not print 

print(s[0].upper() + s[1:]) #1 st chacter will print  upper case

'''
'''
x="This is your {}th atempt and your attempt remaining is {}"  # use {} for index for place 
print(x.format(3,2)) #format is add int or float into str

y="This is your {}th atempt and your attempt remaining is {}"

x=5
z=4.1
print(y.format(z,x))


x="This is your {}th atempt and your {} attempt remaining is {}"
s='as'
a=1
c=3
print(x.format(c,s,a))'''

'''
p="welcome in \"New\" python world" #print "new" as it
print(p)

a="my name is 'Akash' "
print(a)
a="My name is \"Akash\" " #print Akash in double Inverted comma

print(a)


x="This is your \npython world" #printsome part in new line

print(x)

x="This is your \tpython world" #printsome part in tab

print(x)


x="This is your \'python world" #print ' before python

print(x)

x="This is your \\python world" #print \ before python

print(x)


x="This is your \bpython world" #printbackshlash before python

print(x)


x="This is your \fpython world" #print sq before python

print(x)  '''


'''
x="this is your python world" 

print(x.capitalize()) #print 1st letter of string will print capital

print(x.count('i')) # print character i how many times came in string

print(x.find('t')) # showing index no of t
print(x.find('G')) # showing G place
print(x.find('p'))
print(x.find('G'))
print(x.index('i')) # shown index no of that character 

print(x.index('p')) # index and find both are same work
print(x.islower())
a="akash"
print(a.replace('a','A')) #replace is change any letter to other '''

'''
a="Akash"

print(a.islower())
print(a.islower()) #show false becoz all letter is not lowercase

print(a.isupper()) #show false becoz all letter is not uppercase

print(a.lower()) #will print in lower case

print(a.upper()) #will print in upper case  '''

'''
a=("akash shere from akola")
p=(a.split()) #split is convert string into list
print(p)

print(type(p))

print(a.strip())

print(a)

s="akash shere"
print(s[2:4])
print(s.index('s')) #showing index of charct s
print(s.capitalize()) #1st letter will capitalize
print(s.count('a')) #count no of letter a
print(s.find('g')) # 
print(s.index('a'))

a="Akash shere"
print(a[:2],a[-2:],a[:-2])'''

# strings concatination :it add two str 
a="Aka"
b="sh"
s=a+b
print(s)



#Boolean : its output comes in either True Or False only
'''
a=(212)
print(bool(a))
print(a.__bool__())

a=3
b=7
c=(a>b)
print(c,type(c))

print(bool("Hello"))

x=(bool(15))
print(x,type(x)) '''


'''
class myclass(): #create boolean datatype
  def __len__(self):
    return 1

myobj = myclass() for 1
print(bool(myobj)) 


class myclass():
    def __len__(self):
        return 0
myjob = myclass() #for 0
print(bool(myjob)) 

x = 200
print(isinstance(x, int)) #create boolean datatype

'''


print('ABC'.lower()) #will print in lower case


'''

#Write a program to print every character of a string entered by user in a new line using loop.

x=input(str('enter string'))
for i in x:
    print(i)


# Write a program to find the length of the string "refrigerator" without using len function.
x= "refrigerator"
c=0
for i in x:
    c+=1
print(c)   ''' 
'''
# Write a program to check if the letter 'e' is present in the word 'Umbrella'.
w = 'Umbrella'

print(w.find('e')) #show index no

print ('e' in 'Umbrella') # show output in boolean


#Write a program to check if the word 'orange' is present in the "This is orange juice".
print('orange' in "This is orange juice")

a= "This is orange juice"
print('orange' in a.split())

x="akash shere"

print('sh' in x.split()) #this is not shown one letter

print('shere' in x.split()) #show only word '''

'''Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is.
For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.'''

'''
b= "Akash Arunkumar Shere"

b=b.split()

c=b[0][0]+'.'+b[1][0]+'.'+b[2]
print(c) '''

# Check the occurrence of the letter 'e' and the word 'is' in the sentence "This is umbrella".
c="This is umbrella"
print('e'  in c)
print('is' in c.split())

'''
# Write a program to find the number of vowels, consonents, digits and white space characters in a string.

st = "greeks for greeks121 @"

vowel='aeiou'
consonant = 'bcdfghjklmnpqrstvwxyz'
space =  ' '
digit ='0123456789'
spec_sign='@!/\,.;:+-'

vowel_count  = 0
consonant_count = 0
digit_count = 0
space_count = 0
spec_count =0 
print('Original string:',st)
for i in st:
    if i in vowel:
        vowel_count +=1
    elif i in consonant:
        consonant_count +=1
    elif i in space:
        space_count +=1
    elif i in spec_sign:
        spec_count +=1
    else:
        digit_count +=1
print('vowel_count:',vowel_count)
print('consonant_count:',consonant_count)
print('digit_count:',digit_count)
print('space_count:',space_count)
print('spec_sign:',spec_count)        
'''
'''
#Write a program to make a new string with all the consonents deleted from the string "Hello, have a good day".
s = "Hello, have a good day"
a=['a','e','o','u','i','A','E','O','U','I']

for i in s:
    if i not in a:
        s=s[:s.index(i)]+s[s.index(i)+1:]
print(s)

s = "Hello, have a good day"
a=['a','e','o','u','i','A','E','O','U','I']
for i in s:
    if i in a:
        s=s[:s.index(i)]+s[s.index(i)+1:]
        print(s)
print(s)
        '''
'''
# Write a program to find out the largest and smallest word in the string "This is an umbrella".

st = "This is an umbrella"
st= st.split()
maxx =st[0]
max_len = len(st[0])
for i in st :
    if len(i) > max_len :
        max_len = len(i)
        maxx =i
print(maxx)

 # for Min
 
st = "This is an umbrella"
st= st.split()
minn =st[0]
min_len = len(st[0])
for i in st :
    if len(i) < min_len :
        
        min_len = len(i)
        minn =i
print(minn)
'''

'''
#Take two number and
#check whether the sum is greater than 5, less than 5 or equal to 5.

x=4
y=3
s=x+y
if s==5:
    print("is same",s==5)
elif s>5:    
    print("is greater ",s>5)
else:    
    print("is less ",s<5)'''

'''
#Judge the follwing expressions :
#not(True and True)
#True or False
#not(False and True)
#False and False

print(not(True and False))
print(True and False)
print(False and False) '''

'''
#Suppose passing marks of a subject is 35.
# Take input of marks from user and check whether it is greater than passing marks or not.


mark =(int(input("enter mark:")))

if 35 >mark :
    print("fail")
elif mark ==35:
    print("pass but mark is 35")
else:
    print("pass") '''



s='akash shere'
print('akash' in s.split())




