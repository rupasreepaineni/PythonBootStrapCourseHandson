
import random
alphabets =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
special_characters = ['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the PyPassword Generator!")
password_length = int(input("Enter the desired length of your password?\n:"))
alphabets_length = int(input("How many alphabets would you like in your password? \n"))
numbers_length = int(input("How many numbers would you like in your password? \n"))
special_characters_length = int(input("How many special characters would you like? \n "))



# easy
password = ""
for i in range(0,alphabets_length):
    password_alpha = random.choice(alphabets)
    password += password_alpha
for i in range(0,numbers_length ):
    password_num = random.choice(numbers)
    password += password_num

for i in range(0,special_characters_length ):
    password_spec = random.choice(special_characters)  #password + = random.choice(special_characters)
    password +=  password_spec
print(password)


# hard
password_list =[]
for i in range(0,alphabets_length):
    password_alpha = random.choice(alphabets)
    password_list += password_alpha
for i in range(0,numbers_length ):
    password_list += random.choice(numbers) # list also can be cancatened same as strings


for i in range(0,special_characters_length ):
    password_list += random.choice(special_characters)  #password + = random.choice(special_characters)

print(password_list)
#shuffled_password =[]
random.shuffle(password_list)
print(password_list)   # no need to create separate variable, it'll shuffle and assign to the same variable
# conversion of list to string
final_password=""
for char in password_list:
      final_password += char
print(f"Your generated password is:",final_password)


