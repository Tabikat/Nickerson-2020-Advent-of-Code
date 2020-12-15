import os
file=open('Day5.txt').read()
boarding_passes=file.split('\n')

#determines the dimensions of the plane based on the boarding passes input
FB=0
RL=0
plane_dim=list(boarding_passes[0])
for i in plane_dim:
    if i=='F':
        FB+=1
    elif i=='B':
        FB+=1
    elif i=='R':
        RL+=1
    elif i=='L':
        RL+=1
rows=2**FB #2^7 makes 128 rows
columns=2**RL #2^3 makes 8 columns

#calculates the ranges for the Front and Left sections
def lower_half(min,max):
    half=(max-min)/2
    if half==1:
        return min
    return (min,max-half)

#calculates the ranges for the Back and Right sections
def upper_half(min,max):
    half=(max-min)/2
    if half==1:
        return min+1
    return (min+half,max)

seatIDs=[]
for i in range(len(boarding_passes)):
    one_pass=list(boarding_passes[i]) #list of coordinates for one pass
    (min_row,max_row)=(0,rows)
    (min_col,max_col)=(0,columns)
    #determines the row of the seat
    for j in range(FB):
        if one_pass[j]=='F': #Front
            if max_row-min_row!=2:
                (min_row,max_row)=lower_half(min_row,max_row)
            else:
                seat_row=lower_half(min_row,max_row)
        if one_pass[j]=='B': #Back
            if max_row-min_row!=2:
                (min_row,max_row)=upper_half(min_row,max_row)
            else:
                seat_row=upper_half(min_row,max_row)
    #determines the column of the seat
    for j in range(FB,FB+RL):
        if one_pass[j]=='L': #Left
            if max_col-min_col!=2:
                (min_col,max_col)=lower_half(min_col,max_col)
            else:
                seat_col=lower_half(min_col,max_col)
        if one_pass[j]=='R': #Right
            if max_col-min_col!=2:
                (min_col,max_col)=upper_half(min_col,max_col)
            else:
                seat_col=upper_half(min_col,max_col)
    seatIDs.append(seat_row*8+seat_col)
print('Lowest Seat ID:', min(seatIDs))
print('Highest Seat ID:', max(seatIDs))
for seat in range(int(min(seatIDs)),int(max(seatIDs))):
    if seat not in seatIDs:
        print('My Seat:', seat)
