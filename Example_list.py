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
    
'''There is an easy way to programmatically create lists of numbers in Python.

To create a list of numbers from 2 to 10, just use the following code:
'''
x = range(2, 11)

'''Then the variable x will contain the list [2, 3, 4, 5, 6, 7, 8, 9, 10]. Note that the second number in the
   range() function is not included in the original list.
   Now that x is a list of numbers, the same for loop can be used with the list:
'''

for element in x:
    print(element)

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num1 = int(input("Enter the Number Here to find the Divisors : "))
numdivisors = []

for num in list(range(1,num1+1)):
    if num1 % num == 0 :
        numdivisors.append(num)
print(numdivisors)        

