students = [('Alice', 85), ('Bob', 92), ('Charlie', 98)]
score_90_or_above = []
for student in students:
    if student[1] >= 90:
        score_90_or_above.append(student)

print(f'Students with score 90 or above: {score_90_or_above}')