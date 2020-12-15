import os
input=[1,12,0,20,8,16]
input_indices={1:[0],12:[1],0:[2],20:[3],8:[4],16:[5]}

while len(input)<30000000:
    if input.count(input[-1])==1:
        if len(input_indices[0])==2:
            dictionary_values=input_indices[0]
            input_indices[0]=[dictionary_values[-1],len(input)]
        else:
            input_indices[0].append(len(input))
        input.append(0)
        print(len(input))
    else:
        previous_indices=input_indices[input[-1]]
        new_number=previous_indices[-1]-previous_indices[-2]
        if new_number in input:
            dictionary_values=input_indices[new_number]
            if len(input_indices[new_number])==2:
                input_indices[new_number]=[dictionary_values[-1],len(input)]
            else:
                input_indices[new_number].append(len(input))
        else:
            input_indices[new_number]=[len(input)]
        input.append(new_number)
        print(len(input))
#print(input_indices)

print('2020th number:',input[2019])
print('30000000th number:',input[29999999])
