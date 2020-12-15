import os
file=open('Day14.txt').read()
initialization=file.split('mask = ')
initialization.remove('')

for i in range(len(initialization)):
    initialization[i]=initialization[i].replace('\n',' ')
    initialization[i]=initialization[i].replace(' mem[',' ')
    initialization[i]=initialization[i].replace('] = ',' ')
    initialization[i]=initialization[i].split(' ')
print(initialization)

program={}
for i in initialization:
    program[i][0]=program[i][1:]

print(program)
