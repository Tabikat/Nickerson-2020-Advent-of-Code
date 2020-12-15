import os
import math
file=open('Day13.txt').read()
file=file.split('\n') #list of 2 objects, time and bus_IDS
time=int(file[0]) #earliest timestamp I can leave
bus_IDs=file[1].split(',') #splits into a list as separated by commas

#Part 1
#makes a list of the bus IDs and their indices
for i in range(len(bus_IDs)):
    bus_IDs[i]=[bus_IDs[i],i]

i=0
while i!=len(bus_IDs):
    if bus_IDs[i][0]=='x': #deletes the 'x' terms
        del bus_IDs[i]
    else:
        bus_IDs[i][0]=int(bus_IDs[i][0]) #converts the str to int
        i+=1

#makes a list of when the next bus for each route will arrive
next_bus=[]
for bus in bus_IDs:
    next_bus.append(((time//bus[0])+1)*bus[0]) # // takes the floor function

print('Next Bus ID:', (min(next_bus)-time)*bus_IDs[next_bus.index(min(next_bus))][0])

#Part 2
bus_num=[] #list of bud IDs
bus_offset=[] #list of original indices to determine offsets
timestamp=[] #for tracking the potential timestamps t
for bus in bus_IDs: #creates the lists of bus IDs and offsets
    bus_num.append(bus[0])
    bus_offset.append(bus[1])

def lcm(x,y): #function to calculate the least common multiple
    return abs(x*y)//math.gcd(x,y)

#calculates the first two possible numbers for the earliest timestamps
for n in range(100000000000000//bus_num[0]*bus_num[0],10000000000000000,bus_num[0]):
    if (n+bus_offset[1])%bus_num[1]==0:
        timestamp.append(n)
        timestamp.append(n+bus_offset[1])
        break

addend=lcm(bus_num[0],bus_num[1])
for i in range(2,len(bus_num)): #We are only looking for the 2+ timestamps
    while len(timestamp)<=len(bus_num): #continues until lengths of t==bus_num
        if (timestamp[0]+bus_offset[i])%bus_num[i]==0: #finds potential next
            addend=lcm(addend,bus_num[i]) #finding the next lcm skips more #s
            timestamp.append(timestamp[0]+bus_offset[i])
            break
        else: #if the timestamp didn't work, add the addend to find next potentials
            for t in range(len(timestamp)):
                timestamp[t]+=addend

print('Earliest Timestamp:', timestamp)
