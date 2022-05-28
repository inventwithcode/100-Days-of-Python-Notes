# import random

# names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]

# scores = {
#     student: random.randint(1, 100) for student in names
# }

# print(scores)

# passed_students = {
#     student: score for (student, score) in scores.items() if score >= 60
# }

# print(passed_students)
import pandas

hunters = {
    "hunter": ["Dean", "Sam", "Bobby", "Jack"],
    "power": [100, 100, 110, 99999]
}

hunters_data_frame = pandas.DataFrame(hunters)

# print(hunters_data_frame)
# for (index, row) in hunters_data_frame.iterrows():
#     print(row)

for (index, row) in hunters_data_frame.iterrows():
    if row.power > 100:
        print(row.hunter)
