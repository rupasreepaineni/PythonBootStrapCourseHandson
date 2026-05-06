# Random numbers we can use random.randint() to generate random integers within a specified range.
#random.random() generates a random float between 0.0 and 1.0., to generate random float between two values we can use random.uniform(a,b)
#first one refers to (random) to module, whereas second one refers to (random()) function
#random.uniform(a,b) generates a random float between a and b., like a<N<b,like floating values
import random

#random_integer = random.randint(1,10)
#print(random_integer)

#random_flo = random.random() # it'll not take any values as input, it'll not generate 0/1, only float values
#print(random_flo)

#value = random.uniform(10,20) # it'll generate float values between the given range
#print(value)

#based on 0/1 generate heads/tails
heads_or_tails = random.randint(0,1)
print(heads_or_tails )
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
