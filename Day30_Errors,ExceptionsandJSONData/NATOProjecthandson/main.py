
import pandas
phonetic_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_phonetic_alphabets =  {row.letter:row.code for (index,row) in phonetic_alphabets.iterrows()}
print(dict_phonetic_alphabets)
def generate_phonetic():
    Name = input("Enter your name:").upper()
    k= []
    try:
        k = [dict_phonetic_alphabets[l] for l in Name]
    except KeyError:
        print("Sorry!,Enter only letters in alphabet format")
        generate_phonetic()
    else:
        # using list comprehension
        print(k)

generate_phonetic()