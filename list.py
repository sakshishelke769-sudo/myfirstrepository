# numbers=[9,6,8,3,5,7,2]

# numbers2=[8,5,3,5,8,4,6]

# numbers.insert(4,67)
# print(numbers)
# numbers.remove(3)
# print(numbers)

# numbers.reverse()
# print(numbers)

# numbers.pop()
# print(numbers)

# numbers.pop(0)
# print(numbers)


# name=[4,5,6,3,7,["playing,singing"],6, 9,3]

# print(name[5][0])

# print(name[5])



#for loop
# list=["apple","orange","kiwi","pineapple"]

# for items in list:
#     print(f"this are my fevorite fruits :{items}")

#while loop 

# name=input("Enter your name: ")

# while name=="sakshi":
#     print("valid user")

# print("Invalid user")    


#tuple

# my_tuple=(3,"siya",8,9,3,2)
# print(type(my_tuple))
# print(my_tuple)
# print(my_tuple[1])


#dictionary

# mydic={"name":"siya","contact":9469389204,"address":"Akola","salary":50000}

# print(mydic)
# print(mydic["salary"])

# for key in mydic:
#     print(key)
#     print(f"This is the {key} and this  is the value of it {mydic[key]}")
# for values in mydic.values():
#     print(values)    


# mydic["Role"]=["Accounting"]
# print(mydic)     



#set

# myset={"sakshi",21,"python"}
# print(myset)
# print(type(myset))
# myset.remove(21)
# print(myset)
# myset.discard(0)
# print(myset)



#Create a list of 5 integers.
# mylist=[5,4,2,90,17,2,2]
# print(mylist)

#Print the first element of a list.
# print(mylist[0])

#Print the last element of a list.

# print(mylist[4])

# #Find the length of a list.
# print("Length of my list is : ",len(mylist))

#add an element to the end of a list.
# mylist.append(7)
# print(mylist)

#Insert an element at a specific position.
# mylist.insert(3,6)
# print(mylist)


#Remove an element by value.
# mylist.remove(6)
# print(mylist)

#Remove an element by index.
# mylist.pop(4)
# print(mylist)

#Check if an element exists in a list.

# if 17 in mylist:
#     print("an element exixst in a list ...")

# else:
#     print("No element found...")  


#Count how many times an element appears.     
 
# element=2
# print("count of",element,"is",mylist.count(2))

#Find the index of an element.
# pos=mylist.index(2)
# print("index of 2 is : ",pos)

#Sort a list in ascending order.
# mylist.sort()
# print("sorting a list in ascending order",mylist)


#Sort a list in descending order.
# mylist.sort(reverse=True)
# print("sorting a list in descending order",mylist)


#Reverse a list.
# l=[6,8,3, 1,7,4,2]
# l.reverse()
# print("Reversing a list : ",l)

#Clear all elements from a list
# print(l)
# l.clear()
# print("clear all elements from a list",l)

#Create a tuple of 5 numbers.
# tuple_t =(22,86,17,45,30)
# print(tuple_t)
# print(type(tuple_t))

#Print the first element of a tuple
# print("first element of my tuple is : ",tuple_t[0])

#Print the last element of a tuple.
# print("last element of my tuple is : ",tuple_t[4])

#Find the length of a tuple.
# t2=(48,22,35,81,18,)
# print("Length of my tuple is : ",len(tuple_t))
# print("Length of my tuple2 is : ",len(t2))

#Count the occurrences of a value in a tuple.
# tuple_t.count(22)
# print("Count of occurrance of 22 in my tuple is : ",tuple_t.count(22))
# print("Count of occurrance of 22 in my tuple2 is : ",t2.count(22))

#Find the index of an element in a tuple.
# tuple_t.index(86)
# print("index of 86 in my tuple is : ",tuple_t.index(86))

#Convert a tuple to a list.
# print(t2)
# print(type(t2))
# t2=list()
# print(type(t2))

#Convert a list into a tuple
# t2=tuple()
# print(type(t2))

#Concatenate two tuples.
# result=tuple_t + t2
# print("Concatination two tuples tuple_t and t2 : ",result)

#Check whether an element exists in a tuple

# if 22 in tuple_t:
#     print("Element found")
# else:
#     print("Element not exixts")   

#Create a set of integers.    
 
# set1={15,67,75,33,23,55,23,15}
# print("I create a set :",set1)
# print(type(set1))


#Add an element to a set.

# set1.add(11)
# print("adding an element to a set",set1)

#Remove an element from a set.

# print("REmoving 23 from the set",set1.remove(23))
# print(set1)

#Check whether an element exists in a set.

# if 75 in set1:
#     print("Eliment exists in a set")
# else:
#     print("Element does not exists")    


#Find the length of a set

# print("Length of my set is : ",len(set1))

#Find the union of two sets.
 
# s2={23,45,18,22,15,55} 

# result=set1.union(s2)
# print("Union of two set set1 and s2 is : ",result)


#Find the intersection of two sets.
# result=set1.intersection(s2)
# print("Intersection of two sets set1 and s2 is : ",result)


#Find the difference between two sets.
# r=set1.difference(s2)
# print("Diffrence between two sets set1 and s2 is : ",r)


#Clear all elements from a set.

# s2.clear()
# print("clearing all elements from a set s2 : ",s2)

#Remove duplicate elements from a list using a set.

# numbers=[12,45,12,55,37,44]
# u=list(set(numbers))
# print("Removing duplicate value from the list using a set : ",u)

#Create a dictionary with student details.

student={"Name":"Priyansh","Id":202,"Branch":"Scince","Sub":"Chemistry"}
# print("this is my dictionary with student detail :  ",student)
# print(type(student))

#Print the value of a specific key.

# print("Value of sub key is : ",student["Sub"])

#Add a new key-value pair.

# student["City"]="Amaravti"
# print("adding a new key value pair :")
# print(student)

#Update the value of an existing key.

# student["Id"]=201
# print("Updating the value of an existing key : ",student)

#Delete a key from a dictionary.
 
# student.pop("City",None)
# print("deleting key city from a dictionary",student)

#Find the length of a dictionary.

# print("Lenhth of my sictionary is : ",len(student))

#Print all the keys

# print("Printing all the keys of my dictionary : ",student.keys())



#Print all the values.

# print("printing all the values of my dictionary : ",student.values())

#Print all key-value pairs.
# print("printing all key-value pairs of my dictionary :")

# for key, value in student.items():
#     print(f"{key}:{value}")

#Check whether a key exists.    

# key="Name"
# if key in student:
#     print("exists in my dictionary",key)
# else:
#     print("key does not exist..")    

#Use get() to retrieve a value.

# print("using get to retrive a value from dictionary Value of name is : ",student.get('Name'))

#Merge two dictionaries.

# student_2={"name":"siya","branch":"Ds","id":101}
# result=student|student_2
# print("merging two student dictionaries :",result)

#Clear a dictionary.
# print(student_2)
# student_2.clear()
# print(student_2)

#Create a dictionary from two lists (keys and values).

# l1=['name','rollno','address','field','sub']
# l2=['Rakesh',23,'Akot','Arts','Drawing']
# keys=l1
# values=l2
# my_dictionary=dict(zip(keys, values))
# print("creating a dictionary from two lists :")
# print(my_dictionary)


#Iterate through a dictionary and print each key and value.
print("Iterating through a dictionary and printing each key and value :")
for key ,value in student.items():
    print(f"keys: {key}, values: {value}")