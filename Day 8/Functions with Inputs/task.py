# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")
#
# greet()
#
# # Functions than allows for inputs
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
# greet_with_name("Kiyun")

# Funtions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")
greet_with("Nowhere", "Jack Bauer")
greet_with(location="Korea", name="Kiyun")