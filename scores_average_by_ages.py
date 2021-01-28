import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

with open("clean_data.csv", mode = "r") as file:
	data = file.read().split("\n")

#take header
header = data[0]
header = header.split(",")

#take subjects from header
subjects = header[5:]

total_subjects = subjects[0:2] + subjects[4:]

#get students list
students = data[1:]
students.pop()
total_students = len(students)

numbers_of_students_by_age_group = [0,0,0,0,0,0,0,0,0,0,0]
sum_score_of_a_student_by_age = [0,0,0,0,0,0,0,0,0,0,0]
average_score_of_a_student_by_age = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(students)):
	students[i] = students[i].split(",")

for student in students:
	count = 0
	score_student = 0
	score_student_average = 0
	age = 2020 - int(student[4])
	if age >= 27:
		age = 27
	numbers_of_students_by_age_group[age - 17] += 1
	#loop for calculating average score of a student by age
	for i in range(5,16):
		if student[i] != "-1":
			if i == 7 or i == 8:
				continue
			count += 1
			score_student += float(student[i])
		if count != 0:
			score_student_average = score_student/count
	sum_score_of_a_student_by_age[age-17] += score_student_average

for i in range(len(numbers_of_students_by_age_group)):
	average_score_of_a_student_by_age[i] = round(sum_score_of_a_student_by_age[i]/numbers_of_students_by_age_group[i],2)
print(numbers_of_students_by_age_group)
print(sum_score_of_a_student_by_age)
print(average_score_of_a_student_by_age)