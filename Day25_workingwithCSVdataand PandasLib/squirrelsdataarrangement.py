#it deals with the different colour squirrels count
#steps involved:
#read the data and use count function and do it

import pandas
#read the file and store it
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data["Primary Fur Color"])
#here we've to get the count of Nan,Cinnamon,Gray
Fur_Color =data["Primary Fur Color"].value_counts()
#other way to create Dataframe
final_frame = Fur_Color.to_frame(name = "Count")
print(final_frame)
final_frame.to_csv("squirreldata.csv") #in this code there won't be index we can add by another line of code


# or code by course, which have index
import pandas
# read the file and store it
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data["Primary Fur Color"] == "Gray")
Nan_squirrels = len(data["Primary Fur Color"] == "Nan")
Cinnamon_squirrels = len(data["Primary Fur Color"] == "Cinnamon")

frame = {
    "Fur Colour" : ["grey_squirrels","Nan_squirrels","Cinnamon_squirrels"],
    "Count" : [grey_squirrels, Nan_squirrels, Cinnamon_squirrels]
}
dict = pandas.DataFrame(frame)
dict.to_csv("squirrelsdata.csv")

