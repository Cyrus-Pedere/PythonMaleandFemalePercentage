#   Cyrus Jayson A. Pedere
#   Bscpe 1-1 Programming Logic and Design
#   FSw1 Module 2: Input, Processing, and Output
# 
#   **** 1. Male and Female Percentages *****
#         PYTHON LANGUAGE


male = int(input("How many males are in the class?"))
female = int(input("How many females are in the class?"))

classTotal = male + female 
percentage = 100

malePercentage = (male*percentage)/classTotal
femalePercentage = (female*percentage)/classTotal

print("The total number of students registered in the class is: ", classTotal, "and the percentage for the male is ", malePercentage, "&.", "for the female is ", femalePercentage, "&.")

