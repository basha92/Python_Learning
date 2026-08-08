#this program provides examples for all collection types in python
'''collection - single variable used to store multiple values
List - [] ordered and changeable; allows duplicates; any type of data can be stored;
insert(), append(), extend(), pop()'''

#example list
#fruits = ['apple', 'orange', 'coconut', 'kiwi']
#print all elemetnts
#print(fruits)

#print particular
#print(fruits[0])
#print(fruits[1])

#print in range
#print(fruits[::-1]) #print from last element
#print(fruits[::2]) #print all second elements from zeroth element
#print(fruits[2:4]) #print the elemtns in the index 2,3.

#adding elements
''' append() - add all emenents as one. it takes one argument at a time;
extend() - add elements one by one'''
#fruits.append(['strawberry', 'banana']) - ['apple', 'orange', 'coconut', 'kiwi', ['strawberry', 'banana']]
#fruits.extend(['strawberry', 'banana']) - ['apple', 'orange', 'coconut', 'kiwi', 'strawberry', 'banana']
#print(fruits)

'''set - {} unordered and immutable. ADD/REMOVE ok. no duplicates
common methods - add(), remove(), update(), pop()'''
#fruits = {'apple', 'orange', 'coconut', 'kiwi', 'dragon fruit'}

#adding element
# fruits.add('banana')

#updating
#The .add() method treats whatever you pass into it as one single element.
#The .update() method expects an iterable (a collection it can loop through). 
#Because a string is an iterable in Python, 
#.update() unpacks the string and attempts to add every individual character. 
#Since sets automatically remove duplicates, only the unique letters remain.
#fruits.update('dragon fruit')
#o/p: {' ', 'coconut', 'a', 'd', 'kiwi', 'orange', 'apple', 'o', 'u', 'i', 't', 'r', 'g', 'f', 'n'}

#removing element
#fruits.remove('apple')

#popping out the last element
#fruits.pop()

#print(fruits)

'''tuples - () ordered and immutable(unchangeable); duplicates are ok. faster'''

#fruits = ('apple', 'orange', 'coconut', 'kiwi', 'dragon fruit', 'apple')

#print(fruits.index('orange'))
#print(len(fruits))
#print('apple' in fruits)
#returns the count of the string
#print(fruits.count('apple'))

'''Dictionaries - {} do not allow duplicates. any type of data can be stored'''
#fruits = {'apple', 'orange', 'coconut', 'kiwi', 'dragon fruit', 'apple'}
student = {'Name': 'John', 'age': 30, 'courses': ['Maths', 'CompSci']}

#prints whole dictionary
#print (student)

#prints particular element in dictionary
#print(student['courses'])

#or use the below method
#print(student.get('Name'))

#add or update element
student.update({'Name': 'Jane', 'Phone': '555-55555', 'age': 25})
print(student)

#to see keys
print(student.keys())
 #to see values
print(student.values())