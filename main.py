students = [
    {
        "name": "Alice",
        "age": 17,
        "gender": "Female",
        "address": {
            "city": "Phnom Penh",
            "district": "Chamkarmon"
        },
        "subjects": [
            {"name": "Math", "score": 85},
            {"name": "Physics", "score": 78},
            {"name": "Biology", "score": 90}
        ]
    },
    {
        "name": "Sokha",
        "age": 16,
        "gender": "Male",
        "address": {
            "city": "Siem Reap",
            "district": "Svay Dangkum"
        },
        "subjects": [
            {"name": "English", "score": 75},
            {"name": "Computer", "score": 88},
            {"name": "Art", "score": 92}
        ]
    },
    {
        "name": "Dara",
        "age": 18,
        "gender": "Male",
        "address": {
            "city": "Battambang",
            "district": "Battambang"
        },
        "subjects": [
            {"name": "History", "score": 60},
            {"name": "Geography", "score": 70},
            {"name": "Math", "score": 80}
        ]
    }
]

# Q1.How many Male Students?
count_male = 0
for student in students:
  if student["gender"] == "Male":
    count_male += 1
print('Male student are:',count_male)
# Q2.How many students learn in "Math"?
count_math = 0
for student in students:
  for subject in student['subjects'] :
    if subject['name'] == "Math" :
      count_math += 1
print('student who study math:',count_math)
# Q3.Cellulate  average score of Sokha
total_score = 0
total_subject = 0
for student in students :
  if student['name'] == "Sokha":
    for subject in student['subjects']:
      total_score += subject['score']
      total_subject += 1
print('Average score of sokha :',total_score/total_subject)
# Q4.Sum total score of Dara
total_score = 0
for student in students :
  if student['name'] == "Dara":
    for subject in student['subjects']:
      total_score += subject['score']
print('Total score of Dara :',total_score)