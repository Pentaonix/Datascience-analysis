import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

with open("clean_data.csv", encoding = "utf8", mode = "r") as file:
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

#last name list
name_list - [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for student in students:
    student = student.split(',')
    print(student[1])