class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade_all_courses = 0

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def count_average_grade(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        if len(all_grades) != 0:
            self.average_grade_all_courses = sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade_all_courses < other.average_grade_all_courses

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade_all_courses <= other.average_grade_all_courses

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade_all_courses > other.average_grade_all_courses

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade_all_courses >= other.average_grade_all_courses

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade_all_courses == other.average_grade_all_courses

    def __str__(self):
        self.count_average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade_all_courses}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade_all_courses = 0

    def count_average_grade(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        if len(all_grades) != 0:
            self.average_grade_all_courses = sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_all_courses < other.average_grade_all_courses

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_all_courses <= other.average_grade_all_courses

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_all_courses > other.average_grade_all_courses

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_all_courses >= other.average_grade_all_courses

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_all_courses == other.average_grade_all_courses

    def __str__(self):
        self.count_average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade_all_courses:.1f}\n")


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


# Студенты
student = Student('Алёхина', 'Ольга', 'Ж')
student_2 = Student('Сергей', 'Сидоров', 'М')

# Лекторы
lecturer = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Жанна', 'Баклажанова')

# Проверяющие
reviewer = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Максим', 'Галкин')

# Добавляем курсы студентам
student.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['C++']

# Добавляем курсы лектрам и проверяющим
lecturer.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['JS', 'Java', 'C++']
reviewer.courses_attached += ['Python', 'C++']
reviewer_2.courses_attached += ['JS', 'Java', 'C++']

# Добавляем завершенные курсы студентам
student.finished_courses += ['Введение в программирование']
student_2.finished_courses += ['Эффективное саморазвитие']

# Проверяющий выставляет оценки
reviewer.rate_hw(student, 'Python', 5)
reviewer.rate_hw(student, 'Python', 6)
reviewer.rate_hw(student, 'Python', 7)
reviewer.rate_hw(student_2, 'C++', 9)
reviewer.rate_hw(student_2, 'C++', 9)

# Оценка лекторов студентами
student.rate_lecture(lecturer, 'Python', 7)
student.rate_lecture(lecturer, 'Java', 8)
student.rate_lecture(lecturer, 'С++', 8)
student.rate_lecture(reviewer, 'Python', 6)
student_2.rate_lecture(lecturer_2, 'Python', 3)
student_2.rate_lecture(lecturer_2, 'C++', 4)
student_2.rate_lecture(lecturer_2, 'C++', 5)

# Вывод метода __str__
print(student)
print(student_2)
print(lecturer)
print(lecturer_2)
print(reviewer)
print(reviewer_2)

# Операции сравнения
print(student < student_2)
print(lecturer >= lecturer_2)
print(student == student_2)

students = [student, student_2]
lecturers = [lecturer, lecturer_2]

def calc_avg_students(students, course_name):
    total = 0
    count = 0
    for student in students:
        if course_name in student.grades:
            total += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    return total / count if count != 0 else 0

def calc_avg_lecturers(lecturers, course_name):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total += sum(lecturer.grades[course_name])
            count += len(lecturer.grades[course_name])
    return total / count if count != 0 else 0

course_name = 'Python'

print(f"Cредняя оценка студентов по {course_name}: {calc_avg_students(students, course_name)}")
print(f"Средняя оценка лекторов по {course_name}: {calc_avg_lecturers(lecturers, course_name)}")

