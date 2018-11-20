# Input name and print odd characters
name = input("Enter name:")

# Check that the name is not blank
while len(name)<=0:
    print("Name is blank, enter again")
    name = input("Enter name")

# print odd characters in name
print(name[::2])

