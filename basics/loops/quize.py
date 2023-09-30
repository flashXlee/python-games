# Define family list of your family members 
# Write a code , that loops over the list and print the following
# if family member is khalid OR sami print your are a programmer\
# otherwise print you are not a programmer

family = ["Khalid", "Sami", "He", "Hadi"]
for members in family:
    print ("Checking " + members + " ...")
    if  members=="Khalid" or members=="Sami":
        print("you are a programmer")
    else:
        print("you are not a programmer")