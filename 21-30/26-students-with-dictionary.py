students = {}

for i in range(3):
    student = input("Сурагчийн нэр: ")
    score = int(input("Сурагчийн дүн: "))
    students[student] = score

print(students)

avg = sum(students.values()) / len(students)
highest = max(students.values())
lowest = min(students.values())

for name, score in students.items():
    print(f"{name} - {score}")

print(f"Хамгийн их: {highest}, Хамгийн бага: {lowest}, Дундаж: {avg}")