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

for i in range(len(students)):
	students[i] = students[i].split(",")

for student in students:
	age = 2020 - int(student[4])
	if age >= 27:
		age = 27
	numbers_of_students_by_age_group[age - 17] += 1

print(numbers_of_students_by_age_group)