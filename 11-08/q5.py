a_str = input("Enter the 1st Number: ")
b_str = input("Enter the 2nd number: ")

a = float (a_str)
b = float (b_str)

# add = (a+b)
# sub = (a-b)
# multi = (a*b)
# div = (a/b)

print("Addition: ", a+b)
# print("Subtraction: ", sub)
# print("Multiplication: ", multi)
# print("Division: ", div)


# The print() statements are updated to use f-strings (formatted string literals). 
# This is a modern and clean way to embed variables directly into a string. 
# The syntax is f"some text {variable} some more text".