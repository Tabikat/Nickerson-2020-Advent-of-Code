import os
file=open('Day6.txt').read()
groups=file.split('\n\n')

some_yes_answers=0
all_yes_answers=0
for i in range(len(groups)):
    num_of_people_in_group=groups[i].count('\n')+1
    groups[i]=groups[i].replace('\n','')
    #determines all possible answers for the group
    answers=[]
    for j in list(groups[i]):
        if j not in answers:
            answers.append(j)
    some_yes_answers+=len(answers)
    #determines which letters are in every answer
    nonanswers=[]
    for k in answers:
        if groups[i].count(k)!=num_of_people_in_group:
            nonanswers.append(k)
    all_yes_answers+=(len(answers)-len(nonanswers))


print('Sum of Yes Answers:', some_yes_answers)
print('Sum of All-Yes Answers:', all_yes_answers)
