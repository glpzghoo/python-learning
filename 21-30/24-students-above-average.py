students = []
scores = []

for i in range(3):
    student = input("Сурагчийн нэр: ")
    students.append(student)

    score = int(input("Сурагчийн дүн: "))
    scores.append(score)

avg = sum(scores) / len(scores)
print(f"Дундаж оноо: {avg}")

found = False

for i, student in enumerate(students):
    if scores[i] > avg:
        print(f"{student}-н дүн {scores[i]}, дунджаас илүү байна!")
        found = True

if not found:
    print("Дундаас дээш оноо авсан сурагч алга.")
