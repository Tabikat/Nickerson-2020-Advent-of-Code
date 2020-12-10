import os
file=open('Day9.txt').read()
XMAS_data=file.split('\n')

#changes XMAS_data from a list of str to a list of int
for i in range(0,len(XMAS_data)):
    XMAS_data[i]=int(XMAS_data[i])

length_of_preamble=25
preamble_index=[i for i in range(0,length_of_preamble)] #lists no. of items in preamble
preamble=[XMAS_data[i] for i in preamble_index] #creates the preamble
for number in range(preamble_index[length_of_preamble-1]+1,len(XMAS_data)):
    #lists the 25 preamble numbers as identified by their indices in preamble_index
    num_of_sums=0 #track how many ways to make a sum using preamble
    for j in range(0,length_of_preamble):
        #looks for differences in numbers in the preamble, excluding itself
        if XMAS_data[number]-preamble[j] in preamble:
            if XMAS_data[number]-preamble[j]!=preamble[j]:
                num_of_sums+=1
    #checks if number was sum of preamble numbers
    if num_of_sums==0:
        weakness_key=XMAS_data[number]
        print('Weakness Key:', XMAS_data[number])
        break #To gather data about the remaining numbers, remove this break
    #adds 1 to the list of indexes for the preamble
    for i in range(0,len(preamble_index)):
        preamble_index[i]+=1
    preamble=[XMAS_data[i] for i in preamble_index] #recreates the preamble

#adds all numbers in data until equal to or larger than weakness key
for i in range(0,len(XMAS_data)):
    encryption_weakness=XMAS_data[i]
    for j in range(i+1,len(XMAS_data)):
        encryption_weakness+=XMAS_data[j]
        if encryption_weakness==weakness_key:
            print('Encryption Weakness:', min(XMAS_data[i:j])+max(XMAS_data[i:j]))
        elif encryption_weakness>weakness_key:
            break
