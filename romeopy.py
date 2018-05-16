import string

fname=input('enter file name:')
try:
    fhand=open(fname,mode='r')
except:
    print('file dosent exist')
    exit()

d=dict()
for line in fhand:
    line=line.rstrip()
    line=line.translate(line.maketrans('','',string.punctuation))
    line=line.lower()
    print(line)
    words=line.split()
    for word in words:
        d[word]=d.get(word,0)+1


print(d)
