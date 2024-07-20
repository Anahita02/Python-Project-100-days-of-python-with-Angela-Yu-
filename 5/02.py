#challenge2

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

average = 0
for average_height in student_heights:
    average += average_height

number_of_student = 0
for student in student_heights:
    number_of_student +=1

average_student_height = round(average / number_of_student)
print(average_student_height)