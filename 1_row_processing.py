#to clean the raw data

file = open("raw_data.txt", "r")

data = file.readline()

#clear \n \r \t
data = data.split("\\n")
for i in range(len(data)):
	data[i] = data[i].replace("\\r","")
	data[i] = data[i].replace("\\t","")

#clear HTML tags
for i in range(len(data)):
	# 1 row processing
	tags = []
	for j in range(len(data[i])):
		if data[i][j] == "<":
			begin = j
		if data[i][j] == ">":
			end = j
			tags.append(data[i][begin:end+1])
	for tag in tags:
		data[i] = data[i].replace(tag,"")

#clear spaces
for i in range(len(data)):
	data[i] = data[i].strip()

#clear empty lines
not_empty = []
for i in range(len(data)):
	if data[i] != "":
		not_empty.append(data[i])
data = not_empty

name = data[7]
dob = data[8]
scores = data[9]



#fixing unicode
chars = []
codes = []
file = open("unicode.txt", encoding="utf8",mode="r")
table = file.read().split("\n")
for i in table:
	element = i.split(" ")
	chars.append(element[0])
	codes.append(element[1])
for i in range(len(codes)):
	name = name.replace(codes[i], chars[i])
	scores = scores.replace(codes[i], chars[i])

#fixing more special charaters
for i in range(len(name)):
	if name[i:i+2] == "&#":
		name = name.replace(name[i:i+6],chr(int(name[i+2:i+5])))

for i in range(len(scores)):
	if scores[i:i+2] == "&#":
		scores = scores.replace(scores[i:i+6],chr(int(scores[i+2:i+5])))

data = [name, dob, scores]



file = open("test.txt",encoding="utf8",mode="w")
for i in range(len(data)):
	file.write(str(data[i]) + "\n")	


