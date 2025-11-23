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
   - Option "student" - gets student's name and last name (as a single variable, can be as two variables if implemented correctly) and name of his/her class (i.e. 3C)
   - Option "teacher" - gets teacher's name and last name (as a single variable, can be as two variables if implemented correctly), name of the subject teacher is responsible for, and finally the names of classes he/she drives - each in new line till empty line is received
   - Option "mentor" - gets mentor's name and last name (as a single variable, can be as two variables if implemented correctly) and name of class he/she is mentoring
   - Option "finish" - return to the first menu

Managing users:

It is required to select one option: class, student, teacher, mentor or finish. After performing each option (except "finish") the menu should be displayed again
   - Option "class" - gets the info about particular class (i.e. 3C) - the list of students belonging to this class and the mentor
   - Option "student" - gets student's name and last name, all his subjects and teachers responsible for subjects
   - Option "teacher" - gets teacher's name and last name, and all "his/her" subjects
   - Option "mentor" - gets teacher's name and last name, and all "his/her" students
   - Option "finish" - return to the first menu

*
"""
class Student:
    def __init__(self, name, last_name, class_name, list_of_subjects):
        self.name = name
        self.last_name = last_name
        self.class_name = class_name
        self.list_of_subjects = list_of_subjects

    def __repr__(self):
        return f"Student({self.name}, {self.last_name}, {self.class_name}, {self.list_of_subjects})"

class Teacher:
    def __init__(self, name, last_name, subject):
        self.name = name
        self.last_name = last_name
        self.subject = subject

    def __repr__(self):
        return f"Teacher({self.name}, {self.last_name}, {self.subject})"

class Mentor:
    def __init__(self, name, last_name, class_name):
        self.name = name
        self.last_name = last_name
        self.class_name = class_name

    def __repr__(self):
        return f"Mentor({self.name}, {self.last_name}, {self.class_name})"

# class Class:
#     def __init__(self, class_name):
#         self.class_name = class_name
#
#     def __repr__(self):
#         return f"Class({self.class_name}, with students {self.students_list} and mentors {self.mentor_list})"

school = {
    "students": [
        Student("Armin", "van Buuren", "1A", ["Trance", "Techno", "EDM"]),
        Student("Paul", "Oakenfold", "2B", ["Trance", "EDM"]),
        Student("Paul", "van Dyk", "1A", ["Trance", "Techno"]),
        Student("Oliver", "Heldens", "2B", ["Techno", "EDM"]),
    ],
    "teachers" : [
        Teacher("Tijs", "Verwest", "Trance"),
        Teacher("Adam", "Beyer", "Techno"),
        Teacher("Martin", "Garrix", "EDM"),
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

def search_subject_list_for_a_student (students, ):
    teachers_by_class_list = []

while True:
    user_input = input("Choose command:\n1. Create\n2. Manage\n3. End\n")
    if user_input == "1":
        object_to_create = input(
            "Whom do you want to create?\n1. Student\n2. Teacher\n3. Mentor"
        )
        match object_to_create:
            case "1":
                students_name = input("Provide student's name: ")
                students_last_name = input("Provide student's last name: ")
                students_class = input("Provide class name: ")
                students_list_of_subjects = []
                while True:
                    subject = input("Provide student's subject: ")
                    if not subject:
                        break
                    else:
                        students_list_of_subjects.append(subject)
                student = Student(
                    students_name,
                    students_last_name,
                    students_class,
                    students_list_of_subjects
                )
                school["students"].append(student)

            case "2":
                teachers_name = input("Provide teacher's name: ")
                teachers_last_name = input("Provide teacher's last name: ")
                teachers_subject = input("Provide teacher's subject: ")
                teacher = Teacher(
                    teachers_name,
                    teachers_last_name,
                    teachers_subject
                )
                school["teachers"].append(teacher)

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

    elif user_input == "2":
        manage_option = input(
            "What would you like to manage?\n1. Class\n2. Student\n3. Teacher\n4. Mentor\n"
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
            #     linia = wyszukaj_linie_lotnicza_pasazera(
            #         imie=imie_pasazera, nazwisko=nazwisko_pasazera, lotnisko=lotnisko
            #     )
            #     if linia:
            #         print(f"Nazwa linii {imie_pasazera} {nazwisko_pasazera} to {linia}")
            #     else:
            #         print(
            #             "Nie ma takiego pasażera lub nie mamy takiej linii lotniczej."
            #         )
            # case "3":
            #     nazwa_linii = input("Podaj nazwę linii lotniczej: ")
            #     lista_lotow = znajdz_loty_linii_lotniczej(
            #         nazwa_linii, lotnisko.get("linie_lotnicze")
            #     )
            #     print(f"Lista lotów {nazwa_linii} to {lista_lotow}")
            # case "4":
            #     imie = input("Podaj imię stewardessy: ")
            #     nazwisko = input("Podaj nazwisko stewardessy: ")
            #     numer_lotu_stewardessy = znajdz_lot_stewardessy(
            #         imie, nazwisko, lotnisko.get("stewardessy")
            #     )
            #     lista_pasazerow = wyszukaj_pasazerow_lotu(
            #         lotnisko.get("pasazerowie"), numer_lotu_stewardessy
            #     )
            #     print(
            #         f"Pasażerowie lotu stewardessy {imie} {nazwisko} to {lista_pasazerow}"
            #     )
    elif user_input == "3":
        break

