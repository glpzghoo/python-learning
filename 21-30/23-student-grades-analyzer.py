names = []
scores = []

for i in range(0, 3):
    name = input("Сурагчийн нэр? - ")
    names.append(name)
    score = int(input("Сурагчийн дүн? - "))
    scores.append(score)

avg = sum(scores) / len(scores)
highestScore = max(scores)
lowestScore = min(scores)

index = scores.index(max(scores))
highestScoreStudent = names[index]
index = scores.index(min(scores))
lowestScoreStudent = names[index]

print(f"Дундаж: {avg}")
print(f"Хамгийн их: {highestScore}, Сурагч: {highestScoreStudent}")
print(f"Хамгийн бага: {lowestScore}, Сурагч: {lowestScoreStudent}")