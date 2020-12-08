import os
import re

hgt_num=re.compile('[0-9]+')
validate_num=hgt_num.match('193cm')
print(validate_num)
hgt_unit=re.compile('[cmin]+')
validate_unit=hgt_unit.search('193cm')
print(validate_unit)
if validate_unit:
    if validate_unit.group()=='cm':
        if int(validate_num.group()) in range(150,193):
            print(int(validate_num.group()),'cm')
        else:
            print('None')
    elif validate_unit.group()=='in':
        if int(validate_num.group()) in range(59-76):
            print(int(validate_num.group()),'in')
