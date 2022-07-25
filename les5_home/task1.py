student = {"name": "Ivanov Ivan", "marks": []}
student_names = []

while True:
    data = input()  # [add, Ivan, Ivanov]
    command = data.split()[0]
    if command == "add":
        name = data.split()[1]
        sname = data.split()[2]
        student[name + ' ' + sname] = []
        student_names.append(student)  #name + ' ' + sname

    if command == "all":
        for k, v in student.items():
            print(f"{k}")

    if command == "mark":  # mark <Оценка> <Номер>
        mark = data.split()[1]
        number = int(data.split()[2])

        student1 = student_names[1]
        student1["marks"].append("5")
        print(student_names)



        # if number == 1:
        #     student[student_names[0]].append(mark)
        #     print(f' {number}. {k} {mark}')
        # elif number == 2:
        #     student[student_names[1]].append(mark)
        #     print(student)

    if command == "exit":
        break
