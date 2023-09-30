# def greetings(name,age):
#     result = int(age) + 1
#     print("Hello " + name + " you are " + str(result) + " next year")

# answer = input("what is your name? ")
# age = input("how old are you? ")

# greetings(answer,age)


def greetings(name,year_born):
    age = 2023 - int(year_born)
    next_year = age + 1 
   
    print("Hello, " + name + " you are " + str(age) + " years old")
    print(name + " you will be " + str(next_year) + " next year" )

answer = input("what is your name? ")
year = input("When were you born? ")

greetings(answer,year)