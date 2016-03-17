n = int(raw_input())
students = [[raw_input(),float(raw_input())] for i in range(n)]
grades = list(set(j[1] for j in students))
grades.sort()
penultimateGrade = grades[1]
printedStudents = []
for student in students:
    if student[1] == penultimateGrade:
        printedStudents.append(student[0])
printedStudents.sort()
for name in printedStudents:
    print name