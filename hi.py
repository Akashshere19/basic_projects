'''import name
name.greet("akash") '''
'''
# Write a program to
#find out the largest and smallest word in the string "This is an umbrella".
a=('thisisare is s umbrella')
a=a.split()
maxx= a
max_len = len(a)
for i in a:
    if len(i) < max_len:
        max_len = len(i)
        maxx = i
print(maxx)  '''

'''
# Write a program to check if a given string is a Palindrome.
#A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc.

a=['121','aba','caac','akashhsaka','mom','akash']
j=0
for i in a:
    
    print(i[:],j)
    (i[::-1],j)
    
    print(i ==i[::-1],'yes its palindrome')
    j+=1

        '''
'''
# Write down the names of 10 of your friends in a
#list and then sort those in alphabetically ascending order.

name =['akash','sham','ram','ganesh','rahul','oppo','bala','xray']
name.sort()
print(name)'''

'''
#Write a program to make a new string with the word "the" deleted in
#the sentence "This is the lion in the cage".

s=("This is the lion in the cage The ")
s = s.split()
for i in s:
    if i == 'the' or i=='The':
        del(s[s.index(i)])
print(s)
print(' '.join(s)) '''
        


s=("This is the lion in the cage The ")
#for i in s:
if s == s.lower():
        print(s.capitalize())










