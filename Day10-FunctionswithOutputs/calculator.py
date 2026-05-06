def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

#adding a dictionary to store the operations
operators ={"+": add ,
            "-": subtract,
            "*":multiply,
            "/":divide} #here we're just storing the names, not intiliazing functions'

#perform the operation to multiply 4*8 by using above dictionary
#print(operators["*"](4,8))
print(operators.keys())

def Calculator():
    should_accumlate = True
    num1 = float(input("Enter the first number: "))
    while should_accumlate:
        for symbol in operators:  # extracting the keys from the dictionary to print the symbols
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?"))
        answer = {operators[symbol](num1,num2)}
        print(f" {num1} {operation} {num2} = {answer}")  # call the dictionary and perform the operation

        choice = input(f"Type 'Y' to continue calculating with {answer} , or type 'n' to start new calculation ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumlate = False
            print("\n"*20)
            Calculator()



Calculator()