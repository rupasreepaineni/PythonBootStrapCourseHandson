#FileNotFoundError
try:
    file = open("handson.txt")
    # a_dict = {"key":"value"}
    # print(a_dict["dhgfhjf"])
# except : # this eradicates complete error
#     file = open("handson.txt", "w")
#     file.write("something")
except FileNotFoundError: #this works only file errors
    file = open("handson.txt", "w")
    file.write("something")
# except KeyError:
#     print("Key doesn't exists")

#if we want to store the message then
# except KeyError as error_message:
#     print(f"The Key {error_message}doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    print("Hello dear")
    file.close()