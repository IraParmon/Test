# coding=utf-8
student_names = []

while True:
    data = input()  # [add, Ivan, Ivanov]
    command = data.split()[0]
    if command == "add":
        name = data.split()[1]
        sname = data.split()[2]
        new_student = {"name": name + ' ' + sname, "marks": []}
        student_names.append(new_student)

    if command == "all":
        print(student_names)

    if command == "mark":  # mark <Оценка> <Номер>
        mark = int(data.split()[1])
        number = int(data.split()[2])

        student1 = student_names[number - 1]
        student1["marks"].append(mark)
        # print(student1)

    if command == "delete":  # delete <Номер>
        number = int(data.split()[1])
        student_names.pop(number - 1)

    if command == "edit":  # edit <Номер> <Имя> <Фамилия> 	Изменяет имя
        number = int(data.split()[1])
        name = data.split()[2]
        sname = data.split()[3]
        student2 = student_names[number - 1]
        student2["name"] = name + ' ' + sname
        # print(student2)

    if command == "average":  # average <Оценка>
        number = int(data.split()[1])
        student1 = student_names[number - 1]
        average = int(sum(student1["marks"]) / len(student1["marks"]))
        print(average)

    if command == "exit":
        break
