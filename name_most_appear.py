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
    # print(last_name)
    if last_name not in name_list:
        name_list.append(last_name)
        name_count.append(0)
        #get 2 value with same index
        name_count[name_list.index(last_name)] += 1
    else:
        name_count[name_list.index(last_name)] += 1
# print(name_list, name_count)

#bubble sort
for i in range(len(name_count)):
    for j in range(i+1,len(name_count) - 1):
        if name_count[j] > name_count[i]:
            #swap count
            temp = name_count[i]
            name_count[i] = name_count[j]
            name_count[j] = temp
            #swap name
            temp = name_list[i]
            name_list[i] = name_list[j]
            name_list[j] = temp

name_list = name_list[:20]
name_count = name_count[:20]
print(name_list, name_count)     

#barchart
#set limit to vertical axis
figure, axis = plt.subplots()
axis.set_ylim(0,25000)

#list from 0-11 -> get name
y_pos = np.arange(len(name_list))

#plot the barchart using 2 list(name,value)
plt.bar(y_pos, name_count, align='center', alpha=0.5)

#change horizontal category name
plt.xticks(y_pos, name_list)

#labeling for vertical axis
plt.ylabel('Number of appearance')

#barchart's name
plt.title('Name that appears the most')

#set labels for columns
rects = axis.patches
for rect, name_list in zip(rects, name_count):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height , name_list,
            ha='center', va='bottom')

plt.show()
 