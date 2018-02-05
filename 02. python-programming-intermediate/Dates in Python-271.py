## 1. The Time Module ##

import time

current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
print(current_hour)
print(current_struct_time.tm_year)
print(current_struct_time.tm_mon)
print(current_struct_time.tm_mday)
print(current_struct_time.tm_hour)
print(current_struct_time.tm_min)

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.utcnow()
current_year = current_datetime.year
current_month = current_datetime.month
print(datetime.datetime.utcnow())


## 4. Timedelta ##

import datetime
kirks_birthday = datetime.datetime(year=2233, month=3, day=22)
diff = datetime.timedelta(weeks=15)
before_kirk = kirks_birthday - diff
print(before_kirk)

## 5. Formatting Dates ##

import datetime
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime

mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(mystery_date_2)

## 8. Reformatting Our Data ##

import datetime

for row in posts:
    row[2] = datetime.datetime.fromtimestamp(float(row[2]))

## 9. Counting Posts from March ##

import datetime
march_count = 0
for row in posts:
    if row[2].month == 3:
        march_count +=1
print(march_count)        

## 10. Counting Posts from Any Month ##

def countPostsInMonth(month, data):
    count = 0
    for row in data:
        if row[2].month == month:
            count +=1
    return count

feb_count = countPostsInMonth(2, posts)
aug_count = countPostsInMonth(8, posts)