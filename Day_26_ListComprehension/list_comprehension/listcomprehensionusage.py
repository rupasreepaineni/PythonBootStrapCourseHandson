# n = [1,2,3]
# k =[]
# for i in n:
#     j = i+1
#     k.append(j)
# print(k)


#syntax: new_list = [action for iteration_variable in list]
n = [1,2,3]
x = [m + 1 for m in n] # here "m" is variable to iterate for "n" list
print(x)

#list comprehension with string
c = "angela"
new = [l for l in c]
print(new)

#range(1,5)
ran = [x*2 for x in range(1,5)]
print(ran)

#names
names = ["sun","moon","king","queen","his","her"]
short_names = [sn for sn in names if len(sn)>3]
print(short_names)
short_names = [sn.upper() for sn in names if len(sn)>3]
print(short_names)