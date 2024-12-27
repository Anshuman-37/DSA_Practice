#Question 29: Multi-key sorting (like sorting a database table by multiple columns).
students = [
    ("Alice", 15, "A"),
    ("Bob", 16, "B"),
    ("Charlie", 15, "C"),
    ("David", 16, "A"),
    ("Eve", 15, "B")
]

# Sort by grade (ascending), then age (descending), then name (ascending)
sorted_students = sorted(
    students,
    key=lambda student: (student[2], -student[1], student[0])
)

for student in sorted_students:
    print(student)