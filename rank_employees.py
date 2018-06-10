from firebase import firebase
import json
from correlation import calc_correlation
import sys

if len(sys.argv) != 2:
    print("Usage is python rank_employees <task-requirement>")

firebase = firebase.FirebaseApplication(FIREBASE_DIR, None)

employees = []

result = firebase.get('/employees', None)

for key in result:
    employees.append(result[key])

ratings = []

search_string = sys.argv[1]

correlation = calc_correlation(search_string, 10)

for ee in employees:
    rating = 0
    for lang in ee["skills"].keys():
        rating += correlation[lang] * ee["skills"][lang]

    ratings.append(tuple((rating, ee["name"])))

ratings.sort(reverse = True)

print("Name       - Rating")
for rating, name in ratings:
    print("{:10s} - {:2.2f}".format(name, rating))
