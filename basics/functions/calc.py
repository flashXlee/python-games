# greetings I am Calc. Below is code. please do not delete or add anything.
# press control then the symbol next to the one. it will open terminal.
# click the up arrow and press enter to begin.
# if it doesn't work, type this.
#python '/Users/sami/code/python-games/basics/functions/calc.py'

def add (n1,n2):
    return n1+n2

def sub (n1,n2):
    return n1-n2

def divide (n1,n2):
    return n1/n2

def multiply (n1,n2):
    return n1*n2

print("I can add, divde, or  subtract two numbers for you. Would you like to add or subtract? ")
think = input("Write add,divide or subtract in the text box(you can write sub to subtract) ")
if think == "add": 
    answer = input("Ok, give me the first number: ")
    answer_2 = input("Give me the second number: ")
    result = add(int(answer),int(answer_2))
    print(result)
elif think == "sub" or "subtract":
    answer_1 = input("Ok, give me the first number: ")
    answer2= input("Give me the second number: ")
    result = sub (int(answer_1),int(answer2))
    print(result)
elif think == "divide":
    answer1 = input("Ok, give me the first number: ")
    answer2 = input("Give me the second number: ")
    result = divide(int(answer1),int(answer2))
    print(result)

elif think == "multiply":
    answer = input("Ok, give me the first number: ")
    answer3 = input("Give me the second number: ")
    result = multiply(int(answer),int(answer3))
    print(result)
else: print("bye annoying guy")

# thank you for using me :)