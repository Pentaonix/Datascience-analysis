import csv
#to clean the raw data

file = open("raw_data.txt", "r")

datas = file.read().split("\n")

header = ["SBD", "tên", "dd", "mm", "yy", "toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hoá học", "tiếng anh"]
with open("clean_data.txt", encoding="utf8", mode="w", newline = "") as file_csv:
	writer = csv.writer(file_csv)
	writer.writerow(header)
sbd = 2000000
for data in datas:
	sbd += 1
	with open("wrong_id.txt", mode = "r") as file:
		sbds = file.read().split(",")
		if str(sbd) in sbds:
			continue
	sbd_str = "0" + str(sbd)
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

	# standardize data
	name = name.lower()
	scores = scores.lower()

	dob_list = dob.split("/")
	dd = dob_list[0]
	mm = dob_list[1]
	yy = dob_list[2]

	scores = scores.replace(":", "")
	scores = scores.replace("khxh ", "khxh   ")
	scores = scores.replace("khtn ", "khtn   ")
	scores = scores.replace(" 10", "  10")
	scores_list = scores.split("   ")

	data = [sbd_str, name.title(), int(dd), int(mm), int(yy)]

	for subjects in ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hoá học", "tiếng anh"]:
		if subjects in scores_list:
			data.append(float(scores_list[scores_list.index(subjects) + 1]))
		else:
			data.append(-1)

	with open("clean_data.txt", encoding="utf8", mode="a", newline = "") as file_csv:
		writer = csv.writer(file_csv)
		writer.writerow(data)
	


