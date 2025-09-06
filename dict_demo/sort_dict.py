students = [
    {"name": "Alice", "age": 25, "score": 85},
    {"name": "Bob", "age": 22, "score": 92},
    {"name": "Charlie", "age": 23, "score": 78},
    {"name": "David", "age": 24, "score": 88}
]

sorted_students = sorted(students, key=lambda x: x["age"],reverse=True)
print(sorted_students)

