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

for i in range(len(numbers_of_students_by_age_group)):
	average_score_of_a_student_by_age[i] = average_score_of_a_student_by_age[i]*70000/10
# print(numbers_of_students_by_age_group)
# print(sum_score_of_a_student_by_age)
# print(average_score_of_a_student_by_age)
label = ["17", "18", "19", "20", "21", "22", "23", "24", "25", "26", ">26"]

#barchart
#set limit to vertical axis
figure, axis = plt.subplots()
axis.set_ylim(0,70000)


#list from 0-11 -> get name
y_pos = np.arange(len(label))

#plot the barchart using 2 list(name,value)
plt.bar(y_pos, numbers_of_students_by_age_group, align='center', alpha=0.5)
plt.plot(y_pos, average_score_of_a_student_by_age, color = 'red', marker = 'o')

#change horizontal category name
plt.xticks(y_pos, label)

#set after plot chart
ax2 = axis.twinx()
ax2.tick_params('y', color = 'red') 
ax2.set_ylim(0,10)
ax2.set_ylabel("Average scores")


#labeling for vertical axis
axis.set_ylabel('Numbers of students')
axis.set_xlabel('Age')

#barchart's name
plt.title('Scores_average_by_ages')

#set labels for columns
rects = axis.patches
for rect, label in zip(rects, numbers_of_students_by_age_group):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height , label,
            ha='center', va='bottom')

plt.show()