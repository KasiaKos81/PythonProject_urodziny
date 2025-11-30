"""
Create a program, which manages a school's database. There should be a possibility to create three types of users (student, teacher, mentor), there should be a possibility to manage those type of users
**Program for managing the school's DB**

Requirements:

The program user will have a possibility to enter one of the below mentioned commands:

- "create" - to create a new user (student, teacher, mentor)
- "manage" - to manage a user
- "end" - to exit the program

Creating users:

It is required to select one option: student, teacher, mentor or finish. After performing each option (except "finish") the menu should be displayed again
   - Option "student" - asks user to provide student's name and last name (as a single variable, can be as two variables if implemented correctly) and name of his/her class (i.e. 3C)
   - Option "teacher" - asks user to provide teacher's name and last name (as a single variable, can be as two variables if implemented correctly), name of the subject teacher is responsible for, and finally the names of classes he/she drives - each in new line till empty line is received
   - Option "mentor" - asks user to provide mentor's name and last name (as a single variable, can be as two variables if implemented correctly) and name of class he/she is mentoring
   - Option "finish" - return to the first menu

Managing users:

It is required to select one option: class, student, teacher, mentor or finish. After performing each option (except "finish") the menu should be displayed again
   - Option "class" - gets the info about particular class (i.e. 3C) - the list of students belonging to this class and the mentor
   - Option "student" - asks user to provide student's name and last name, then gets his subjects and teachers responsible for subjects
   - Option "teacher" - asks user to provide teacher's name and last name, then gets all "his/her" subjects
   - Option "mentor" - asks user to provide mentor's name and last name, then gets all "his/her" students
   - Option "finish" - return to the first menu

*
"""

class Student:
    def __init__(self, name, last_name, class_name):
        self.name = name
        self.last_name = last_name
        self.class_name = class_name

    def __repr__(self):
        return f"Student({self.name}, {self.last_name}, {self.class_name})"

class Teacher:
    def __init__(self, name, last_name, subject, list_of_classes):
        self.name = name
        self.last_name = last_name
        self.subject = subject
        self.list_of_classes = list_of_classes

    def __repr__(self):
        return f"Teacher({self.name}, {self.last_name}, {self.subject}, {self.list_of_classes})"

class Mentor:
    def __init__(self, name, last_name, class_name):
        self.name = name
        self.last_name = last_name
        self.class_name = class_name

    def __repr__(self):
        return f"Mentor({self.name}, {self.last_name}, {self.class_name})"

school = {
    "students": [
        Student("Armin", "van Buuren", "1A"),
        Student("Paul", "Oakenfold", "2B"),
        Student("Paul", "van Dyk", "1A"),
        Student("Oliver", "Heldens", "2B"),
    ],
    "teachers" : [
        Teacher("Tijs", "Verwest", "Trance", ["1A", "2B"]),
        Teacher("Adam", "Beyer", "Techno", ["2B"]),
        Teacher("Martin", "Garrix", "EDM", ["1A", "2B"]),
    ],
    "mentors" : [
        Mentor("Jean Michel", "Jarre", "1A"),
        Mentor("David", "Guetta", "2B"),
    ]
}

def search_students_by_class_name (students, class_name):
    students_by_class_list = []
    for student in students:
        if student.class_name == class_name:
            students_by_class_list.append(student)
    else:
        if not students_by_class_list:
            print("There is no such class name")
    return students_by_class_list

def search_mentors_by_class_name (mentors, class_name):
    mentors_by_class_list = []
    for mentor in mentors:
        if mentor.class_name == class_name:
            mentors_by_class_list.append(mentor)
    else:
        if not mentors_by_class_list:
            print("There is no such class name")
    return mentors_by_class_list

def search_class_names_for_a_student (students, students_name, students_last_name):
    for student in students:
        if student.name == students_name and student.last_name == students_last_name:
            return student.class_name
    print("There is no such student")
    return None

