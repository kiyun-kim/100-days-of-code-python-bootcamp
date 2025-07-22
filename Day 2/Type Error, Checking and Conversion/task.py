# len("Hello")
#
# print(type("Hello"))
# print(type(123))
# print(type(3.14159))
# print(type(True))

# print(int("123") + int("456"))

# ValueError -> int("abc")
# TypeError

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) # str
print(type(length_of_name)) # int

print("Number of letters in your name: " + str(length_of_name))