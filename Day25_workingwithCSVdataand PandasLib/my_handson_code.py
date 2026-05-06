#converting data into DataFrame and few inbuilt functions and to csv
#we can tap to dataframe by - 1.data["temp"] 2.data.temp

import pandas

data = pandas.read_csv("weather_data.csv") #here data/name of the variable is called DataFrame[which holds the value]
#the first two lines are different like
# print(type(data))
# print(data["temp"])
#dataframe - helps to convert our data to any format
# data_dict = data.to_dict()
# print(data_dict)
#
# #extracting the data into a list - "series operation"
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# #calculating average of temp
# # c=0
# # for i in temp_list:
# #     c+=i
# # avg = c /len(temp_list)
# avg = sum(temp_list) /len(temp_list)
# print(avg)
# #with pandas
# print(data["temp"].mean())
# #to print maximum num
# print(data["temp"].max())
#
# #getting data from one column
# print(data["condition"])
# #or
# print(data.condition)


# #getting the row data
# print(data[data.day== "Monday"])
# #to find a row with max temp
# print(data[data.temp == data.temp.max()]) #here we're checking and assigning the data

#     tapping to a single value of a particular
# Monday = data[data.day == "Monday"]
# print(Monday.condition)
# Monday_temp_F= Monday.temp+32
# print(Monday_temp_F)

#Creating dataframe from stratch,
data_dict = {
    "students" : ["Angela","Yu","Jun"],
    "scores" : [76,54,12]
}
frame_creation = pandas.DataFrame(data_dict)
print(frame_creation)
#converting dataframe data to csv
frame_creation.to_csv("new_created.csv")