def search_class_names_for_a_mentor (mentors, mentors_name, mentors_last_name):
    for mentor in mentors:
        if mentor.name == mentors_name and mentor.last_name == mentors_last_name:
            return mentor.class_name
    print("There is no such mentor")
    return None

def search_teacher_by_class_name(teachers, class_name):
    list_of_teachers = []
    for teacher in teachers:
        if class_name in teacher.list_of_classes:
            list_of_teachers.append(teacher)
    return list_of_teachers

def search_teachrs_subjects(teachers, teachers_name, teachers_last_name):
    for teacher in teachers:
        if teacher.name == teachers_name and teacher.last_name == teachers_last_name:
            return teacher.subject
    print("There is no such teacher")
    return None

while True:
    user_input = input("Choose command:\n1. Create\n2. Manage\n3. End\n")
    if user_input == "1":
        object_to_create = input(
            "Whom do you want to create?\n1. Student\n2. Teacher\n3. Mentor\n4. Finish\n"
        )
        match object_to_create:
            case "1":
                students_name = input("Provide student's name: ")
                students_last_name = input("Provide student's last name: ")
                students_class = input("Provide class name: ")
                student = Student(
                    students_name,
                    students_last_name,
                    students_class,
                )
                school["students"].append(student)
                print(student)

            case "2":
                teachers_name = input("Provide teacher's name: ")
                teachers_last_name = input("Provide teacher's last name: ")
                teachers_subject = input("Provide teacher's subject: ")
                teachers_list_of_classes = []
                while True:
                    class_name = input("Provide class name (press enter to finish): ")
                    if not class_name:
                        break
                    else:
                        teachers_list_of_classes.append(class_name)
                teacher = Teacher(
                    teachers_name,
                    teachers_last_name,
                    teachers_subject,
                    teachers_list_of_classes
                )
                school["teachers"].append(teacher)
                print(f"Added teacher: {teacher}")

            case "3":
                mentors_name = input("Provide mentor's name: ")
                mentors_last_name = input("Provide mentor's last name: ")
                mentors_class = input("Provide mentor's class: ")
                mentor = Mentor(
                    mentors_name,
                    mentors_last_name,
                    mentors_class
                )
                school["mentors"].append(mentor)
                print(f"Added mentor: {mentor}")

            case "4":
                continue

    elif user_input == "2":
        manage_option = input(
            "What would you like to manage?\n1. Class\n2. Student\n3. Teacher\n4. Mentor\n5. Finish\n"
        )
        match manage_option:
            case "1":
                class_name = input(
                    "Provide class name: "
                )
                students_by_class_list = search_students_by_class_name(
                    school.get("students"), class_name
                )
                mentors_by_class_list = search_mentors_by_class_name(
                    school.get("mentors"), class_name
                )
                print(f"Mentors and students belonging to class {class_name}, Mentors: {mentors_by_class_list} Students: {students_by_class_list}")

            case "2":
                students_name = input("Provide student's name: ")
                students_last_name = input("Provide student's last name: ")
                class_name = search_class_names_for_a_student(school.get("students"), students_name, students_last_name)
                list_of_teachers = search_teacher_by_class_name(school.get("teachers"), class_name)
                print(f"List of student's subjects with the teachers: {list_of_teachers}")

            case "3":
                teachers_name = input("Provide teacher's name: ")
                teachers_last_name = input("Provide teacher's last name: ")
                subject = search_teachrs_subjects(school.get("teachers"), teachers_name, teachers_last_name)
                print(f"List of teacher's subjects: {subject}")

            case "4":
                mentors_name = input("Provide mentor's name: ")
                mentors_last_name = input("Provide mentor's last name: ")
                class_name = search_class_names_for_a_mentor(school.get("mentors"), mentors_name, mentors_last_name)
                list_of_students = search_students_by_class_name(school.get("students"), class_name)
                print(f"List of students lead by Mentor including their class names: {list_of_students}")

            case "5":
                continue

    elif user_input == "3":
        break

