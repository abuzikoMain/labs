# import json
# import urllib.request
# with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users') as f:
#     print(f"{json.loads(f.read())}")

import csv
with open('annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv', 'r') as f:
  reader = csv.reader(f)
  cnt = 0
  total_income = 0
  for row in reader:
    cnt +=1
    if row[4] == 'Total income':
      total_income += float(row[5])
    # print(f'{row}\n')
    if cnt == 100:
      break
print(total_income)