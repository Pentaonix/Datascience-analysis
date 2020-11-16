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

#list for counting all drop-exam each subject
dont_take_exam = [0,0,0,0,0,0,0,0,0,0,0]
dont_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(students)):
	students[i] = students[i].split(",")

for s in students:
	for i in range(5,16):
		if s[i] == "-1":
			dont_take_exam[i-5] += 1

for i in range(0,11):
	dont_take_exam_percentage[i] = round(dont_take_exam[i]*100/total_students,2)

#barchart
#set limit to vertical axis
figure, axis = plt.subplots()
axis.set_ylim(0,100)

#list from 0-11 -> get name
y_pos = np.arange(len(subjects))

#plot the barchart using 2 list(name,value)
plt.bar(y_pos, dont_take_exam_percentage, align='center', alpha=0.5)

#change horizontal category name
plt.xticks(y_pos, subjects)

#labeling for vertical axis
plt.ylabel('Percentage(%)')

#barchart's name
plt.title('Exams_not_taken')

#set labels for columns
rects = axis.patches
for rect, label in zip(rects, dont_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 1, label,
            ha='center', va='bottom')

plt.show()