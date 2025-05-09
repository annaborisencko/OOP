class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_grade(self, course_name=None):
        avgrade = 0
        if len(self.grades):
            if course_name:
                if course_name in self.grades.keys():
                    result = round(sum(self.grades[course_name])/len(self.grades[course_name]),1)
                else:
                    result = f'Студент {self.surname} {self.name} на включен в группу на курсе "{course_name}"'
                return result
            else:
                for course_name in self.grades.keys():
                    avgrade += round(sum(self.grades[course_name])/len(self.grades[course_name]),1)
                result = round(avgrade/len(self.grades),1)
                return result
        else:
            return f'У данного студента пока отсутствуют оценки за домашнее задание'
    
    def __str__(self):
        result = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade()}\n'
            f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {', '.join(self.finished_courses)}'
        )
        return result
    
    def __lt__(self, student):
        return self.average_grade() < student.average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self, course_name=None):
        avgrade = 0
        if len(self.grades):
            if course_name:
                if course_name in self.grades.keys():
                    result = round(sum(self.grades[course_name])/len(self.grades[course_name]),1)
                else:
                    result = f'Преподаватель {self.surname} {self.name} не преподает на курсе "{course_name}"'
                return result
            else:
                for course_name in self.grades.keys():
                    avgrade += round(sum(self.grades[course_name])/len(self.grades[course_name]),1)
                result = round(avgrade/len(self.grades),1)
                return result
        else:
            return f'У данного преподавателя пока отсутствуют оценки за лекции'

    def __str__(self):
        result = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.average_grade()}'
        )
        return result

    def __lt__(self, lecturer):
        return self.average_grade() < lecturer.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        result = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
        )
        return result

student1 = Student('Василий', 'Васильев', 'мужской')
student2 = Student('Иван', 'Иванов', 'мужской')

reviewer1 = Reviewer('Мая', 'Виноградова')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Зоя', 'Яблочкова')
reviewer2.courses_attached += ['Python расширенный']

lecturer1 = Lecturer('Николай', 'Расторгуев')
lecturer1.courses_attached += ['Python']


lecturer2 = Lecturer('София', 'Ротару')
lecturer2.courses_attached += ['Python расширенный']


student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['English']
student1.add_courses('Вокал')
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 7)


student2.courses_in_progress += ['Python расширенный']
student2.add_courses('Python')
student2.add_courses('Вокал')
reviewer2.rate_hw(student2, 'Python расширенный', 7)
reviewer2.rate_hw(student2, 'Python расширенный', 8)
reviewer2.rate_hw(student2, 'Python расширенный', 10)
student2.rate_lecturer(lecturer2, 'Python расширенный', 8)
student2.rate_lecturer(lecturer2, 'Python расширенный', 5)


print(f'Информация о студенте №1: \n{student1}\n')
print(f'Информация о студенте №2: \n{student2}\n')


print(f'Информация о проверяющем №1: \n{reviewer1}\n')
print(f'Информация о проверяющем №2: \n{reviewer2}\n')

print(f'Информация о лекторе №1: \n{lecturer1}\n')
print(f'Информация о лекторе №2: \n{lecturer2}\n')

if student1<student2:
    print(f'Лучший студент: {student2.surname} {student2.name}')
else:
    print(f'Лучший студент: {student1.surname} {student1.name}')

if lecturer1<lecturer2:
    print(f'Лучший преподаватель: {lecturer2.surname} {lecturer2.name}')
else:
    print(f'Лучший преподаватель: {lecturer2.surname} {lecturer2.name}')

#Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса)
def get_avgrade_of_students_by_course(students=[], course_name=None):
    avgrade = 0
    students_by_course = 0
    for student in students:
        if isinstance(student, Student) and course_name in student.courses_in_progress and student.grades.get(course_name):
            avgrade += student.average_grade(course_name)
            students_by_course += 1
        else:
            avgrade = avgrade
    if students_by_course:
        result = avgrade/students_by_course
    else: 
        result = f'На заданном курсе отсутствуют студенты, либо оценки им еще не выставлены'
    return result

#Функция для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса)
def get_avgrade_of_lecturers_by_course(lecturers=[], course_name=None):
    avgrade = 0
    lecturers_by_course = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached and lecturer.grades.get(course_name):
            avgrade += lecturer.average_grade(course_name)
            lecturers_by_course += 1
        else:
            avgrade = avgrade
    if lecturers_by_course:
        result = avgrade/lecturers_by_course
    else: 
        result = f'На заданном курсе отсутствуют преподаватели, либо оценки им еще не выставлены'
    return result

course_name = 'Python'
students = [student1, student2]
avgrade_by_course = get_avgrade_of_students_by_course(students, course_name)
print(f'Средняя оценка за домашние задания на курсе "{course_name}": {avgrade_by_course}')

lecturers = [lecturer1, lecturer2]
avgrade_by_course = get_avgrade_of_lecturers_by_course(lecturers, course_name)
print(f'Средняя оценка за лекции на курсе "{course_name}": {avgrade_by_course}')