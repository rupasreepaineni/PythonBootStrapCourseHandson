#list is data structure in python that is used to store multiple items in a single variable.
#Lists are ordered, changeable, and allow duplicate values.
#Lists are created using square brackets [] and items are separated by commas.

#usage of random w.r.t list
#index out of range is nothing but exceeding the limit of index in a list

#a =["apple","banana","cherry"]
#print(a)
#accessing items
#print(a[1])
#print(a[-1])
#a.append("promogranate") #add item to the end of the list
#print(a)
#a.insert(1,"orange") #insert item at specified index
#print(a)

#who pays the bill
friends = ["Radha","Shyam", "Singha","Roy","Chandra"]
count = len(friends)
print(count)
import random
rand_number = random.randint(1,count)
print(friends[rand_number-1] + " is going to pay the bill")

#or ******
payer = random.choice(friends)   # random.choice() takes the sequences as a function
print(payer + " is going to pay the bill")