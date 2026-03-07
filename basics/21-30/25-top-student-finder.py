students = []
scores = []

for i in range(3):
    student = input("Сурагчийн нэр: ")
    students.append(student)

    score = int(input("Сурагчийн дүн: "))
    scores.append(score)

top_score = max(scores)

for i, student in enumerate(students):
    if scores[i] == top_score:
        print(student, scores[i])