import json
import urllib.request
import csv

#Task 1
print('Task 1')
with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users') as f:
    lst = json.loads(f.read())
for each in lst:
    print(f'Name: {each['name']} | City: {each['address']['city']} | Phone: {each['phone']}')


#Task 2
print('Task 2')
with open('annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)

with open('annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv', 'r', encoding='utf-8-sig') as f:
  reader = csv.DictReader(f)
  for row in reader:
    print(row)

# #Task 3
print('Task 3')

with open('annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv', 'r') as f:
  reader = csv.reader(f)
  cnt = 1
  total_income = 0
  for row in reader:
    cnt +=1
    if row[4] == 'Total income':
      print(cnt)
      
      total_income += float(row[5])

  print(total_income)


with open('annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv', 'r') as f:
  reader = csv.DictReader(f)
  total_income = 0
  for row in reader:
     if row['variable'] == 'Total income':
      inc = row['value']
      total_income += int(inc)

print(total_income)

#Task 4
print('Task 4')
jsons = []
with open('annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv', 'r', encoding='utf-8-sig') as f:
  temp_d = {}
  reader = csv.DictReader(f)
  headers = reader.fieldnames
  for row in reader:
    for header in headers:
      temp_d.update({header: row[header]})
    jsons.append(temp_d)
    temp_d = {}
  
print(jsons)

