#Student marksheet
'''stdno=int(input('Enter student no:'))
stdname=input('Enter Student name:')
mrs1=int(input('Enter mark of sub1:'))   
mrs2=int(input('Enter mark of sub2:'))
mrs3=int(input('Enter mark of sub3:'))
mrs4=int(input('Enter mark of sub4:'))
mrs5=int(input('Enter mark of sub5:'))
mrs6=int(input('Enter mark of sub6:'))
    
total=mrs1+mrs2+mrs3+mrs4+mrs5+mrs6
avgm=total/6

if mrs1<35 or mrs2 <35 or mrs3 <35 or mrs4<35 or mrs5<35 or mrs6<35:
    print('Your Result Faild.!')

elif avgm >=60:
    print('you are pass with First division')
    if avgm >=75:
        print('You are pass with Distiction')
    elif avgm >=90:
        print('You are pass with Golden meddle')

print('Total mark of All Sub:',total)
print('Average mark of all sub is:',avgm)'''

'''
#Employee salary slip
empno=int(input('Enter a Id of Employ:'))
empname=input('Please Enter Employee Name:')
job  = input('Enter job of Employee:')
sal = int(input('Enter Salary of Employee:'))
#hra=input('Enter HRA of Employee:')
#da=int(input('Enter DA for Employee:'))
#ta=int(input('Enter TA for Employee:'))
if job =='cleark' or 'Cleark':
    hra=sal*(35/100)
    da=sal*(28/100)
    ta=sal*(22/100)
elif job=='junior Engineer' or 'Junior Engineer':
    hra=sal*(38/100)
    da=sal*(30/100)
    ta=sal*(24/100)
elif job=='senior Engineer' or 'Senior Engineer':
    hra=sal*(40/100)
    da=sal*(32/100)
    ta=sal*(25/100)
elif job=='manager' or 'Manager':
    hra=sal*(43/100)
    da=sal*(35/100)
    ta=sal*(28/100)
    
if  sal <20000:
    it=sal*(30/100)
if 20000< sal >=35000:
    it=sal*(35/100)
if 30000< sal >=50000:
    it=sal*(40/100)
if 50000 < sal:
    it=sal*(45/100)

print('Id of Employ:',empno)
print('Employee Name:',empname)
print('Employee Job:',job)
print('Salary of Employee:',sal)
print('HRA of Employee:',hra)
print('DA for Employee:',da)
print('TA for  Employee:',ta)
print('IT for employee:',it)'''

'''
pmt=float(input('Enter loan amount:'))
lt=(input('Enter loan Type:'))
t=int(input('Enter no of months:'))

if lt=='Agriculture':
    r=7.5
elif lt =='Home':
    r=12
    
elif lt=='Personal':
    r=15
else:
    pass
   
si=pmt*r*t/100
tpmt=pmt+si
print('your rate of interest is:',r) #if enter diff loan type then will give error for r
print('Interest amount is:',si)
print('total payable amount:',tpmt)'''


unit=int(input('Enter unit for electricity:'))
GST=5
if unit<75:
    if 0<unit<50:
        BillAmount=10*1.45*GST
    elif 51<unit<75:
        BillAmount=10*2.60*GST
          
elif unit <225:
            if 0<unit<100:
                BillAmount=10*2.60*GST
            elif 101<unit<200:
                BillAmount=10*3.60*GST
            elif 201<unit<225:
                BillAmount=10*6.90*GST
                
elif unit >225:
            if 0<unit<50:
                    BillAmount=10*2.65*GST
            elif 51<unit<100:
                    BillAmount=10*3.35*GST
            elif 101<unit<200:
                    BillAmount=10*5.40*GST
            elif 201<unit<300:
                    BillAmount=10*7.10*GST
            elif 301<=unit<400:
                    BillAmount=10*7.90*GST
            elif 401<=unit<=500:
                    BillAmount=10*8.50*GST
            elif unit>500:
                    BillAmount=10*9.95*GST
                    
print('Your Bill Amount is:',BillAmount)                   
 
  

                

    
