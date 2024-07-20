#challenge2

student_scores = {
"Harry": 81,
"Ron": 78,
"Hermione": 99,
"Draco": 74,
"Nevil": 62,
}

student_grades={}

for student in student_scores:
    score = student_scores [student]
    if score >= 91:
        student_grades[student] ="outstanding"
    elif score >= 81:
        student_grades[student] ="Exceed Expectations"
    elif score >=71:
        student_grades[student] ="Acceptable"
    elif score <= 70:
        student_grades[student] ="Fail"



print(student_grades)