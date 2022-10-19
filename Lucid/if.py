#write a prog to print if given numb is even num
'''n= int(input('enter a no:'))
r=n%2
if r ==0:
    print(n,'is even no')'''

# write a program to print if given number is bigger than 10
'''
no1=int(input('enter a no:'))
print('i am berfore the if statement')
if no1>=10:
    print('hi i am in if statement')
    print(no1,'is bigger than 10')
    print('end of if statement')
print('****after if statement*****')'''

# write a program to print given number is positive number
'''
n= int(input('enter a no:'))
if n >0:
    print(n,'is positive number')'''
# write a program to print given number is positive number or Negitive number

'''no1=int(input('enter a no:'))
if no1>=0:
    print(no1,'is positive')
else:
    print(no1,'is NOT POSITIVE number')'''
    
# write a program to print given number is even number or odd number
'''n= int(input('enter a no:'))
if n%2==0:
    print(n,'is even')
else:
    print(n,'is no is odd')'''
# write a program to print given number is bigger than 10 or not bigger than 10
'''no1=int(input('enter a no:'))
print('I am before the if statement')
if no1>10:
    print('Hi i am in if loop')
    print(no1,'is bigger than 10')
    print('end of if block')

else:
    print('Hi i am in else block')
    print(no1,'is NOT BIGGER than 10')
    print('end of else block')
print('******')
print('i am not in if block')

print('the end')'''
# write a program to print biggest number in given 2 numbers
'''
no1 = int(input('enter First number:'))
no2 = int(input('enter Second number:'))
if no1> no2:
    print(no1,'no1 is bigger number')
else:
    print(no2,'no2 is bigger number')'''

# write a program to print given number is bigger than 10 or smaller than 10 or equal to 10
'''
no1=int(input('enter a number:'))
print('I am before the if statement')
if no1>10:
    print('hi i am in if statement')
    print(no1,'is bigger than 10')
    print('end of the if block')
elif no1<10:
    print('hi i am in elif block')
    print(no1,'is smaller than 10')
    print('end of elif block')
else:
    print('hi i am in else block')
    print(no1,'is equal to 10')
    print('end of else block')
print('*********')
print('i am outside of all block')'''

# write a program to print given number is positive number or Negitive number or zero
'''no1 =int(input('enter a no:'))
if no1 <0:
    print(no1,'this no is negative')

elif no1 >0:
    print(no1,'this no is positive')
else:
    print(no1,'this no is equal to zero')'''


# find biggest no
'''
no1=int(input('enter a first no:'))
no2=int(input('enter a second no:'))
no3=int(input('enter a third no:'))
if no1 >no2 and no1>no3:
    print(no1,'is biggest no')
elif no2 >no1 and no2 > no3:
    print(no2,'is biggest no')
else:
    print(no3,'is biggest no')'''

'''
no1=int(input('enter a first no:'))
no2=int(input('enter a second no:'))
no3=int(input('enter a third no:'))
no4=int(input('enter a fourth no:'))

if no1> no2 and no1>no3 and no1> no4:
    print(no1,'is biggest no')
    
elif no2 > no3 and no2 > no3 and no2 > no4:
    print(no2,'is biggest no')
elif no3 > no4:
    print(no3,'is biggest no')
else:
    print(no4,'is biggest no')'''

# write a program to accept weekday number [1-7] as input and  display the weekday name
'''
wdno = int(input('enter a no:'))
if wdno==1:
    print('SUNDAY')
elif wdno==2:
    print('MONDAY')
elif wdno==3:
    print('THUESDAY')
elif wdno == 4:
    print('WEDNESDAY')
elif wdno==5:
    print('THURSDAY')
elif wdno == 6:
    print('FRIDAY')
elif wdno == 7:
    print('SATURDAY')
else:
    print('INVALID INPUT')'''
# write week no and its day.
'''
wdno = int(input(" Enter weekday number [1 to 7] : "))
if wdno==1:
    print("SUNDAY")
else:
    if wdno == 2:
        print("MONDAY")
    else:
        if wdno == 3:
            print("TUESDAY")
        else:
            if wdno == 4:
                print("WEDNESDAY")
            else:
                if wdno == 5:
                    print("THURSDAY")
                else:
                    if wdno == 6:
                        print("FRIDAY")
                    else:
                        if wdno == 7:
                            print("SATURDAY")
                        else:
                            print("INVALID INPUT")
print("THE END")'''

# write a program to take runtime input month number in between 1 to 12  print the month name
'''
no=int(input('enter a no in between 1 to 12:'))
if no == 1:
    print('JANUARY')
elif no==2:
    print('FEBRUARY')

elif no==3:
    print('MARCH')
elif no==4:
    print('APRIL')
elif no==5:
    print('MAY')
elif no==6:
    print('JUNE')
elif no==7:
    print('JULY')
elif no==8:
    print('AUGUST')
elif no==9:
    print('SEPTEMBER')       
elif no==10:
    print('OCTOMBER')
elif no==11:
    print('NOVEMBER')
elif no==12:
    print('DECEMBER') '''   

'''
no=int(input('enter a no in between 1 to 12:'))

if no == 1:
    print('JANUARY')
else:
    if no==2:
        print('FEBRUARY')
    else:
        if no==3:
            print('MARCH')
        else:       
            if no==4:
                print('APRIL')
            else:    
                if no==5:
                    print('MAY')
                else:    
                    if no==6:
                        print('JUNE')
                    else:    
                        if no==7:
                             print('JULY')
                        else:
                            if no==8:
                                print('AUGUST')
                            else:    
                                if no==9:
                                     print('SEPTEMBER')
                                else:
                                    
                                    if no==10:
                                            print('OCTOMBER')
                                    else:
                                        if no==11:
                                                print('NOVEMBER')
                                        else:
                                            
                                            if no==12:
                                                print('DECEMBER')


print('the end')
'''

no1 = int(input(" Enter First Number :"))
no2 = int(input(" Enter Second  Number :"))
no3 = int(input(" Enter Third Number :"))

if no1== no2 and no1 == no3 :
    print(" the three number are same values ")
else :
    if no1 > no2 and no1 > no3 :
        print(no1 , " n1 is biggest")
    elif no2>no3 :
        print(no2 , " n2 is biggest ")
    else :
        print(no3, " n3 is biggest ")


"""
if no1!= no2 or no1 != no3 or  no2!=no3:
    if no1 > no2 and no1 > no3 :
        print(no1 , " n1 is biggest")
    elif no2>no3 :
        print(no2 , " n2 is biggest ")
    else :
        print(no3, " n3 is biggest ")
else :
    print(" the three number are same values ")

"""






    
