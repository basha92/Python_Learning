#this program provides examples for all collection types in python
'''collection - single variable used to store multiple values
List - [] ordered and changeable; allows duplicates; any type of data can be stored;
insert(), append(), extend(), pop()'''

#example list
fruits = ['apple', 'orange', 'coconut', 'kiwi']
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

'''Tuples - () '''
