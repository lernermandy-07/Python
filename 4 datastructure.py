# # the data structure in python are folls

# comparison in data structures in python

# List	Tuple	Set	   Dictionary

# list

# A list is a non-homogeneous data structure that stores the elements in columns of a single row or multiple rows.


# Tuple

# A Tuple is a non-homogeneous data structure that stores elements in columns of a single row or multiple rows.


# set

# The set data structure is non-homogeneous but stores the elements in a single row.


# Dictionary

# A dictionary is also a non-homogeneous data structure that stores key-value pairs.


# # list

# list is a mutable 

num=[1,34,45,56,67,89,90]

print(num)

float=[12,34,56,34,56,34.56,34]

# sort 

print(float)

float.sort()

print(float)

name=['mandar','kalu','amol']

print(name)

com=[2+3j,4+5j,45]

print(com)

all=[34,77.77,'mandy',56+5j,'bharat']

print(all)

print(all,num,float,name,com)

# all.append

all.append(23)

print(all)

# num.insert

num.insert(2,100)

print(num)

num.insert(4,'randy')

print(num)

float.insert(3,'cricket')

print(float)

name.insert(4,'randy')

print(name)

# remove

num.remove('randy')

print(num)

cars=['lamborgini','wokswagun','bmw','mercedese','porche']

print(cars)

cars.extend(['tata','mahindra','tesla'])

print(cars)

# pop

cars.pop(3)

print(cars)

cars.pop(1)

print(cars)

# del 

del cars[1:3]

print(cars)

# Forward indexing  

component=[34,45,67,89,758,36,25,26]

print(component,type(component))

print(component[2])

#  Backward Indexing 

print(component[-7])

#  Forward slicing 

print(component[0:7])

#  Backward slicing 

print(component[-6:])

#  Step slicing

print(component[1:2:7])

# min , max , sum ,  sort

value=[282382393,43934935,7374,737878,7437393,37347383983]

print(min(value))

print(max(value))

print(sum(value))

value.sort()

print(value)




# set in the set are we can stored unique values 

lock={17,38,89,436,682,377.36,82,}

print(lock,type(lock))

clock={23.78,28,56,89,100,56}

print(clock,type(clock))

soll={100,45,1000,45,89,35}

print(soll)

# soll.add

soll.add(77)

print(soll)

# soll.remove

soll.remove(100)

print(soll)

# soll.pop

fruits = {"apple", "banana", "cherry","mango","lemon","guava"}

fruits.pop() 

print(fruits)

soll.pop()

print(soll)


# union set

clas1={'mandy','randy','candy','akshara','gayatri'}

print(clas1,type(clas1))

teacher2={'lad mam','shikalgar sir','kachare sir','vasave sir'}

print(teacher2,type(teacher2))

school=clas1.union(teacher2)

print(school)


# intersection set in python

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

# set difference in python

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)



# tuple in python

# tuple are unmutable we cannot change the value in tuple

electrons=('protons,nuetrons,electrons,atom')

print(electrons,type(electrons))

print(electrons[2])

table=(2,4,6,8,10)

print(table,type(table))

print(table[2])

# count in tuple method in python 

values = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5,5,67,6,5,5,5,4,3,5,67,43,2,456,322,4,56,77,896,32,21,34,1,23,4)

x = values.count(5)

print(x)

y=values.count(5)

print(y)

z=values.count(4)

print(z)

print(len(values))

# forword indexing in python

print(values[2])

# backword indexing in python

print(values[-30])

# forword slicing in python

print(values[2:30])



# dictinary in python

student={'mandy':'python','harsh':'java','tejas':'js','mahek':'c#' }

# lenght in python

print(len(student))

# values in python dictionayr

print(student,type(student))

print(student['mandy'])

print(student['mahek'])

print(student['tejas'])

# update in dictionary

no={'mandy':'java','randy':'js'}

print(no)

no.update({'candy':'c++'})

print(no)


# keys in python dictionary

print(student.keys())

# Python program to show working

# of items() method in Dictionary



Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }

print("Dictionary items:")

# Printing all the items of the Dictionary

print(Dictionary1.items())

clas={1:'deshmukh mam', 2:'rasal sir',3:'shah sir',4:'rahul sir',5:'renushe sir'}

print(clas,type(clas))


# items  in python 

print(student.items())

# add 2 list in python

clas1=['mandy','randy','candy','akshara','gayatri']

print(clas1,type(clas1))

teacher2=['lad mam','shikalgar sir','kachare sir','vasave sir']

print(teacher2,type(teacher2))

school=dict(zip(clas1,teacher2))

print(school)


stu=['mandy','kapil','rahul','rohan']

languages=['python','js','java','c++']

print(stu,type(stu))

print(languages,type(languages))

combine=dict(zip(stu,languages))

print(combine,type(combine))

print(combine['mandy'])

# update in Dictionary

combine['randy'] = 'r'

print(combine)

del combine['randy']

print(combine)


# dict in dict and also list

cricket={'bat':'stroke','bowl':'white','batsman':['rohit','dhoni'] ,'india':{'state':'maharashtra','bcci':'jay shah'}}

print(cricket,type(cricket))

print(cricket['bat'])

print(cricket['bowl'])

print(cricket['batsman'])

print(cricket['batsman'][1])

# print(cricket,['india'])



# range in python


# The range() function in Python takes up to three arguments:

# start (optional):

# An integer specifying the starting value of the sequence. If not provided, the default is 0.

# stop (required):

# An integer specifying the ending value of the sequence (exclusive). The sequence will stop one value before this.

# step (optional):

# An integer specifying the increment between each value in the sequence. If not provided, the default is 1. 

m = range(1,10)

print(m,type(m))

c = list(range(10))

local=list(range(0,99))

print(local)

# range through for loop

lucky=list(range(17))

print(lucky)

for i in lucky:
    print(i)

values=list(range(7,78))

print(values)

for i in values:
    print(i)

birth=list(range(2,17))

print(birth)

for i in birth:
    print(i)




