'''
Lists are basically an ordered way of grouping things (called elements) - the cool thing about lists
 in Python is that you can have a list that contains objects of multiple types.
 Your list can mix between strings, integers, objects, other lists, what have you.

topics:
Lists
More conditionals (if statements)

Take a list, say for example this one:

  my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5
'''

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in my_list:
    if(element<5):
        print(element)


# More Conditionals(finding Grades)

grade = int(input("Enter your numerical Grade : "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >=70:
    print("C")
elif grade >= 65:
    print("D")
else:
    print("F")
    



