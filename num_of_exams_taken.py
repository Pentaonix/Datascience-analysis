import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

with open("clean_data.csv", mode = "r") as file:
	data = file.read().split("\n")

#take header
header = data[0]
header = header.split(",")

#take subjects from header
subjects = header[5:]

#get students list
students = data[1:]
students.pop()
total_students = len(students)

num_of_exams_taken = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(students)):
	students[i] = students[i].split(",")

for s in students:
	count = 0
	for i in range(5,16):
		if s[i] != "-1":
			count += 1
			if i == 7 or i == 8:
				count -= 1
	num_of_exams_taken[count] += 1

print(subjects)
print(students[0])
print(num_of_exams_taken)