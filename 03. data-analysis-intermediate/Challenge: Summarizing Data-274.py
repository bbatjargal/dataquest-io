## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages[:5])
print(recent_grads[:5])

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

major_categories = all_ages['Major_category'].unique()


aa_cat_counts = dict()
rg_cat_counts = dict()

for category in major_categories:
    data_category = all_ages[all_ages['Major_category']==category]
    aa_cat_counts[category] = data_category["Total"].sum()
    
    data_category = recent_grads[recent_grads['Major_category']==category]
    rg_cat_counts[category] = data_category["Total"].sum()

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0

sum_low_wage_jobs = recent_grads["Low_wage_jobs"].sum()
total = recent_grads["Total"].sum()

low_wage_proportion = sum_low_wage_jobs / total 
print(low_wage_proportion)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for major in majors:
    all_ages_major = all_ages[all_ages["Major"] == major]
    recent_grads_major = recent_grads[recent_grads["Major"] == major]
    
    all_ages_rate = all_ages_major["Unemployment_rate"]
    recent_grads_rate = recent_grads_major["Unemployment_rate"]
    
    if  float(recent_grads_rate) < float(all_ages_rate):
        rg_lower_count += 1
        
print(rg_lower_count)