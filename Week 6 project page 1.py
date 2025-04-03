

"""A program that manages students grades and information for a classroom.
The dictionary should contain the students name, ID and list of grades
Write functions that can add new students, update grades and remove students from gradebook.
Calculate the average for each student and overall class average for assignment, exams etc.
Reports of grade-distribution, top performing and students at risk should be generated."""

print('')
print('WESLEY SECONDARY SCHOOL SCIENCE DEPARTMENT GRADEBOOK: FIRST TERM')
print('')

#students main dictionary

students = {'101': 'Ebuka', '102': 'Cessa', '103': 'John'}

#each students dictionary

Ebuka = {'name' : 'Ebuka Wilfred', 'ID' : 101, 'grades for exams' : [90, 85, 71], 'grades for assignments' : [40, 42, 48]}
Cessa  = {'name' : 'Cessa Prince', 'ID' : 102, 'grades for exams' : [95, 93, 89], 'grades for assignments' : [50, 48, 49]}
John = {'name' : 'John Cena', 'ID' : 103, 'grades for exams' : [60, 81, 74], 'grades for assignments' : [35, 40, 38]}

#function that can add student
print('Function that adds new students')
def add_new_student(last_key, student, full_name, ID, exam_lst, assign_lst ):
    students[str(int(last_key) + 1)] = student
    student = students[str(int(last_key) + 1)]
    student = {}
    student['name'] = full_name
    student['ID'] = ID
    student['grades for exams'] = exam_lst
    student['grades for assignments'] = assign_lst
    print(student)
    print(students)

last_key = input('Enter last value: ')
student = input('Enter name: ')
full_name = input('Enter full name: ')
ID = str(int(last_key) + 1)
exam_lst = []

exam_lst.append(input('Enter exam1: '))
exam_lst.append(input('Enter exam2: '))
exam_lst.append(input('Enter exam3: '))

assign_lst = []
assign_lst.append(input('Enter assign1: '))
assign_lst.append(input('Enter assign2: '))
assign_lst.append(input('Enter assign3: '))

add_new_student(last_key, student,full_name, ID, exam_lst, assign_lst)

#Function that updates grades

# def update(key, student, full_name, ID, n_exam_lst, assign_lst):
#     students[key] = student
#     student = students[key]
#     student = {}
#     student['name'] = full_name
#     student['ID'] = ID
#     student['grades for exams'] = n_exam_lst
#     student['grades for exams'] = assign_lst
#     print(student)

# key = input('Enter key: ')
# student = input('Enter name of student: ')
# full_name = input('Enter full name: ')
# ID = int(key)
# n_exam_lst = []

# n_exam_lst.append(input('Enter exam1: '))
# n_exam_lst.append(input('Enter exam2: '))
# n_exam_lst.append(input('Enter exam3: '))

# assign_lst = []
# assign_lst.append(input('Enter assign1: '))
# assign_lst.append(input('Enter assign2: '))
# assign_lst.append(input('Enter assign3: '))


# update(key, student, full_name, ID, n_exam_lst, assign_lst)







# #average for each student for the term

# print('Student\'s Averge')
# print('')

# #avg for 101
# print('Average for 101')
# print('')

# g_list101 = Ebuka.get('grades for exams')

# num_sum = 0
# length = len(g_list101)

# for grade in g_list101:
#     num_sum += grade
# avg_for_101 = num_sum/length

# #avg for 102
# print('Average for 102')
# print('')

# g_list102 = Cessa.get('grades for exams')

# num_sum = 0
# length = len(g_list102)

# for grade in g_list102:
#     num_sum += grade
# avg_for_102 = num_sum/length

# #avg for 103
# print('Average for 103')

# g_list103 = John.get('grades for exams')

# num_sum = 0
# length = len(g_list103)

# for grade in g_list103:
#     num_sum += grade
# avg_for_103 = num_sum/length



