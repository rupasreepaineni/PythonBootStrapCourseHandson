final=[]
temp = [
    ['Monday', '12', 'Sunny'],
    ['Tuesday', '14', 'Rain'],
    ['Wednesday', '15', 'Rain'],
    ['Thursday', '14', 'Cloudy'],
    ['Friday', '21', 'Sunny']
]

# for temper in temp:
#     c =  temper[1]
#     final.append(c)
# print(final)

c = [] # Start with an empty list

for row in temp:
    middle_val = row[1] # Grab the '12', '14', etc.
    c.append(middle_val)
print(c)