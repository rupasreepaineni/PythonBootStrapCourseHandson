scores = [128,182,47,58,200,199,134,256,305,400,450]
print(sum(scores))

sum = 0
#indetail sum function
for i in scores:
    sum +=i
print(sum)
print(max(scores))

#indetail max function by using loops
max_score = 0
for j in scores:
   if j>max_score:
         max_score = j

print( max_score,"largest number")