import re

hand=open('mbox-short.txt')
'''
for line in hand:
    line=line.rstrip()
    #x=re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z0-9]',line) for finding without < >
    #x=re.findall('^X-.*: ([0-9.]+)',line) finds X-kib=nes and extract number
    #x=re.findall('^Details:.*rev=[0-9]+',line) details line
    #x= re.findall('^From .* ([0-9][0-9]):', line)
    x=re.findall('.*rev=39742$',line)
    if len(x)>0:
        print(x)


s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst=re.findall('\S+@\S+',s)
print(lst)

Exercise 1: Write a simple program to simulate the operation of the grep command
on Unix. Ask the user to enter a regular expression and count the number
of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

p=input('enter your expression: ')
count=0
for line in hand:
    line=line.rstrip()
    if re.search(p,line):
        count+=1

print('mbox has {} lines that matched'.format(count),p)

'''
sumz=0
count=0
for line in hand:
    line=line.rstrip()
    x=re.findall('New Revision: ([0-9]+)',line)
    
    if len(x)>0:
        q=float(x[0])
        sumz+=q
        count+=1
        print(x,q)

print('%.3f' %(sumz/count))
        





































