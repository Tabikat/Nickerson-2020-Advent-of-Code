import os
import math
file=open('Day10.txt').read()
output_joltages=file.split('\n')

for i in range(len(output_joltages)):
    output_joltages[i]=int(output_joltages[i])
output_joltages.append(0) #adds the outlet joltage of 0
builtin_joltage=max(output_joltages)+3
output_joltages.append(builtin_joltage) #adds phone's joltage
output_joltages.sort()
print(output_joltages)
outlet_joltage=0
one_jolt=0
two_jolt=0
three_jolt=0
removable_num=[]
for i in range (1,len(output_joltages)):
    if output_joltages[i]-output_joltages[i-1]==1:
        one_jolt+=1
        if i>=2:
            if output_joltages[i]-output_joltages[i-1]==3:
                removable_num.append(output_joltages[i-2])
            if output_joltages[i]-output_joltages[i-2]==2:
                removable_num.append(output_joltages[i-1])
    if output_joltages[i]-output_joltages[i-1]==2:
        two_jolt+=1
        if i>=3:
            if output_joltages[i]-output_joltages[i-1]==3:
                removable_num.append(output_joltages[i-2])
    if output_joltages[i]-output_joltages[i-1]==3:
        three_jolt+=1
print(removable_num)

only_remove_one=0
for i in range(2,len(removable_num)):
    if removable_num[i]-removable_num[i-2]==2:
        only_remove_one+=1

possible_comb=2**len(removable_num)
print(possible_comb)
distinct=possible_comb
for r in range(only_remove_one):
    print('choose',r)
    print('n!=',math.factorial(len(removable_num)))
    print('n-r!=',math.factorial(len(removable_num)-r))
    print('r!=',math.factorial(r))
    print('n choose r',math.factorial(len(removable_num))/(math.factorial(len(removable_num)-r)*math.factorial(r)))
    distinct-=math.factorial(len(removable_num))/(math.factorial(len(removable_num)-r)*math.factorial(r))

print('Joltage Distribution:', one_jolt*three_jolt)
print('Distinct Connections', distinct+1)
