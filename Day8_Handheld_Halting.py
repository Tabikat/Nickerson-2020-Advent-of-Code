import os
import string
file=open('Day8.txt').read()
boot_code=file.split('\n')

#Part 1
accumulator=0
i=0
while 'x' not in boot_code[i]:
    if boot_code[i][0:3]=='acc':
        accumulator+=int(boot_code[i][4:])
        boot_code[i]=boot_code[i]+'x'
        i+=1
    if boot_code[i][0:3]=='jmp':
        i+=int(boot_code[i][4:])
    if boot_code[i][0:3]=='nop':
        i+=1
print('Accumulator Before Loop:',accumulator)

#Part 2
def terminate_loop(start_code):
    accumulator=0
    i=0
    while 'x' not in start_code[i]:
        if start_code[i][0:3]=='acc':
            if 'x' in start_code[i]:
                return 'Infinite Loop'
            accumulator+=int(start_code[i][4:])
            start_code[i]=start_code[i]+'x'
            i+=1
            if i==len(start_code):
                return accumulator
        if start_code[i][0:3]=='jmp':
            if 'x' in start_code[i]:
                return 'Infinite Loop'
            if int(start_code[i][4:])==0:
                return 'Infinite Loop'
            new_i=int(start_code[i][4:])
            start_code[i]=start_code[i]+'x'
            i+=new_i
            if i==len(start_code):
                return accumulator
        if start_code[i][0:3]=='nop':
            if 'x' in start_code[i]:
                return 'Infinite Loop'
            start_code[i]=start_code[i]+'x'
            i+=1
            if i==len(start_code):
                return accumulator
    return 'Infinite Loop'

boot_code=file.split('\n')
for i in range(0,len(boot_code)):
    if boot_code[i][0:3]=='nop':
        boot_code[i]=boot_code[i].replace('nop','jmp')
        print('Accumulator:',terminate_loop(boot_code))
        if terminate_loop(boot_code)=='Infinite Loop':
            boot_code=file.split('\n')
            continue
    #    elif (type(terminate_loop(boot_code)))==int:
    #        print('Accumulator:',terminate_loop(boot_code))
    if boot_code[i][0:3]=='jmp':
        boot_code[i]=boot_code[i].replace('jmp','nop')
        print('Accumulator:',terminate_loop(boot_code))
        if terminate_loop(boot_code)=='Infinite Loop':
            boot_code=file.split('\n')
            continue
    #    else:
    #        print('Accumulator:',terminate_loop(boot_code))
