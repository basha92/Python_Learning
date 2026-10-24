#type annotation or type casting annotates the variable with a type. It can be used for functions also.
#this won't change the functionality of the code. 
#python supports almost all data types: int, float, str, tuple, set, dictionary for type casting
#two types: 1.explicit - user assigns it 2.implicit - python converts them to higher data type to prevent data loss automatically

#implicit casting
#a = 1.9
#b = 8
#c=a+b
# print(type(a)) #float
# print(type(b)) #int
# print(c)
# print(type(c)) #converts to float

#explicit casting
def add_numbers(a:int,b:int,c:int) -> int:
    return a+b+c

result = add_numbers(1,2,3)
print(result)