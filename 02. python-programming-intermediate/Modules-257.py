## 1. Introduction to Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)

print(root)
print(flr)

## 2. Importing Using An Alias ##

import math as m
root = math.sqrt(33)
print(root)

## 3. Importing A Specific Object ##

from math import *
root = sqrt(1001)
print(root)

## 4. Variables Within Modules ##

import math
pi = math.pi
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)

print(pi, a, b, c, end=" ")

## 5. The CSV Module ##

import csv
f = open("nfl.csv")
reader = csv.reader(f)
nfl = list(reader)
print(nfl)

#print(f)
#data = f.read()
#print(data)
#rows = data.split("\n")
#for row in rows:
#    print(row)

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv")
patriots_wins = 0
rows = list(csv.reader(f))
for row in rows:
    if row[2] == "New England Patriots":
        patriots_wins+=1
print(patriots_wins)

## 7. Making a Function that Counts Wins ##

import csv
f = open("nfl.csv")
nfl = list(csv.reader(f))

def nfl_wins(teamname, rows):
    count = 0
    for row in rows:
        if row[2] == teamname:
            count +=1
    return count

cowboys_wins = nfl_wins("Dallas Cowboys", nfl)
falcons_wins = nfl_wins("Atlanta Falcons", nfl)
