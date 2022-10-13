from operator import le


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
# Прописать функцию среднего значения оценки
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
            average_rating = sum_rating / len_rating
            return print(average_rating)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


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
 




#Студенты
student_1 = Student('Игорь', 'Игорев', 'Муж')
student_1.courses_in_progress += ['Python']

student_2 = Student('Светлана', 'Светкина', 'Жен')
student_2.courses_in_progress += ['Python']

#Лекторы
lecturer_1 = Lecturer('Олег', 'Олегов')
lecturer_1.courses_attached += ['Python']
 
lecturer_2 = Lecturer('Ирина', 'Иринова')
lecturer_2.courses_attached += ['Python']

#Проверяющие
reviewer_1 = Reviewer('Сергей', 'Сергеев')
reviewer_1.courses_attached += ['Python']
 
reviewer_2 = Reviewer('Ольга', 'Ольгова')
reviewer_2.courses_attached += ['Python']

# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 9)

print(student_1.av_rating())