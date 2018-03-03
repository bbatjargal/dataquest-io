## 2. Array Comparisons ##

print(world_alcohol)
print(world_alcohol[:, 2])
countries_canada = world_alcohol[:, 2] == "Canada"
years_1984 = world_alcohol[:,0] == '1984'

## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:, 2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria]

## 4. Comparisons with Multiple Conditions ##

row_1986 = world_alcohol[:, 0] == '1986'
row_algeria = world_alcohol[:, 2] == 'Algeria'
is_algeria_and_1986 = row_1986 & row_algeria
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986]

## 5. Replacing Values ##


matrix = numpy.array([
            [5, 10, 15], 
            [20, 25, 30],
            [35, 40, 45]
         ])
second_column_25 = matrix[:,1] == 25
matrix[:,1][second_column_25] = 10
    
world_alcohol[world_alcohol[:,0] == '1986', 0] = '2014'
world_alcohol[world_alcohol[:,3] == 'Wine', 3] = 'Grog'

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4]==''
world_alcohol[is_value_empty, 4] = 0

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption= alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = numpy.sum(alcohol_consumption)
average_alcohol = numpy.mean(alcohol_consumption)

## 9. Total Annual Alcohol Consumption ##

canada_and_1986 = (world_alcohol[:,0]=='1986') & (world_alcohol[:,2]=='Canada')
canada_1986 = world_alcohol[canada_and_1986 ]
canada_1986[:, 4][canada_1986[:,4] == ''] = 0
canada_alcohol = canada_1986[:,4].astype(float)
total_canadian_drinking = numpy.sum(canada_alcohol)

## 10. Calculating Consumption for Each Country ##

totals = {}
countries = world_alcohol[:,2]
for country in countries:
    country_and_1989 = (world_alcohol[:, 0] == '1989') & (world_alcohol[:,2]==country)
    particular_country = world_alcohol[ country_and_1989 ]
    particular_country[ particular_country[:, 4] == '', 4] = 0
    totals[country] = numpy.sum(particular_country[:,4].astype(float))


## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for key in totals:
    if totals[key] > highest_value:
        highest_value = totals[key]
        highest_key = key