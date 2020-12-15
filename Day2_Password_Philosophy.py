import os
file=open('Day2.txt').read()
file=file.split('\n')

#makes list of lists
for i in range(len(file)):
    file[i]=file[i].split()

sled=0 #tracks each valid sled password
toboggan=0 #tracks each valid toboggan password
for i in range(len(file)): #
    #min and max is the numbers on either side of -
    min,max=file[i][0].split('-')
    min,max=int(min),int(max)
    policy=str(file[i][1].strip(':')) #determines the character for policy
    pw=list(file[i][2])
    #calculates sled passwords, counts num. of characters in pw
    count=pw.count(policy)
    if count in range(min,max+1): #add 1 because the range does not include the ceiling
        sled+=1
    #calculates toboggan passwords, checks for characters in places
    if pw[min-1] is policy:
        if pw[max-1] is not policy:
            toboggan+=1
    if pw[max-1] is policy:
        if pw[min-1] is not policy:
            toboggan+=1
print('Number of Valid Sled Passwords:',sled)
print('Number of Valid Toboggan Passwords:', toboggan)
