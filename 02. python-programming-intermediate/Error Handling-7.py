## 2. Sets ##

import csv

f = open("legislators.csv")
data = list(csv.reader(f))[1:]

gender = []
for row in data:
    gender.append(row[3])
    
gender = set(gender)
print(gender)
    

## 3. Exploring the Dataset ##

import csv

f = open("legislators.csv")
legislators = list(csv.reader(f))[1:]
party = []
for row in legislators:
    party.append(row[6])
party = set(party)
print(party)
print(legislators)

## 4. Missing Values ##

import csv

f = open("legislators.csv")
legislators = list(csv.reader(f))[1:]
for legislator in legislators:
    if legislator[3] == "":
        legislator[3] = "M"
        

## 5. Parsing Birth Years ##

import csv

f = open("legislators.csv")
data = list(csv.reader(f))[1:]
birth_years = []
for row in data:
    parts = row[2].split("-")
    birth_years.append(parts[0])

    

## 6. Try/except Blocks ##

try:
    float("hello")
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##

try:
    int("")
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

import csv
f = open("legislators.csv")
data = list(csv.reader(f))[1:]
converted_years = []
for row in data:
    try:
        parts = row[2].split("-")
        converted_years.append(int(parts[0]))
    except Exception:
        converted_years.append("")
        pass

## 9. Convert Birth Years to Integers ##

for row in legislators:
    try:
        birth_year = int(row[2].split("-")[0])
    except Exception:
        birth_year = 0
    row.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]