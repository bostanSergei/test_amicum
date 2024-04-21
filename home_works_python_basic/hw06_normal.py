class School:
    def __init__(self):
        self.classes = []

    def add_class(self, school_class):
        self.classes.append(school_class)

    def get_all_classes(self):
        return [school_class.name for school_class in self.classes]


class SchoolClass:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
            teacher.classes.append(self)

    def get_students(self):
        return [student.get_full_name() for student in self.students]

    def get_teachers(self):
        return [teacher.get_full_name() for teacher in self.teachers]


class Student:
    def __init__(self, first_name, last_name, parent1, parent2):
        self.first_name = first_name
        self.last_name = last_name
        self.parent1 = parent1
        self.parent2 = parent2

    def get_full_name(self):
        return f"{self.last_name} {self.first_name[0]}."

    def get_parents(self):
        return f"Мама: {self.parent1.get_full_name()}, Папа: {self.parent2.get_full_name()}"

    def get_subjects(self, school_class):
        return [teacher.subject for teacher in school_class.teachers]


class Parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"


class Teacher:
    def __init__(self, first_name, last_name, subject):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.classes = []

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def teach_classes(self):
        return [school_class.name for school_class in self.classes]


my_school = School()

class_5A = SchoolClass("5А")
class_7B = SchoolClass("7Б")

my_school.add_class(class_5A)
my_school.add_class(class_7B)

teacher_math = Teacher("Иван", "Иванов", "Математика")
teacher_phy = Teacher("Петр", "Петров", "Физика")

class_5A.add_teacher(teacher_math)
class_7B.add_teacher(teacher_phy)

mother = Parent("Ольга", "Смирнова")
father = Parent("Алексей", "Смирнов")

student1 = Student("Илья", "Смирнов", mother, father)

class_5A.add_student(student1)

print("Список классов в школе:", my_school.get_all_classes())
print("Список учеников в классе 5А:", class_5A.get_students())
print("Список предметов ученика Илья:", student1.get_subjects(class_5A))
print("Родители ученика Илья:", student1.get_parents())
print("Список учителей в классе 5А:", class_5A.get_teachers())
