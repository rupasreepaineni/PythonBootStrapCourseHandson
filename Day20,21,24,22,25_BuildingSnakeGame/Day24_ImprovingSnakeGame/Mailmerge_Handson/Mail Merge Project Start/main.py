

with open(f"./Output/ReadyToSend/example.txt") as x:
    #reading the example context which needs to be printed
    content = x.read()

with open("./Input/Names/invited_names.txt") as l:
    for names in l:
        #nam = l.readline().strip(), this is general mistake,
        # asking to skip the line readline - makes to move to next line
        nam = names.strip() #here it reads the line
        with open(f"./Output/ReadyToSend/letter_for_{nam}.txt", "w") as y:
            final_letter = content.replace("name", nam)
            y.write(final_letter)  # this helps file to open and write into it