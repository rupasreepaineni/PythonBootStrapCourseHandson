#.title() function helps to call the outputs in title case
#we can output by returning the final value in the function
#the function call will be stored to a variable inorder to catch the output

def name(f_name,l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name+ l_name  #
final = name("sneha","kumar") # storing the output in a variable
print(final)

def function_1(text1,text2):
   text = text1+text2
   return text

def function_2(tex):
    txt = tex.title()
    print(txt)
one_value = function_1("hello","world")
function_2(one_value)
function_2(function_1("hello", "world"))