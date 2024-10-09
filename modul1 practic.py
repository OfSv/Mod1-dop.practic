grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = list(tuple(students))
students_list.sort()

av_grades = map(lambda index_grades: sum(index_grades) / len(index_grades), grades)
average = dict(zip(students_list, av_grades))

print(average)