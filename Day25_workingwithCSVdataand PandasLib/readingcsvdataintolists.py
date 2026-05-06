# l =[]
# with open("weather_data.csv") as f:
#     l = f.readlines()
#     print(l)


#there are predefined csv datahandling statements
import csv
with open("weather_data.csv") as n:
    l = csv.reader(n)
    print(l) # object has been created - l
    #we can iterate inorder to store in a list
    for row in l:
        print(row[1])

# import pandas
#
# data = pandas.read_csv("weather_data.csv") #skiprows=2 if any unwanted rows we've we can use that

# print(data)
# print(data["temp"])





