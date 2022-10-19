import getpass
import string
import os

users=['user','user2','user3']
#users=input('enter a  name:')
pins=['1234','2222','3333']
amounts=[1000,2000,3000]
count=0
while True:
    user = input('\nEnter user Name:')
    user=user.lower()
    if user in users:
        if user == users[0]:
            n=0
        elif user == users[1]:
            n=1
        else:
            n=2
        break
    else:
        print('--------')
        print('********')
        print('INVALID USERNAME')
        print('********')
        print('---------')

while count <3:
    print('--------')
    print('********')
    pin= str(getpass.getpass('PLEASE ENTER PIN:'))
    print('********')
    print('--------')
    if pin.isdigit():
        if user == 'user1':
            if pin ==pins[0]:
                break
            else:
                count +=1
                print('--------')
                print('********')
                print('INVALID PIN')
                print('********')
                print('---------')
        if user == 'user2':
            if pin ==pins[1]:
                break
            else:
                count +=1
                print('--------')
                print('********')
                print('INVALID PIN')
                print('********')
                print('---------')
        if user == 'user3':
            if pin ==pins[2]:
                break
            else:
                count +=1
                print('--------')
                print('********')
                print('INVALID PIN')
                print('********')
                print('---------')
    else:
        print('--------')
        print('********')
        print('PIN CONSISTS OF 4 DIGITS')
        print('********')
        print('--------')
        count+=1
if count ==3:
        print('--------')
        print('********')
        print('3 UNSUCCESFUL PIN ATTEMPTS,EXITING')
        print('!!!YOUR CARD HAS BEEN LOCKED !!!')
        print('********')
        print('--------')
        exit()
        
print('--------')
print('********')
print('LOGING SUCCESFUL,CONTINUE')
print('********')
print('---------')
print('********')
print()
print('********')
print('---------')
print(str.capitalize(users[n]),'WELCOME to ATM')
print('*********')
print('----ATM SYSTEM----')

while True:
    print('---------')
    print('*********')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nSTATEMENT__(S) \nWithdraw__(L) \nchange PIN_(P) \nquit____(Q) \n: ').lower()
    print('*********')
    print('---------')
    valid_responses =['s','w','l','p','q']
    response =response.lower()
    if response =='s':
       print('---------')
       print('*********')
       print(str.capitalize(users[n]),'YOU HAVE ', amounts[n],'rupees on your Account.')
       print('*********')
       print('---------')
    elif response =='w':
       print('---------')
       print('*********')
       cash_out=int(input('ENTER AMOUNTYOU WOULD LIKE TO WITHDRAW'))
       print('*********')
       print('---------')
       if cash_out % 10 !=0:
            print('--------')
            print('********')
            print('AMOUNT TO YOU WANT WIDHDRAW MUST TO MATCH 1000 RUPEES')
            print('********')
            print('---------')        
       elif cash_out > amounts[n]:
            print('--------')
            print('********')
            print('YOU HAVE INSUFFICENT AMOUNT')
            print('********')
            print('---------') 
       else:
           amounts[n]=amounts[n] - cash_out
           print('--------')
           print('********')
           print('YOU HAVE INSUFFICENT AMOUNT')
           print('********')
           print('---------') 
    elif response =='l':
           print()
           print('---------')
           print('*********')
           cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE : '))
           print('*********')
           print('---------')
           print()
           if cash_in % 10 !=0:
               print('--------')
               print('********')
               print('AMOUNT TO YOU WANT WIDHDRAW MUST TO MATCH 1000 RUPEES')
               print('********')
               print('--------')
           else:
               amounts[n] = amounts[n] + cash_in
               print('--------')
               print('********')
               print('NEW BALANCE IS :',amounts[n],'Rupees')
               print('********')
               print('--------')
    elif response =='p':
           print()
           print('---------')
           print('*********')
           new_pin = str(getpass.getpass('ENTER A NEW PIN : '))
           print('*********')
           print('---------')
           
           if new_pin.isdigit() and new_pin !=pin[n] and len(new_pin == 4):
               print('--------')
               print('********')
               new_pin = str(getpass.getpass('CONFIRM NEW PIN: '))
               print('********')
               print('--------')
               if new_pin !=new_pin:
                   print('--------')
                   print('********')
                   print('PIN MISMATCH')
                   print('********')
                   print('--------')
               else:
                   pins[n]=new_pin
                   print('NEW PIN SAVED')     
           else:
               print('--------')
               print('********')
               print('NEW PIN MUST BE 4 DIGITS \nAND MUST BE  DIFFERENT TO PREVIOUS PIN')
               print('********')
               print('--------')        
    elif response == 'q':
        exit()
    else:
        print('--------')
        print('********')
        print('RESPONSE NOT VALID')
        print('********')
        print('--------')
