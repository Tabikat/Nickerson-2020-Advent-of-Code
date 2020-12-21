import os
file=open('Day11.txt').read()
seat_layout=file.split('\n') #list of strings
height=len(seat_layout)
width=len(seat_layout[0])
layout_string=''.join(seat_layout) #string

#builds a dictionary with the string index of a seat and the seats around it that need checking
neighboring_seats={}
for i in range(1,len(layout_string)-1):
    if layout_string[i]!='.':
        if i==width-1 or i==height*width-width: #top right and bottom left corners
            continue
        elif i in range(width): #top row
        #N represents non-seats
            neighboring_seats[i]=('N','N','N',i-1,i+1,i+width-1,i+width,i+width+1)
        elif i in range(height*width-width+1,height*width-1): #bottom row
            neighboring_seats[i]=(i-width-1,i-width,i-width+1,i-1,i+1,'N','N','N')
        elif i%width==0: #left column
            neighboring_seats[i]=('N',i-width,i-width+1,'N',i+1,'N',i+width,i+width+1)
        elif i%width==width-1: #right column
            neighboring_seats[i]=(i-width-1,i-width,'N',i-1,'N',i+width-1,i+width,'N')
        else:
            neighboring_seats[i]=(i-width-1,i-width,i-width+1,i-1,i+1,i+width-1,i+width,i+width+1)

#build a function to check seats
def seat_check(index, layout, seatIDs, occupied_to_empty_rule, recursion):
    count=0
    seats_to_check=seatIDs[index]
    if layout[index]=='#':
        for seat in seats_to_check:
            if seat=='N':
                continue
            if layout[seat]=='#':
                count+=1
        if recursion=='NO':
            if count>=occupied_to_empty_rule:
                return 'L'
            else:
                return '#'
    #    if recursion=='YES':
    #        continue
    if layout[index]=='L':
        for seat in seats_to_check:
            if seat=='N':
                continue
            if layout[seat]=='#':
                return 'L'
                break
        if recursion=='NO':
            return '#'
    #    if recursion=='YES':
    #        continue

#builds a second round to compare to layout1
def comparable_round(layout, seatIDs, occupied_to_empty_rule,recursion):
    new_layout='#'
    for i in range(1,len(layout)-1):
        if i==width-1 or i==height*width-width:
            new_layout+='#'
        elif layout[i]=='.':
            new_layout+='.'
        else:
            new_layout+=seat_check(i,layout,seatIDs,occupied_to_empty_rule,recursion)
    new_layout+='#'
    return new_layout

#To start, since every seat is empty, they will all become occupied
layout1=''
for seat in layout_string:
    if seat=='L':
        seat=seat.replace('L','#')
    layout1+=seat

layout2=comparable_round(layout1,neighboring_seats,4,'NO')

while layout1!=layout2:
    layout1=layout2
    layout2=comparable_round(layout1,neighboring_seats,4,'NO')

print('Part 1, Occupied Seats:',layout2.count('#'))
