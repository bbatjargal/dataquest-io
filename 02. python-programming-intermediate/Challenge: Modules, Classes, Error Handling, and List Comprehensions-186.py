## 2. Introduction to the Data ##

import csv
f = open("nfl_suspensions_data.csv")
nfl_suspensions = list(csv.reader(f))
header = nfl_suspensions[:1][0]
nfl_suspensions = nfl_suspensions[1:]
years = {}
year_index = None
for index, column in enumerate(header):
    if column == "year":
        year_index = index
if year_index is not None:
    for row in nfl_suspensions:
        year = row[year_index]
        if year in years:
            years[year] = years[year] + 1
        else:
            years[year] = 1
print(years)
    
    
    

## 3. Unique Values ##

import csv
class NflSuspension:
    def __init__(self, data):
        self.header = data[:1][0]
        self.data = data[1:]
    
    def getColumnIndex(self, name):  
        column_index = [ index for index, column in enumerate(self.header) if column == name ]
        if len(column_index) > 0:
            return column_index[0]
        return None

    def getUniqueList(self, name):
        unique_list = []
        column_index = self.getColumnIndex(name)      
        if column_index is not None:
            unique_list = [ row[column_index] for row in self.data ]
            
        return set(unique_list)
   
f = open("nfl_suspensions_data.csv") 
nfl_suspension = NflSuspension(list(csv.reader(f)))
unique_teams = nfl_suspension.getUniqueList("team")
unique_games = nfl_suspension.getUniqueList("games")
 

## 4. Suspension Class ##

class Suspension:
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]
    def __str__(self):
        return self.name
third_suspension = Suspension(nfl_suspensions[2])
print(third_suspension)

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0

    def get_year(self):
        return self.year

missing_year = Suspension(nfl_suspensions[22])    
twenty_third_year = missing_year.get_year()