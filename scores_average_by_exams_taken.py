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
num_of_exams_taken_per = [0,0,0,0,0,0,0,0,0,0]
scores_sum_by_exems_taken = [0,0,0,0,0,0,0,0,0,0]
scores_average_by_exems_taken = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(students)):
	students[i] = students[i].split(",")

#loop for each student
for s in students:
	count = 0					#numbers of subjects
	score_student = 0			#scores total for them
	score_student_average = 0	#average score of that student
	#loop over all subjects of 1 student
	for i in range(5,16):
		if s[i] != "-1":
			if i == 7 or i == 8:
				continue
			count += 1
			score_student += float(s[i])
		if count != 0:
			score_student_average = score_student/count
	num_of_exams_taken[count] += 1
	scores_sum_by_exems_taken[count] += score_student_average

total = 0
for i in num_of_exams_taken:
	total += i


for i in range(len(num_of_exams_taken)):
	num_of_exams_taken_per[i] = round(num_of_exams_taken[i]*100/total,4)

for i in range(len(scores_sum_by_exems_taken)):
	if num_of_exams_taken[i] != 0:
		scores_average_by_exems_taken[i] = round(scores_sum_by_exems_taken[i]/num_of_exams_taken[i],2)

print(num_of_exams_taken)
print(scores_average_by_exems_taken)

# #barchart
# #set limit to vertical axis
# figure, axis = plt.subplots()
# axis.set_ylim(0,100)

# #list from 0-11 -> get name
# y_pos = np.arange(len(subjects))

# #plot the barchart using 2 list(name,value)
# plt.bar(y_pos, dont_take_exam_percentage, align='center', alpha=0.5)

# #change horizontal category name
# plt.xticks(y_pos, subjects)

# #labeling for vertical axis
# plt.ylabel('Percentage(%)')

# #barchart's name
# plt.title('Exams_not_taken')

# #set labels for columns
# rects = axis.patches
# for rect, label in zip(rects, dont_take_exam):
#     height = rect.get_height()
#     axis.text(rect.get_x() + rect.get_width() / 2, height + 1, label,
#             ha='center', va='bottom')

# plt.show()

