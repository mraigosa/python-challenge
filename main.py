import glob
import csv
from collections import Counter

# Interate through directory files
filepaths = glob.glob('raw_data/*.csv')

# Create a list to hold all csv data
all_csv_data = []

# Read each csv file and append the contents to the all_csv_data list
for file in filepaths:
    with open(file, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvdata = list(csvreader)
        all_csv_data.extend(csvdata[1:])

# Write the merged data to a new file
csvpath ="merged_records.csv"
with open(csvpath, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Date", "Revenue"])
    csvwriter.writerows(all_csv_data)

#Define lists to store data
date = [] 
revenue = []

#Iterate through csv file to create date and revenue lists
for row in all_csv_data:

    #Add to date lists
    date.append(row[0])

    #Add to revenue lists
    revenue.append(row[1])

#Convert revenue list from str to int to revenue_int table
revenue_int = [int(x) for x in revenue]

#Calculate sum of revenue integer table
revenue_sum = sum(revenue_int)

#Define lists to hold cleaned date lists 
cleaned_date = []

#Iterate through original date list and conform date in new cleaned date list
for row in date:
    if row[0:3] == "Jan":
        new_date = row[-2:] + "-01"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "Feb":
        new_date = row[-2:] + "-02"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "Mar":
        new_date = row[-2:] + "-03"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "Apr":
        new_date = row[-2:] + "-04"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "May":
        new_date = row[-2:] + "-05"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "Jun":
        new_date = row[-2:] + "-06"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "Jul":
        new_date = row[-2:] + "-07"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "Aug":
        new_date = row[-2:] + "-08"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "Sep":
        new_date = row[-2:] + "-09"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "Oct":
        new_date = row[-2:] + "-10"
        cleaned_date.append(new_date[0:8])
    elif row[0:3] == "Nov":
        new_date = row[-2:] + "-11"
        cleaned_date.append(new_date[0:8])
    else:
        new_date = row[-2:] + "-12"
        cleaned_date.append(new_date[0:8])
        
#Combine cleaned date and revenue list into dictionary
dictionary = dict(zip(cleaned_date, revenue))   
#for i in dictionary.items():
#    print(i)

#dictionary = {str(k):int(v) for k,v in dictonary.items()}
#Identify maximum value
max_value = max(dictionary.values())
min_value = min(dictionary.values())

#Get key for maximum value
max_keys = [k for k, v in dictionary.items() if v == max_value]
min_keys = [k for k, v in dictionary.items() if v == min_value]

#average_value = sum(d['value'] for d in dictionary) / len(dictionary)

unique_dates = set(cleaned_date)
unique_dates_count = len(unique_dates)

print('Financial Analysis')
print('-----------------------------------------')   
print ("Total months: " + str(unique_dates_count))
print ("Total Revenue: " + str(revenue_sum))
print ("Greatest increase in revenue: " + str(max_keys) + " " + str(max_value))
print ("Greatest decrease in revenue: " + str(min_keys) + " " + str(min_value))