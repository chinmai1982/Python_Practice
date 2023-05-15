#String Manipulation
name = input("Enter your Name Here : ")
print("Your Name is :" + name)
age = int(input("Enter your Age Here:"))
print(age)
print("Door" + "Closed")
print(4 * "Apple")
print("6" + "Oranges")

sal = 20000.39
print(sal)

'''
Strings are lists
Because strings are lists, you can do to strings everything that you do to lists. You can iterate through them:
'''

S = "Chinmai Sutar"
for str in S:
    print("The letter is : " + str)

string = S[2:7]
print(string)

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = []
for year in years_of_birth: 
    ages.append(2014 - year)
print(ages)
