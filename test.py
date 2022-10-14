grades = {"Математика" : [2, 5, 7, 8], "Русский" : [2, 5, 6, 7]}
gradesr = {"Математика" : [1, 5, 7, 8], "Русский" : [2, 5, 6, 7]}


sum_rating = 0
len_rating = 0
for lesson in grades.keys():
    key = "Русский"
    if lesson == key:
        print(sum(grades[key]))

