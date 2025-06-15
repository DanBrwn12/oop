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


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.finished_courses += ['Введение в программирование']

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

reviewer.rate_hw(student, 'Python', 5)
reviewer.rate_hw(student, 'Python', 6)
reviewer.rate_hw(student, 'Python', 7)

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка


student_2 = Student('Сергей', 'Сидоров', 'М')
student_2.finished_courses += ['Эффективное саморазвитие']
student_2.courses_in_progress += ['C++']
reviewer.rate_hw(student_2, 'C++', 9)
reviewer.rate_hw(student_2, 'C++', 9)

lecturer_2 = Lecturer('Жанна', 'Баклажанова')
lecturer_2.courses_attached += ['JS', 'Java', 'C++']

print(student_2.rate_lecture(lecturer_2, 'Python', 3))  # Ошибка
print(student_2.rate_lecture(lecturer_2, 'C++', 4))  # None
print(student_2.rate_lecture(lecturer_2, 'C++', 5))  # None


print(reviewer)
print(lecturer)
print(student)
print(student_2)

print(student < student_2)
print(lecturer >= lecturer_2)
print(student == student_2)