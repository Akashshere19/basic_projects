'''pmt=float(input('Enter principle amount:'))
ri=float(input('Enter rate of interest:'))
nm=int(input('Enter no of months:'))
si=pmt*ri*nm/100
tpmt=pmt+si
print('Interest amount is:',si)
print('total payable amount:',tpmt)'''

'''
stdno=int(input('Enter student no:'))
stdname=input('Enter Student name:')
mrs1=int(input('Enter mark of sub1:'))
if mrs1 >100:
    print('please enter valid mark:')
    
mrs2=int(input('Enter mark of sub2:'))
mrs3=int(input('Enter mark of sub3:'))
mrs4=int(input('Enter mark of sub4:'))
mrs5=int(input('Enter mark of sub5:'))
mrs6=int(input('Enter mark of sub6:'))
total=mrs1+mrs2+mrs3+mrs4+mrs5+mrs6
avgm=total/6
print('total mark of sub1:',mrs1)
print('total mark of sub2:',mrs2)
print('total mark of sub3:',mrs3)
print('total mark of sub4:',mrs4)
print('total mark of sub5:',mrs5)
print('total mark of sub6:',mrs6)
print('Total mark of All Sub:',total)
print('Average mark of all sub is:',avgm)'''

'''
#
empno=int(input('enter a no:'))
empname=input('enter name:')
job=input('enter a job of employee:')
sal=int(input('enter a salary of employee:'))
hra=sal*(35/100)
da=sal*(28/100)
ta=sal*(22/100)
pf=sal*(12/100)
it=sal*(30/100)
grssal=sal+hra+ta+da
netsal=grssal-(pf+it)
print('Employ of Name:',empname)
print('Employ No:',empno)
print('job of Employee:',job)
print('Salary of Employee:',sal)
print('HRA of Employee:',hra)
print('DA of Employee:',da)
print('TA of Employee:',ta)
print('PF of Employee:',pf)
print('IT for Employee:',it)
print('Gross salary of Employee:',grssal)
print('Net salary of Employee:',netsal)'''

'''
#Student marksheet
stdno=int(input('Enter student no:'))
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
print('total mark of sub1:',mrs1)
print('total mark of sub2:',mrs2)
print('total mark of sub3:',mrs3)
print('total mark of sub4:',mrs4)
print('total mark of sub5:',mrs5)
print('total mark of sub6:',mrs6)
print('Total mark of All Sub:',total)
print('Average mark of all sub is:',avgm)'''
























