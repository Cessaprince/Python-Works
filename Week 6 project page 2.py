


#students main dictionary

students = {'101': 'Ebuka', '102': 'Cessa', '103': 'John', '104' : 'Grace'}

#each students dictionary

Ebuka = {'name' : 'Ebuka Wilfred', 'ID' : 101, 'grades for exams' : [90, 85, 71], 'grades for assignments' : [40, 42, 48]}
Cessa  = {'name' : 'Cessa Prince', 'ID' : 102, 'grades for exams' : [95, 93, 89], 'grades for assignments' : [50, 48, 49]}
John = {'name' : 'John Cena', 'ID' : 103, 'grades for exams' : [60, 81, 74], 'grades for assignments' : [35, 40, 38]}



Ebuka_exam = Ebuka.get('grades for exams')
Cessa_exam = Cessa.get('grades for exams')
John_exam = John.get('grades for exams')

min_of_Ebuka = min(Ebuka_exam)
min_of_Cessa = min(Cessa_exam)
min_of_John = min(John_exam)

minimum = min_of_Ebuka
if minimum > min_of_Cessa:
    minimum = min_of_Cessa
    print(f'Student at risk is Cessa with a mminimum of {min_of_Cessa}') 
if minimum > min_of_John:
        print(f'Student at risk is John with a mminimum of {min_of_John}')
else:
    print(f'Student at risk is Ebuka with a mminimum of {min_of_Ebuka}') 
    

