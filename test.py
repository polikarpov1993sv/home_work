grades = {"Математика" : [2, 5, 7, 8], "Русский" : [2, 5, 6, 7]}
gradesr = {"Математика" : [1, 5, 7, 8], "Русский" : [2, 5, 6, 7]}

def av_rating(grades):
    sum_rating = 0
    len_rating = 0
    for course in grades.values():
        sum_rating += sum(course)
        len_rating += len(course)
    average_rating = sum_rating / len_rating
    print(average_rating)

av_rating(grades)