import os
input_indices={1:[0],12:[1],0:[2],20:[3],8:[4],16:[5]}

new_number=16
for i in range(6,30000000):
    if len(input_indices[new_number])==1:
        new_number=0
        if len(input_indices[0])==2:
            dictionary_values=input_indices[0]
            input_indices[0]=[dictionary_values[-1],i]
        else:
            input_indices[0].append(i)
    else:
        previous_indices=input_indices[new_number]
        new_number=previous_indices[-1]-previous_indices[-2]
        if new_number in input_indices:
            dictionary_values=input_indices[new_number]
            if len(input_indices[new_number])==2:
                input_indices[new_number]=[dictionary_values[-1],i]
            else:
                input_indices[new_number].append(i)
        else:
            input_indices[new_number]=[i]
    if i==2019:
        print('2020th number:',new_number)
    if i==29999999:
        print('30000000th number:',new_number)
