import os
file=open('Day3.txt').read()
geology=file.split('\n')

#make a list of lists
for i in range(0,len(geology)):
    geology[i]=list(geology[i])

slopes=['R1D1','R3D1','R5D1','R7D1','R1D2']
trees={}
#dict of slopes
for i in range(0,len(slopes)):
    #(R_value, D_value, x_value, tree_count)
    trees[slopes[i]]=[int(list(slopes[i])[1]),int(list(slopes[i])[3]),0,0]

for i in range(0,len(geology)):
    for slope in slopes:
        if trees[slope][1]!=1:
            if (i%trees[slope][1])!=0: #checks if line count is divisible by D
                continue
        if geology[i][trees[slope][2]]=='#': #checks for trees
            trees[slope][3]+=1
        trees[slope][2]+=trees[slope][0] #moves the x_value R
        #shifts the count as the pattern repeats
        if trees[slope][2]>=len(geology[i]):
            trees[slope][2]-=len(geology[i])

print('Trees on Slope -1:',trees['R1D1'][3])
print('Trees on Slope -1/3:',trees['R3D1'][3])
print('Trees on Slope -1/5:', trees['R5D1'][3])
print('Trees on Slope -1/7:',trees['R7D1'][3])
print('Trees on Slope -2:', trees['R1D2'][3])

product=1
for slope in slopes:
    product*=trees[slope][3]
print(product)
