# Unit 1 activity
# Author: Bryant Chan
# March 4, 2024

# The purpose of this python code is to calculate the area of rectangles

def rectangle_area(length, width):
    return (length * width)

length = float(input("What is the length of the rectangle?"))  # 80.0
width = float(input("What is the width of the rectangle?"))

area = rectangle_area(length, width)

print(f"The area of the rectangle is {area}")

if area > 1000:
    print("The area of this rectangle is greater than 1000")
else:
    print("The area is not greater than 1000.")