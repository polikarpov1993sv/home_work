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
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
   
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
            average_rating = round(sum_rating / len_rating, 2)
            return average_rating

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        return self.av_rating() < other.av_rating()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
            average_rating = round(sum_rating / len_rating, 2)
            return average_rating

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rating()}"
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        return self.av_rating() < other.av_rating()      

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
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res




# Студенты
student_1 = Student('Игорь', 'Игорев', 'Муж')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Введение в програмирование"]

student_2 = Student('Светлана', 'Светкина', 'Жен')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Введение в програмирование"]

# Лекторы
lecturer_1 = Lecturer('Олег', 'Олегов')
lecturer_1.courses_attached += ['Python']
 
lecturer_2 = Lecturer('Ирина', 'Иринова')
lecturer_2.courses_attached += ['Python']

# Проверяющие
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

# Оценки лекторам
student_1.rate_lw(lecturer_1, 'Python', 10)
student_1.rate_lw(lecturer_1, 'Python', 8)
student_1.rate_lw(lecturer_1, 'Python', 6)

student_2.rate_lw(lecturer_2, 'Python', 10)
student_2.rate_lw(lecturer_2, 'Python', 6)
student_2.rate_lw(lecturer_2, 'Python', 6)

