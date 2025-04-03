# REGULAR EXPRESSION ASSIGNMENT

"""Write a python program that checks every line in a file and returns the email address."""

import re
email_list = []

with open('data.txt') as file:
    for line in file:
        line = line.strip() #remove all whitespaces
        y = re.findall('([^ ]+@[^ ]+)', line) #this means find more than one non whitespace character followed by @ and more than one non whitespace character
        if y == []:
            continue
        else:
            for y in y:
                email_list.append(y)
                
print(email_list)

print('OR')

import re
email_list = []

with open('data.txt') as file:
    for line in file:
        line = line.strip() #remove all whitespaces
        y = re.findall('\w+@\w+\.\w+', line) #this means find more than one non whitespace character followed by @ and more than one non whitespace character
        if y == []:
            continue
        else:
            for y in y:
                email_list.append(y)
                
print(email_list)
