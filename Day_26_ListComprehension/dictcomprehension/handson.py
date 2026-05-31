import random
import pandas
#here we're randomly generating the marks for list of names
# names = ["sun","moon","king","queen","his","her"]
# #d = {newkey:new_value for student in names} #syntax
# d = {student:random.randint(1,100) for student in names} #dict comprehension looping through list
# print(d)
#
# passed_students = {student:marks for (student,marks) in d.items() if marks>50 }
# print(passed_students)

#making dict into the Dataframe format
# *** pandas can't deal with the single value, they needs to be passed as a list/something grouped data
# you might be trying to save a single state's data.
# student_annual_scores = {
#     "Rahul": 68,
# "Riah": 78,
# "Ramu": 88
#}
student_annual_scores = { "students" : [ "Rahul","Riah","Ramu"], "scores": [68,78,98]
}

student_dict_frame = pandas.DataFrame(student_annual_scores)
#print(student_dict_frame)

#looping through data frame
# for (key,value) in student_dict_frame.items():
#     print(key) #prints only labels
#     print(value)


#Loops through rows of dataframe
for (index,row) in student_dict_frame.iterrows():
    #print(index) #this just prints index
    #print(row) #takes each row,#*actually row are panda series objects
    #print(row.students)
    #print(row.scores)
    if row.scores >=45:
        print(row.students)
        print(row.scores)

