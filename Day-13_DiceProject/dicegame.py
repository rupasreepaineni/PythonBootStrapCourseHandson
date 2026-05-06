from  random import randint
dice_images =[1,2,3,4,5,6]
#****dice_num = randint(1,6) #here the list index starts from 0 and ends at 5,
# so when it's dice_num[6] it will give an error because there is no index 6 in the list,
#IndexError: list index out of range
dice_num = randint(0,5)

print(dice_images[dice_num])