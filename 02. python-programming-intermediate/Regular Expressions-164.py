## 1. Introduction ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Wildcards in Regular Expressions ##

strings = ["bat", "robotics", "megabyte"]
regex = "b.t"

## 3. Searching the Beginnings And Endings Of Strings ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b....r"

## 5. Reading and Printing the Data Set ##

import csv

f = open("askreddit_2015.csv", "r")
posts_with_header = list(csv.reader(f))
posts = posts_with_header[1:]
for index, post in enumerate(posts):
    if index > 9:
        break
    print(post)


## 6. Counting Simple Matches in the Data Set with re() ##

import re

of_reddit_count = 0
for row in posts:
    if re.search("of Reddit", str(row)) is not None:
        of_reddit_count +=1
print(of_reddit_count)

## 7. Using Square Brackets to Match Multiple Characters ##

import re
of_reddit_count  = 0
for row in posts:
    if re.search("of [Rr]eddit", row[0]) is not None:
        of_reddit_count +=1
print(of_reddit_count)    

## 8. Escaping Special Characters ##

import re
serious_count = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count +=1
print(serious_count)        

## 9. Combining Escaped Characters and Multiple Matches ##

import re
serious_count = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count +=1
print(serious_count)        

## 10. Adding More Complexity to Your Regular Expression ##

import re
serious_count = 0
for row in posts:
    if re.search("[\(\[][Ss]erious[\]\)]", row[0]) is not None:
        serious_count +=1
print(serious_count)       

## 11. Combining Multiple Regular Expressions ##

import re
serious_start_count = 0
serious_end_count = 0
serious_count_final = 0
for row in posts:
    if re.search("^[\[\(][Ss]erious[\)\]]", row[0]) is not None:
        serious_start_count +=1
    if re.search("[\[\(][Ss]erious[\)\]]$", row[0]) is not None:
        serious_end_count +=1
    if re.search("^[\[\(][Ss]erious[\)\]]|[\[\(][Ss]erious[\)\]]$", row[0]) is not None:
        serious_count_final +=1
print(serious_start_count)
print(serious_end_count)
print(serious_count_final)

## 12. Using Regular Expressions to Substitute Strings ##

import re
for row in posts:
    row[0] = re.sub("[\[\(][Ss]erious[\)\]]", "[Serious]", row[0])

## 13. Matching Years with Regular Expressions ##

import re
year_strings = []
for row in strings:
    year = re.search("[12][0-9][0-9][0-9]", row)
    if year is not None:
        year_strings.append(row)
print(str(year_strings))        

## 14. Repeating Characters in Regular Expressions ##

import re
year_strings = []
for row in strings:
    if re.search("[12][0-9]{3}", row) is not None:
        year_strings.append(row)


## 15. Challenge: Extracting all Years ##

import re
years = re.findall("[12][0-9]{3}", years_string)
print(years_string)
print(str(years))