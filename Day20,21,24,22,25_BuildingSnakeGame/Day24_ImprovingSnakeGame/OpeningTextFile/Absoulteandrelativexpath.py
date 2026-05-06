#Absolute - root
#Relative - current path

#opening file through absolute xpath

with open(r"C:\Users\Chandupraveen Gudi\OneDrive\Desktop\normal.txt",mode = "a") as f:
    f.write("\n Gonna get a dream a job")


# below code doesn't work because it treats it as unicodeescape, to make it work
# we need add "r" which meant RawString
# with open("\Users\Chandupraveen Gudi\OneDrive\Desktop\normal.txt",mode = "a") as f:
#     f.write("\n Gonna get a dream a job")


#Relative xpath
#.\Day24_ImprovingSnakeGame\canvasandbuttonsstep1.py
#C:\Users\Chandupraveen Gudi\PycharmProjects\PythonProject1\Pythondaily\Day20,21,24,22,25_BuildingSnakeGame\Day24_ImprovingSnakeGame
with open(r"./new.txt",mode = "a") as f:
    f.write("\n Gonna get a dream a job")

# 1. if in the same file - directly write file name
# if txt file, is any level above ../


