from operator import itemgetter

students = [
    {"name": "Alice", "age": 25, "score": 85},
    {"name": "Bob", "age": 22, "score": 92},
    {"name": "Charlie", "age": 23, "score": 78},
    {"name": "David", "age": 24, "score": 88}
]

sorted_students_method1 = sorted(students, key=lambda x: x["age"],reverse=True)
sorted_students_method2 = sorted(students, key=itemgetter("age"),reverse=True)

print(sorted_students_method1)
print(sorted_students_method2)

