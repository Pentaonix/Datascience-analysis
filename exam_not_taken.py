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

print(students[0])
print(dont_take_exam_percentage)