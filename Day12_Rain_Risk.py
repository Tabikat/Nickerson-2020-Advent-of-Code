import os
file=open('Day12.txt').read()
navigation=file.split('\n')

#Part 1
hori=0 #track horizontal movement
vert=0 #tracks vertical movement
dir=0 #tracks degrees of rotation, where East=0
for i in navigation:
    #N&S change vertical location, E&W change horizontal location
    if i[0]=='N':
        vert+=int(i[1:])
    if i[0]=='E':
        hori+=int(i[1:])
    if i[0]=='S':
        vert-=int(i[1:])
    if i[0]=='W':
        hori-=int(i[1:])
    #L adds degrees, once over 360 degrees, subtract one whole rotation
    if i[0]=='L':
        dir+=int(i[1:])
        if dir>=360:
            dir-=360
    #R subtracts degrees, once under 0 degrees, add one whole rotation
    if i[0]=='R':
        dir-=int(i[1:])
        if dir<0:
            dir+=360
    #R F continues in the direction it is facing
    if i[0]=='F':
        if dir==0:
            hori+=int(i[1:])
        if dir==90:
            vert+=int(i[1:])
        if dir==180:
            hori-=int(i[1:])
        if dir==270:
            vert-=int(i[1:])
print('Manhattan Distance:', abs(hori)+abs(vert))


#Part 2
hori=0 #track horizontal movement
vert=0 #tracks vertical movement
waypt_hori=10 #waypoint horizontal location
waypt_vert=1 #waypoint vertical location
for i in navigation:
    #N&S change vertical location of waypoint, E&W change horizontal location
    if i[0]=='N':
        waypt_vert+=int(i[1:])
    if i[0]=='E':
        waypt_hori+=int(i[1:])
    if i[0]=='S':
        waypt_vert-=int(i[1:])
    if i[0]=='W':
        waypt_hori-=int(i[1:])
    #L rotates points around ship counterclockwise
    if i[0]=='L':
        rotations=int(int(i[1:])/90)
        wh=waypt_hori
        wv=waypt_vert
        #1 rotation represents 90 degrees
        if rotations==1:
            waypt_hori=wv
            waypt_vert=wh
            waypt_hori=-waypt_hori
        #2 rotations represents 180 degrees
        if rotations==2:
            waypt_hori=-waypt_hori
            waypt_vert=-waypt_vert
        #3 rotations represents 270 degrees
        if rotations==3:
            waypt_hori=wv
            waypt_vert=wh
            waypt_vert=-waypt_vert
    #R rotates points around ship clockwise
    if i[0]=='R':
        dir-=int(i[1:])
        if dir<0:
            dir+=360
        rotations=int(int(i[1:])/90)
        wh=waypt_hori
        wv=waypt_vert
        #1 rotation represents 90 degrees
        if rotations==1:
            waypt_hori=wv
            waypt_vert=wh
            waypt_vert=-waypt_vert
        #2 rotations represents 180 degrees
        if rotations==2:
            waypt_hori=-waypt_hori
            waypt_vert=-waypt_vert
        #3 rotations represents 270 degrees
        if rotations==3:
            waypt_hori=wv
            waypt_vert=wh
            waypt_hori=-waypt_hori
    if i[0]=='F':
        hori+=waypt_hori*int(i[1:])
        vert+=waypt_vert*int(i[1:])
        #Moves ship to the waypoint number of times indicated
print('Manhattan Distance with Waypoint:', abs(hori)+abs(vert))
