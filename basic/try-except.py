'''try:
    age=int(input('enter your age'))
    print('your age is :',age)
    if age < 0:
        raise ValueError
    yearOfBirth=2021 - age
    print('your year of birth is:',yearOfBirth)
except ValueError:
    print('Input coorect age.') '''
'''
try:
    age ='aa'
    print(age)
    assert age >0
    yearOfBirth =2021 - age
    print(yearOfBirth)
except AssertionError:
    print('input correct age.')
except ValueError:
    print('value error')
except NameError:
    print('nameerror')
except:
    print('some other error')'''
arr =[1729,2234]
doller =0
try:
    doller =arr[1]
except IndexError:
    print('A')
except:
    print('B')
finally:
    print('c')

doller =23
try:
    doller = doller/0
except ZeroDivisionError:
    print('d')
finally:
    print('e')















