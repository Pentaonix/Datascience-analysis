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

total = 0
for i in num_of_exams_taken:
	total += i

num_of_exams_taken_per = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(num_of_exams_taken)):
	num_of_exams_taken_per[i] = round(num_of_exams_taken[i]*100/total,4)



#Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = num_of_exams_taken
sizes = num_of_exams_taken_per
explode = (0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0)
#explode = (0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


print(subjects)
print(students[0])
print(num_of_exams_taken)