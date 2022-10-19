# if -else: it is also called conditional statements

'''
i=8.9

if i<=9:
    print("hello")
else:
    print("hi")
print("outside of loop")
if i==8.9:
    if i<=9:
        if i>=3:
            if i==int:
                print("loop1")
            else:
                print("loop2")
        if i <10:
            print("loop3")

            
else:
    print("value is not 8.9") '''
    
'''
x=15
if x==20:
    print("it is equal to 20")
    print(x-4)
    
elif x==15:

    print("it is not equal to 15 ")
    x-6

elif x==12:
    print("it is not equal to 12")
    x-3
else:
    print("try again")'''
'''
x=10   
print('its first') if x==10 else print('second')
print(1<x<30)
print(x < 20 < x*2 < 100)'''

'''
number = int(input("Enter the number?"))  
if number==10:  
    print("number is equals to 10")  
elif number==50:  
    print("number is equal to 50");  
elif number==100:  
    print("number is equal to 100");  
else:  
    print("number is not equal to 10, 50 or 100") '''

'''

mark=int(input("enter marks"))
if 75>mark>60 :
    print("you got 1 st class")
elif 85>mark>70:
    print("you got disctiction")
elif mark>85:
    print("you are top")
if mark<60:
    print("you got 2 nd class")'''
'''
#example for security
adhar=str(input("enter y or n:"))
if adhar=='y' or adhar=='Y' :
    print("ok")
    voter_id=input("voter enter y or n:")
    if voter_id=="y"or voter_id=="Y":
        print("ok")
        vehical_licence=input("vehical enter y or n:")
        if voter_id=="y" or vehical_licence=="Y":
            print("you have allowed for program")
        else:
             print("please licence of documents ")
    else:
             print("please voter_id of documents ")
else:
             print("please adhar of documents ")   '''
'''
a=10
b=10

print("greater") if a > b else print("equal")  if a ==b else print("smaller")'''

'''
#remove int type data from list
l=['akash','rohan','rajat','nikhil',8,'pooja','shamali',8.56]
for i in l:
    if type(i) == int or type(i)==float:
       # del (l[l.index(i)])
        l.remove(l[l.index(i)])
print(l) '''

'''
l=['akash','rohan','akash','rajat','nikhil',8,'pooja','shamali',8.56]
s= []
n=[]
for i in l:
    if type(i) == str:
        s=l.count(l[l.index(i)])
        
    elif type(i) == int :
        n=l.pop(i)
        
    print(s)
    
print(n) '''

'''
# find index position of any word
l=['akash','rohan','akash','rajat','nikhil',8,'pooja','shamali',8.56]
s= 'akash'
i=0
m=[ ]
length = len(l)
while i < length :
    if s == l[i]:
        m.append(i)
    i+=1
print(f'{s} is present in {l} at indexse{m}')   

list=['akash','rohan','akash','rajat','nikhil',8,'pooja','shamali',8.56]

s = 'akash'
i=0
m=[]
while i < len(list):
    if s == list[i]:
        m.append(s)
    i+=1
print(m) '''
#remove spaces from string
s='  Hello  World   From Pankaj \t\n\r\tHi There  '
#print(s)
print(s.replace(" ",''))

'''
weight=int(input('enter weight:'))
height=int(input('enter height:'))
x = weight/height*height
if x < 18.5:
    print("under weight")
elif 18.5 <x <25:
    print("normal weight")
elif 30<=x:
    print("obesity") '''

'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3=[i + j for i,j in zip(list1,list2)]
print(list3) '''
numbers = [1, 2, 3, 4, 5, 6, 7]
result = []
for i in numbers:
    result.append(i*i)
print(result)

















