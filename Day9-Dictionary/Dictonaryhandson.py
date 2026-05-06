#defining a key if it's a string we should use "" or ""
#to add the values, stucent_grades={} - define the empty dictionary
# student_grades[scores] = "Outstanding"- then add the values to the dictionary


program = {
    "Hello" : "World",
    "Phrase" : "Tell me a word",
    "Ping": "a message"
}
print(program)

for dict in program:#Here it prints the keys only we're just fetching
    print(dict)

empty_dict ={} # empty dictionary
print(empty_dict) # we can add values if we want
empty_dict["Name"] = "Meenakshi"
print(empty_dict)

#updating the dict the existing values
program["Hello"] = "Everyone"
print(program)

