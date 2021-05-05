"""
Part-I:
def student_grades():
    student_list  = []
    class_map = {1:"MATH", 2:"SCIENCE", 3:"HISTORY"}
    student_num = input("How many students in your list? Please input: ")
    student_num = int(student_num)
    for i in range(student_num):
        student_name = input("Please enter student name: ")
        grade = input("Please input grade: ")
        class_number = input("Please input class number: 1-Math, 2-Science and 3-History: ")
        class_name = class_map[int(class_number)]
        print(i)
        print(class_name)
        student_list.append({})
        student_list[i]["Name"] = student_name
        student_list[i]["Grade"] = grade
        student_list[i]["Course"] = class_name
    for i in range(student_num):
        print(f"Name: {student_list[i]['Name']}, Course: {student_list[i]['Course']}, Grade: {student_list[i]['Grade']}")

student_grades()

"""
"""
Part-II: with input validation:

"""
def student_grades():
    student_list  = []
    name_check = []
    class_map = {1:"MATH", 2:"SCIENCE", 3:"HISTORY"}
    student_num = input("How many students in your list? Please input: ")
    student_num = int(student_num)
    for i in range(student_num):
        go_back1 = True
        go_back2 = True
        go_back3 = True
        while go_back1:
            student_name = input("Please enter student name: ")
            if student_name.isalpha() == False:
                print("Please enter validate chareacter for name.")
                continue
            elif student_name in name_check:
                print("Name already exists and please input different name.")
                continue
            else:
                name_check.append(student_name)
                go_back1 = False
        while go_back2:
            grade = input("Please input grade: ")
            if grade.isnumeric() == False:
                print("Please enter numeric value to grades.")
                continue
            else:
                go_back2 = False
        while go_back3:
            class_number = input("Please input class number: 1-Math, 2-Science and 3-History: ")
            if class_number not in ("1", "2", "3"):
                print("Please enter correct class number: 1 or 2 or 3 but no others.")
                continue
            else:
                go_back3 = False
        class_name = class_map[int(class_number)]
        student_list.append({})
        student_list[i]["Name"] = student_name
        student_list[i]["Grade"] = grade
        student_list[i]["Course"] = class_name
    for i in range(student_num):
        print(f"Name: {student_list[i]['Name']}, Course: {student_list[i]['Course']}, Grade: {student_list[i]['Grade']}")

student_grades()