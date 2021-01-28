import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

with open("clean_data.csv",encoding="utf8", mode = "r") as file:
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

label = ["0 mon", "1 mon", "2 mon", "3 mon", "4 mon", "5 mon", "6 mon", "7 mon", "8 mon", "9 mon"]


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

#data = [float(x.split()[0]) for x in recipe]
data = num_of_exams_taken_per
#ingredients = [x.split()[-1] for x in recipe]
ingredients = label


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct)


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Numbers of exams taken",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Numbers of exams taken")

plt.show()



# #Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = num_of_exams_taken
# sizes = num_of_exams_taken_per
# explode = (0, 0, 0, 0, 0, 0, 0.1, 0, 0, 0)
# #explode = (0,0,0,0,0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()


# print(subjects)
# print(students[0])
# print(num_of_exams_taken)