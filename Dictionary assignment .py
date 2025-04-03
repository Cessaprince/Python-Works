#Iterating through a Dictionary

#sample output
# english: 55 (d)
# average score:

"""Writing a code that returns the subject from the dictionary, the grade score in A, B, C, D or E and the average score. """

subjects = {'English' : 55, 'Maths' : 76, 'Biology' : 81, 'Agric' : 65, 'Chemistry' : 49}

#The grades should look like: A = 80+, B = 70-79, C = 60-69, D = 50-59, E = 40 -49, F = below 39

#iterate through the dictionary 

for subject in subjects:
    if subjects[subject] <= 39:
        print(f'{subject} : {subjects[subject]} (F)')
        print('-' * 10)
    elif subjects[subject] <= 49:
        print(f'{subject} : {subjects[subject]} (E)')
        print('-' * 10)
    elif subjects[subject] <= 59:
        print(f'{subject} : {subjects[subject]} (D)')
        print('-' * 10)
    elif subjects[subject] <= 69:
        print(f'{subject} : {subjects[subject]} (C)')
        print('-' * 10)
    elif subjects[subject] <= 79:
        print(f'{subject} : {subjects[subject]} (B)')
        print('-' * 10)
    elif subjects[subject] >= 80:
        print(f'{subject} : {subjects[subject]} (A)')
        print('-' * 10)

#find the average score from the dictionary

total = 0

for score in subjects.values():
    num = len(subjects.values())
    total += score #total = total + score
avg = total/num
print(f'The average score for the dict, {subjects} is {avg}')



#Iterating through a List

"""Writing a code that removes duplicates from a list using iteration without using the string() function. """

print('-' * 100)

list_of_num = [2,2,7,9,8,4,3,1,5,6,7,3,3,2]
new_list_of_num = []

for num in list_of_num:
    if num not in new_list_of_num:
        new_list_of_num.append(num)
    else:
        continue

result = sorted(new_list_of_num)
print(result)    