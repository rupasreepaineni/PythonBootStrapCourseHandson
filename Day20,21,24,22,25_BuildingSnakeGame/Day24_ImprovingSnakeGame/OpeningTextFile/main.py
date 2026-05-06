# simple way of opening a file
# file = open("normal.txt")
# contents = file.read() #contents is variable
# print(contents)
#
# #important to close the file as soon as we open it
# file.close()

#we can't reopen the same file again before it closes

#developers way of writing code
#with keyword makes file to close automatically
"""with open("normal.txt") as f:
    c = f.read()  #contents is variable
    print(c)
# * no need to close the file"""

#writing into the file
# 1. Append - modes "a", 2. clearing and inserting - mode "w" [the data with modes "a", "w"]
with open("normal.txt",mode = "a") as f:
    f.write("\n Gonna get a dream a job")

#clearning and inserting the data, creating new file ,
with open("new.txt",mode = "w") as f:
    f.write("Hello! This is Rupasree Paineni "
"\nLearning python from 1 week, within 5 weeks i pray and will work to complete whole training"
            "\n Gonna get a dream a job"
            "Getting 6 dream bangles as soon as i get pay ")


#check example of mailmerge handson for clear understanding
#** here we're just jumping back to the above folder and navigating to the required folder
with open("./Input/Names/invited_names.txt") as l:
    nam = l.readline().strip()
    print(nam)


with open("../Mail Merge Project Start/input/Letters/starting_letter.txt") as f:
    mail = f.readline()


#**** here we're ../-- navigating to the root folder and moving to the required folder
