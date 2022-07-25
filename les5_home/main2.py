
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
        mark = data.split()[1]
        number = int(data.split()[2])

        student1 = student_names[2]
        student1["marks"].append(mark)


        print(student1)


    if command == "exit":
        break
