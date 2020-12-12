import os
file=open('Day12.txt').read()
navigation=file.split('\n')

#Part 1
hori=0 #track horizontal movement
vert=0 #tracks vertical movement
dir=0
for i in navigation:
    if i[0]=='N':
        vert+=int(i[1:])
    if i[0]=='E':
        hori+=int(i[1:])
    if i[0]=='S':
        vert-=int(i[1:])
    if i[0]=='W':
        hori-=int(i[1:])
    if i[0]=='L':
        dir+=int(i[1:])
        if dir>=360:
            dir-=360
    if i[0]=='R':
        dir-=int(i[1:])
        if dir<0:
            dir+=360
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
    if i[0]=='N':
        waypt_vert+=int(i[1:])
        print((hori,vert),(waypt_hori,waypt_vert))
    if i[0]=='E':
        waypt_hori+=int(i[1:])
        print((hori,vert),(waypt_hori,waypt_vert))
    if i[0]=='S':
        waypt_vert-=int(i[1:])
        print((hori,vert),(waypt_hori,waypt_vert))
    if i[0]=='W':
        waypt_hori-=int(i[1:])
        print((hori,vert),(waypt_hori,waypt_vert))
    if i[0]=='L':
        rotations=int(int(i[1:])/90)
        wh=waypt_hori
        wv=waypt_vert
        if rotations==1:
            waypt_hori=wv
            waypt_vert=wh
            waypt_hori=-waypt_hori
        if rotations==2:
            waypt_hori=-waypt_hori
            waypt_vert=-waypt_vert
        if rotations==3:
            waypt_hori=wv
            waypt_vert=wh
            waypt_vert=-waypt_vert
        print((hori,vert),(waypt_hori,waypt_vert))
    if i[0]=='R':
        dir-=int(i[1:])
        if dir<0:
            dir+=360
        rotations=int(int(i[1:])/90)
        wh=waypt_hori
        wv=waypt_vert
        if rotations==1:
            waypt_hori=wv
            waypt_vert=wh
            waypt_vert=-waypt_vert
        if rotations==2:
            waypt_hori=-waypt_hori
            waypt_vert=-waypt_vert
        if rotations==3:
            waypt_hori=wv
            waypt_vert=wh
            waypt_hori=-waypt_hori
        print((hori,vert),(waypt_hori,waypt_vert))
    if i[0]=='F':
        hori+=waypt_hori*int(i[1:])
        vert+=waypt_vert*int(i[1:])
        print((hori,vert),(waypt_hori,waypt_vert))
print('Manhattan Distance with Waypoint:', abs(hori)+abs(vert))
