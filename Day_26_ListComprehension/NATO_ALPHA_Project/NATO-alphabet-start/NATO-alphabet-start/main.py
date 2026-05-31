student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    print(value)


import pandas
student_data_frame = pandas.DataFrame(student_dict)
#hints
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
phonetic_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(phonetic_alphabets)
dict_phonetic_alphabets =  {row.letter:row.code for (index,row) in phonetic_alphabets.iterrows()}
#here it iterates over the index of each row, and we're fteching the row data w.r.t letter ad code
print(dict_phonetic_alphabets)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
Name = input("Enter your name:").upper()
k= []
# for l in Name:
#     k.append(dict_phonetic_alphabets[l])
# print(k)

# using list comprehension
k = [dict_phonetic_alphabets[l] for l in Name]
print(k)