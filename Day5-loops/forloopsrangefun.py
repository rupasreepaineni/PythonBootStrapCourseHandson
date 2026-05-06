#instead of creating lists and using for loop on lists we can use range function to generate a sequence of numbers
#RANge should be used in conjunction of another functions like for,if loops
#(a,b+1) , (a,b,c)-- c is the step count
#while loop should be used when we dont know the number of iterations but for loop should be used when we know the number of iterations
#while is only based on condition but for loop is based on sequence of numbers, true,not true like that

for i in range(1,11):
    print(i)

for j in range(1,11,3):
    print(j)

#sum of first 100 natural numbers
sum=0
for i in range(1,101):
    sum+=i
print("sum of first 100 natural numbers is:",sum)