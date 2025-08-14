# Write a Python program to find the area and perimeter of a rectangle 
# when the length and breadth are given as input

length_s = input("Enter the length of the rectangle : ")
breadth_s = input("Enter the breadth of the rectangle : ")

length = float(length_s)
breadth = float(breadth_s)

area = length * breadth
perimeter = 2 * (length + breadth)

print("The Area of the given rectangle is :", area)
print("The perimeter of the given rectangle is :", perimeter)