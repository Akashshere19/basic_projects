'''
power = 3
if power == 1:
    print("yes its ON")
elif power == 0:
    print("please check it")
    if power == 0:
        print("plug it")
    elif power == 1:
        print("please check")
        if power ==0:
            print("turn On")
        elif power  ==1:
            print("fuse ok ?")
            if power ==0:
                print("check fuse")
            elif power== 0:
                print("check fuse")
else:
    print("its ON")'''
'''
# Ask user to give two float input for length and breadth of a rectangle and print area type casted to int.
x=int(input('enter heigth of rectangular:'))
y=int(input('enter breadth of rectangular:'))
        
print("answer is:",x*y) 


length = float(input("please enter length:"))

breadth =float(input("please enter breadth:"))

print(int(float(length)*float(breadth))) '''

'''
#Take side of a square from user and print area and perimeter of it.
print('enter side value:')
side=int(input())
print('area is',side*side)
print('perimeter is :',4*side)


#Take name, roll number and field of interest from user and print in the below format :
#Hey, my name is xyz and my roll number is xyz. My field of interest is xyz

name= str(input("enter your name:"))
Roll_no = int(input("eneter your roll_no:"))
field_interest = str(input("enter your interest field:"))
print('my name is',name,'my roll no is',Roll_no,'and my interest in that',field_interest)



'''
'''
s=input('enter a string:')
length = len(s)
print(*s,sep=' | ')
print('='*(length*4))
print(*range(-len(s),0,1))
'''
'''
print('decision programming')
name = input('enter your name:')
question= input(f'hello {name},will you come for party').lower()
neg = ['no','n','nah','never','not']
pos =['yes','y','yeah','yup','yahoo']
while question == neg and pos:
    print('please be enter certain:')
    question =input(f'hello{name},will you come at party').lower()
else:
    if question in neg:
        print('ok it will manage..')
    elif question in pos:
        print('yes i know that') '''


'''
n=11
for i in range(1,n):
    for j in range(1,i):
        print('*',end=' ')
    
    print('')
for i in range(5):
        print('|') '''




'''

import random


def generate_code():
    """
    Generate a 3 unique digit number
    """
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    solution = digits[:3]
    print(solution)
    return solution


def get_user_guess():
    """
    Get user guess
    """
    return list(input("What is your guess?\n"))


def check_user_guess(user_guess, game_code):
    """
    Check if the user guess is correct or get the clues if not
    """
    if user_guess == game_code:
        return "Game Won"

    results = []
    for index, number in enumerate(user_guess):
        if number == game_code[index]:
            results.append("Match")
        elif number in game_code:
            results.append("Close")
    if results == []:
        return ["Nope"]
    else:
        return results


print("Game Starts!")
code = generate_code()
result = []

while result != "Game Won":

    user_guess = get_user_guess()
    result = check_user_guess(user_guess, code)

    print("Here is the result of your guess:")
    if result == "Game Won":
        print("Game Won!!")
    else:
        for clue in result:
            print(clue)

'''
p=("Grab everything UP TO index 3")
print(p[:-1:-1])
my_list = ['one','two','three',4,5]
print(my_list[:-3])
print(my_list[-3:-2])
print(my_list[-3:])
print(my_list[2:-2])
print(my_list[-1:1:-1])
'''
ls_1= [1,5,'akash']
ls_2 = [4,7.0,'hello']
ls_3 = [2,9,2.5]

my_listt=[ls_1,ls_2,ls_3]
print(my_listt)

list_comprehensive = [row[0] for row in my_listt]
print(list_comprehensive)

'''
'''
l1=[2,3,4]
l2=[1,2,3]
l3=[3,7,8]
list=[no[2] for no in l1]
print(list)
list2 = [no[0] for no in (l2)]
print(list2)
list3 = [no[2] for no in(l3)]
print(list3)'''

'''
l=[2,7,5,0]
p=([i[0] for i in l])
print(p)'''

'''
h=2,
for i in h:
    print(i)'''



def f():
    pass
a=f()
b=f()
print(a==b)
print(a)
'''
class f:
    pass
a=f()
b=f()
print(a==b)'''




x=9
y=8
z=7
c=x,y,z
print(c)
for i in c:
    a=i
    #i+=1
    d=i
    #i+=1
    g=i
print(a,d,g)    














