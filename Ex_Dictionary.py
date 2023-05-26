'''
Dictionary is an order collection of key-value pairs enclosed within {}
Dictionary is mutable
'''
fruits = {'apple':30,'banana':40,'Orange':50,'Grapes':60}
print(fruits.keys())
print(fruits.values())
print(fruits.items())
fruits['apple']=100

fruits['Mango']=70
print(fruits.items())

fruits1 = {'apple':30,'banana':40,'Orange':50,'Grapes':60}
fruits2 = {'guava':90,'cherry':22,}
fruits1.update(fruits2)
print(fruits1.items())



