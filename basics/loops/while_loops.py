answer = input("Shall I throw a water balloon? (yes/no)")
count = 0

while answer == "yes" or answer == "y"or answer == "sure":
    print("SPALSHHH!!!")
    count = count +1
    answer = input("Want to do it again? (yes/no)")
print("I have thrown " + str(count) + " ballons")
print("Bye Bye")