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
name_list = []
name_count = []

for i in range(len(students)):
    students[i] = students[i].split(',')

for student in students:
    student = student[1].split(' ')
    last_name = student[0]
    print(last_name)
    if last_name not in name_list:
        name_list.append(last_name)
        name_count.append(0)
        #get 2 value with same index
        name_count[name_list.index(last_name)] += 1
    else:
        name_count[name_list.index(last_name)] += 1
print(name_list, name_count)
 