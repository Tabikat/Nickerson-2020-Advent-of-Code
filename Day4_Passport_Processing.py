import os
import re #regular expression
file=open('Day4.txt').read()
passports=file.split('\n\n')

for i in range(len(passports)):
    passports[i]=passports[i].replace('\n',' ')

expected_fields=['byr','iyr','eyr','hgt','hcl','ecl','pid']
#bry:#### (1920-2002)
#iyr:#### (2010-2020)
#eyr:#### (2020-2030)
#hgt:#cm (150-193) or #in (59-76)
#hcl:#xxxxxx (x is 0-9 or a-f)
#ecl:amb, blu, brn, gry, grn, hzl, oth
#pid:#########
#cid: ignored

#determines which passports contain all required fields
valid_passports=[]
for passport in passports:
    field_count=0
    for field in expected_fields:
        if field in passport:
            field_count+=1 #tracks that all fields are included
    if field_count==len(expected_fields):
        valid_passports.append(passport)
print('Number of Passports with all fields:',len(valid_passports))

#determines if the value in 'byr' is a number between the values 1920 and 2002
def birth_year(value):
    byr=re.compile('[0-9]+')
    validate=byr.match(value)
    if validate:
        if int(validate.group()) in range(1920,2003):
            return 1
        else:
            return 0
    else:
        return 0

#determines if the value in 'iyr' is a number between the values 2010 and 2020
def issue_year(value):
    iyr=re.compile('[0-9]+')
    validate=iyr.match(value)
    if validate:
        if int(validate.group()) in range(2010,2021):
            return 1
        else:
            return 0
    else:
        return 0

#determines if the value in 'eyr' is a number between the values 2020 and 2030
def expiration_year(value):
    eyr=re.compile('[0-9]+')
    validate=eyr.match(value)
    if validate:
        if int(validate.group()) in range(2020,2031):
            return 1
        else:
            return 0
    else:
        return 0

#determines if the value in 'hgt' is between 150-193 cm or 59-76 in
def height(value):
    hgt_num=re.compile('[0-9]+')
    validate_num=hgt_num.match(value)
    hgt_unit=re.compile('[cmin]+')
    validate_unit=hgt_unit.search(value)
    if validate_unit:
        if validate_unit.group()=='cm':
            if int(validate_num.group()) in range(150,194):
                return 1
            else:
                return 0
        elif validate_unit.group()=='in':
            if int(validate_num.group()) in range(59,77):
                return 1
            else:
                return 0
    else:
        return 0

#determines if the value in 'hcl' is of the form #xxxxxx where x is 0-9 or a-f
def hair_color(value):
    hcl_octo=re.compile('\#')
    validate_octo=hcl_octo.match(value)
    hcl=re.compile('[a-f0-9]+')
    validate_hcl=hcl.search(value)
    if validate_octo:
        if validate_hcl.end()-validate_hcl.start()==6:
            return 1
        else:
            return 0
    else:
        return 0

#determines if the value in 'ecl' is amb, blu, brn, gry, grn, hzl, or oth
def eye_color(value):
    options=['amb','blu','brn','gry','grn','hzl','oth']
    ecl=re.compile('[a-z]+')
    validate=ecl.match(value)
    if validate:
        if validate.group() in options:
            return 1
        else:
            return 0
    else:
        return 0

#determines if the value in 'pid' is a 9-digit number
def passport_ID(value):
    pid=re.compile('[0-9]+')
    validate=pid.match(value)
    if validate:
        if int(validate.end()-validate.start())==9:
            return 1
        else:
            return 0
    else:
        return 0

#makes fields into dictionaries for quick reference
for i in range(len(valid_passports)):
    all_fields={}
    valid_passports[i]=valid_passports[i].split(' ')
    for j in valid_passports[i]:
        field={}
        field[j[0:3]]=j[4:]
        all_fields.update(field)
    valid_passports[i]=all_fields

#determines if the passports with all field contain valid data
num_of_valid_passports=0
for passport in valid_passports:
    validation=0
    validation+=birth_year(passport['byr'])
    validation+=issue_year(passport['iyr'])
    validation+=expiration_year(passport['eyr'])
    validation+=height(passport['hgt'])
    validation+=hair_color(passport['hcl'])
    validation+=eye_color(passport['ecl'])
    validation+=passport_ID(passport['pid'])
    if validation==len(expected_fields):
        num_of_valid_passports+=1
print('Number of Valid Passports:',num_of_valid_passports)
