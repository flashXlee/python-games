# greetings I am Calc. Below is code. please do not delete or add anything.
# press control then the symbol next to the one. it will open terminal.
# click the up arrow and press enter to begin.
# if it doesn't work, type this.
#python '/Users/sami/code/python-games/basics/functions/calc.py'

def add (n1,n2):
    return n1+n2

def sub (n1,n2):
    return n1-n2


print("I can add or subtract two numbers for you. Would you like to add or subtract? ")
think = input("Write add or subtract in the text boxS(you can write sub to subtract) ")

num1 = int(input("Ok, give me the first number: "))
num2 = int(input("Give me the second number: "))
result = 0

if think == "add": 
    result = add(num1,num2)
elif think == "sub" or "subtract":
    result = sub (num1,num2)
    
print(result)
print("bye annoying guy")