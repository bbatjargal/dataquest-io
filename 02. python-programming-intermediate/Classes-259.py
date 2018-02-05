## 2. Defining the Dataset Class ##

class Dataset:
    def __init__(self):
        self.type = "csv"
        
dataset = Dataset()

print(dataset.type)

## 3. Passing Additional Arguments to the Initializer ##

import csv

class Dataset:
    def __init__(self, data):
        self.data = data
        
f = open("nfl.csv")
nfl_data = list(csv.reader(f))

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data
    

## 4. Adding Additional Behavior ##

import csv
class Dataset:
    def __init__(self, data):
        self.data = data
    
    def print_data(self, num_rows):
        print(self.data[:num_rows])
        
f = open("nfl.csv")
nfl_data = list(csv.reader(f))

dataset = Dataset(nfl_data)
dataset.print_data(5)


## 5. Enhancing the Initializer ##

import csv
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
f = open("nfl.csv")
nfl_data = list(csv.reader(f))

dataset = Dataset(nfl_data)
nfl_header = dataset.header
print(nfl_header[0])


## 6. Grabbing Column Data ##

import csv
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        column_data = None
        column_index = None
        
        for idx, value in enumerate(self.header):
            if value == label:
                column_index = idx
                column_data = []
                break
        if column_index is not None:
            for row in self.data:
                column_data.append(row[column_index])
        return column_data
                                
f = open("nfl.csv")
nfl_data = list(csv.reader(f))
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')

## 7. Count Unique Method ##

import csv

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    def column(self, label):
        if label not in self.header:
            return None
        
        index = None
        column_data = None
        for idx, value in enumerate(self.header):
            if label == value:
                index = idx
                column_data = []
                break
        
        if index is not None:
            for row in self.data:
                column_data.append(row[index])
                
        
        return column_data
    
    def count_unique(self, label):
        column_data = self.column(label)
        if column_data is None:
            return 0
        
        unique_data = set(column_data)
        return len(unique_data)
    
f = open("nfl.csv")
nfl_data = list(csv.reader(f))
dataset = Dataset(nfl_data)
total_years = dataset.count_unique("year")   
print(total_years)

## 8. Make Objects Human Readable ##

import csv

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    def __str__(self):
        return str(self.data[:10])

f = open("nfl.csv")
nfl_data = list(csv.reader(f))
nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)