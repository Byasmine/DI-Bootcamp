#exercice 1: Student Grade Summary
print("Exercice 1 : ")

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

#Calculate the avrg grade for each student and store the result
avg_student_grades = {}

for name, grades in student_grades.items():
    average = round (sum(grades)/len(grades),2) #rounding to 2 decimal places
    avg_student_grades[name] = average #assigne directly using key

print("Average student grades : ",avg_student_grades)

#Assign each student a letter grade (A,B,C,D,F)
student_letter_grades= {}
for name, avrg_grade in avg_student_grades.items() :
    if avrg_grade in range(80,90):
        student_letter_grades[name]= 'B'
    elif avrg_grade in range(70,80):
        student_letter_grades[name] ='C'
    elif avrg_grade in range(60,70):
        student_letter_grades[name]= 'D'
    elif avrg_grade < 60 :
        student_letter_grades[name]='F'
    else:
        student_letter_grades[name] = 'A'

print("\nStudent's Average grades : ")
for name in avg_student_grades:
    print(f"{name}: {avg_student_grades[name]} → {student_letter_grades[name]}")
