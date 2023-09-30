# Create program that ask the user to enter two numbers (n1, n2),
# the program need to ask twice, for example, give me number 1 and then give me number 2
# then the 
# program add those numbers and return the result, then print it out
# remember (input rerturns string, you need to cast it to int)
def add (n1,n2):
    return n1+n2

print("I can add two numbers for you")
answer = input("give me the first number: ")
answer_2 = input("give me the second number: ")
result = add(int(answer),int(answer_2))
print(result)
