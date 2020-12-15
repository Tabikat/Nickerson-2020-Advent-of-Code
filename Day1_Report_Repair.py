import os
file=open('Day1.txt').read()
expense_report=file.split()

expense_report=[int(i) for i in expense_report]

#finds the 2 values that add to 2020
for i in range(len(expense_report)):
    for j in range(i, len(expense_report)):
        sum=expense_report[i]+expense_report[j]
        if sum==2020:
            print('2 No. Expense Report 2020:',expense_report[i]*expense_report[j])
            break

#finds the 3 values that add to 2020
for i in range(len(expense_report)):
    for j in range(i, len(expense_report)):
        for k in range(j,len(expense_report)):
            sum=expense_report[i]+expense_report[j]+expense_report[k]
            if sum==2020:
                print('3 No. Expense Report 2020:',expense_report[i]*expense_report[j]*expense_report[k])
                break
