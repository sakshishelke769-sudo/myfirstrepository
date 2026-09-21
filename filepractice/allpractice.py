#1. Data Types


#Find the data type of every value in a mixed list.

my_list=[5,8,2,"Amaish","Nagpur",39.4,True,'s']

print(type(my_list))

for i in my_list :
    print(i,"=",type(i))


#Convert a nested list into a tuple of tuples.

mylist=[[67,45,86],['a','b'],[2,7,4]]
print("Here is my nested list : ",mylist)
print(type(mylist))
result=tuple(tuple(i) for i in mylist)
print("Type of result is : ",type(result))
print(result)
print("converting a nested list into a tupels :",result)




#Remove all duplicate values from a mixed list while preserving the original order.

numbs=[10,20,'Python',10,'Python',30,20,True,True]

result=[]

for i in numbs:
    if i not in result:
        result.append(i)
print("Original list : ",numbs)        
print("List after removing duplicates",result)




#2. Operators


#Check whether a number is a power of 2 using operators.

num=int(input("Enter a number : "))

if num >0 and (num & (num -1))==0:
    print("Power of 2")
else:
    print("Not a power of 2")    


#Swap two numbers using bitwise XOR.

a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))

print("Before swapping..: ")
print("a=",a)
print("b=",b)

a=a^b
b=a^b
a=a^b

print("After swapping..: ")
print("a=",a)
print("b=",b)


#Find whether a number is divisible by both 4 and 6 using logical operators.

n=int(input("Enter your number : "))

if n%4==0 and n%6==0:
    print(n,": The number is divisible by both 4 and 6 .. ")

else:
    print(n,"This number is not divisible by both 4 and 6")    




#Calculate the total electricity bill using different unit rates.

units=int(input("Enter electricity units : "))

if units<=100:
    bill=units*5
elif units<=200:
    bill=(100*5)+(units-100)*7
else:
    bill=(100*5)+(100*7)+(units-200)*10

print("Electricity bill=",bill)          
 


#3. Conditional Statements


#Check whether three sides can form a triangle.

s1=int(input("Entar your number for side 1 : "))
s2=int(input("Enter your number for side 2 : "))
s3=int(input("Enter your number for side 3 : "))

if s1+s2+s3==180:
    print("This three sides can form a triangle ...","s1=",s1,"s2 =",s2,"s3 =",s3)
else:
    print("this three sides can not form a triangle...")    



#Determine the type of triangle (Equilateral, Isosceles, Scalene).


s1=int(input("Entar your number for side 1 : "))
s2=int(input("Enter your number for side 2 : "))
s3=int(input("Enter your number for side 3 : "))

if s1==s2 and s1==s3 and s2==s3:
    print("Its a equilatral triangle...")
elif s1==s2 or s1==s3 or s2==s3:
    print("its a isoscelen triangle...")
elif s1!=s2 and s2!=s3 and s1!=s3:
    print("Its a scalene triangle ...")
else:
    print("it is not a triangle...")    



#Create a simple ATM menu (Withdraw, Deposit, Balance)


balance =5000

print("1.Check Balance")
print("2.Deposite")
print("3.Withdraw")
print("4.Exit")

choice=int(input("Enter your choice : "))

if choice ==1:
    print("Balance =",balance)
elif choice ==2:
    amount=int(input("Enter deposite amount : "))
    balance=balance+amount
    print("Update balance =",balance)

elif choice==3:
    amount=int(input("Enter withdrawal amount : "))
    if amount<=balance:
        balance=balance-amount
        print("Updated Balance =",balance)

    else:
        print("Insefficient Balance ")

elif choice==4:
    print("Thank you..!")

else:
    print("Invalid Choice")



#Calculate income tax based on different tax slabs.

income=int(input("Enter your income : "))
if income<=250000:
    tax=0
elif income<=500000:
    tax=income*5/100
elif income<=1000000:
    tax=income*20/100
else:
    tax=income*30/100

print("tax=",tax)



#Create a menu-driven calculator using if-elif.

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a + b)
elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a - b)
elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a * b)
elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result =", a / b)
elif choice == 5:
    print("Exit")
else:
    print("Invalid Choice")



#4. Loops


#Print all prime numbers between 1 and n.


n=int(input("Enter a number : "))
for i in range(2,n+1):
    count=0

    for j in range(1,i+1):
        if i%j==0:
          count =count+1

    if count==2:
       print(i)     



#Find the factorial of a number using a loop.

num=int(input("Enter a number : "))

fact=1

for i in range(1,num+1):
    fact=fact*i

print("Factorial =",fact)    



#Print the Fibonacci series up to n terms

n=int(input("Enter the number of terms : "))

a=0 
b=1

for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c





#Check whether a number is an Armstrong number.

num=int (input("Enter a number : "))
temp=num
sum=0

while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10

if sum==num:
    print("Armstrong number ...")

else:
    print("Not an amstrong number... ")        



#Reverse a number and check if it is a palindrome.

num=int(input("enter a number : "))

temp=num
reverse=0

while temp>0:
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10

print("Reverse =",reverse)

if num==reverse:
    print("Palidrome number...")
else:
    print("Not a palidrome number...")    



#Find the Greatest Common Divisor (GCD) of two numbers.

num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))

gcd=1

for i in range (1,min(num1,num2)+1):
    if num1 %1==0 and num2%i==0:
        gcd=i

print("GCD =",gcd)        



#5. Functions


#Write a function to check if a string is a palindrome.

def palidrome(s):
    if s ==s[::-1]:
        print(" A string is a Palidrome...")
    else:
        print("A string is not a palidrome...")

text=input("Enter a string : ")
palidrome(text)  



#Write a function to count vowels and consonants in a string.


def count(s):
    vowels = 0
    consonent = 0

    for ch in s:
        if ch.isalpha():
            if ch in "aeiouAEIOU":
                vowels = vowels + 1
            else:
                consonent = consonent + 1

    print("Vowels =", vowels)
    print("Consonents =", consonent)

text = input("Enter a string: ")
count(text)




#Create a function to calculate simple and compound interest.

def interest(p,r,t):
    simple=(p*r*t)/100
    compound=p*(1+r/100)**t-p

    print("Simple interest =",simple)
    print("Compo interest = ",compound)

p = float(input("Enter principle amount : "))
r=float(input("Enter rate : "))
t=float(input("Enter time : "))

interest(p,r,t)


#Write a function to return all factors of a number.

def factors(num):
    result=[]

    for i in range(1,num+1):
        if num %i==0:
           result.append(i)

    return result

num=int(input("Enter a number : "))
print("All facturs of a number : ",factors(num))     



#Write a function to find the second-largest number in a list.

def second_gretest(numbers):
    numbers=list(set(numbers))
    numbers.sort()

    return numbers[-2]


my_list=[10,26,5,40,38]
print("Second largest number = ",second_gretest(my_list))




#6. Lists 

#Merge two lists without duplicates.

list1=[1,2,3,4,5]
list2=[4,5,6,7,8]

result=[]

for x in list1+list2:
    if x not in result:
        result.append(x)

print("Merged list without duplicates : ",result)



#Find the second-largest and second-smallest elements.

numbs=[3,67,23,55,46,33]

numbs=list(set(numbs))
numbs.sort()

print("Second smallest element from my list is : ",numbs[1])
print("Second largest element from my list is : ",numbs[-2])


#Rotate a list to the left by k positions.

my_list =[1,2,3,4,5]
k=2

result=my_list[k:]+my_list[:k]

print("Original list = ",my_list)
print("Rotated list = ",result)

#Separate even and odd numbers into two lists.

numbers=[3,14,7,8,2,9,16,5]
even=[]
odd=[]

for i in numbers:
    if i %2==0:
        even.append(i)

    else:
        odd.append(i)  
print("Even numbers = ",even)
print("Odd numbers =",odd)  
        


#Find the common elements between two lists.

list1=[1,2,3,4,5]
list2=[7,5,3,8,2]
result=[]
for i in list1:
    if i in list2:
        result.append(i)

print("Common elements between list1 and list 2 : ",result)




#7. Tuples & Sets

#Count the frequency of each element in a tuple.

mytuple=(1,3,1,2,4,5,3,2,2)
frequency={}

for i in mytuple:
    if i in frequency:
        frequency[i]=frequency[i]+1
    else:
        frequency[i]=1

print("Frequency of each element in a tuple is :",frequency)            


#Find the union, intersection, and difference of two sets.

s1={2,4,6,8,1,3}
s2={3,2,6,5,1,8}

result=s1.union(s2)
print("Union of two sets : ",result)

result=s1.intersection(s2)
print("Intersection of two sets : ",result)

result=s1.difference(s2)
print("Diffrence of two sets : ",result)



#Check whether one set is a subset of another.

s1={3,5,2}
s2={1,9,5,3,7,2}
print("Set 1 is : ",s1)
print("Set 2 is : ",s2)

if s1.issubset(s2):
    print("Set 1 is subset of Set 2...")
else:
    print("Set 1 is not subset of Set 2... ")    



#8. Dictionaries

#Count the frequency of words in a sentence.

sentence=input("Enter a sentence : ")

words=sentence.split()
frequency={}

for word in words:
    if word in frequency:
        frequency[word]=frequency[word]+1
    else:
        frequency[word]=1

print("Word frequency =",frequency)
            


#Create a dictionary from two lists (keys and values).

l1=['name','id','sub','city']
l2=['Rajvir',101,'Python','Nagpur']
print("List 1 = ",l1)
print("List 2 = ",l2)

keys=l1
values=l2

mydictionary=dict(zip(keys,values))

print("Creating a dictionary from two lists : ",mydictionary)


#Sort a dictionary by its values.

mydict={'a':3,'b':1,'c':2}
print("my dictionary before sorting by its value : ",mydict)
sorted_dict=dict(sorted(mydict.items(),key=lambda x:x[1]))
print("my sorted dictionary after sorting a original  dictionary by its value : ",sorted_dict)



#9. File Handling

#Read a text file and count the number of lines, words, and characters.

file=open('example.txt','r')
lines=file.readlines()

line_count=len(lines)

word_count=0
char_count=0

for line in lines:
    word_count=word_count+len(line.split())
    char_count=char_count+len(line)

file.close()

print("number of lines in my text file are : ",line_count)
print("Number of words in my text file are : ",word_count)
print("Number of characters in my text file are : ",char_count)



#Copy only the even-numbered lines from one file to another.

source=open('example.txt','r')
destination=open('Newfile.txt','w')

lines=source.readlines()

for i in range(len(lines)):
    if(i+1)%2==0:
        destination.write(lines[i])

source.close()
destination.close()

print("Even numbered lines copied successfully...")


#10. Exception Handling

#Handle invalid integer input using try-except.

try:
    num=int(input("Enter a number : "))
    print("You have entered :",num)

except ValueError:
    print(" Ivalid Number! please enter an integer... ")    



#Handle file-not-found errors while reading a file.

try:
    file=open('python.txt','r')
    p=file.read()
    print(p)
    file.close() 
except FileNotFoundError:
    print("File not found ! ")   
    


#11. Modules

#Create a random password generator using the random and string modules.

import random
import string

length=int(input("Enter password length : "))
characters=string.ascii_letters + string.digits +string.punctuation

password=""

for i in range(length):
    password=password +random.choice(characters)

print("Generated password =",password)    


#Use the datetime module to calculate the number of days between two dates.

from datetime import datetime

date1=input("Enter first date (DD-MM-YYYY): ")
date2=input("Enter second date (DD-MM-YYYY): ")

d1=datetime.strptime(date1,"%d-%m-%Y")
d2=datetime.strptime(date2,"%d-%m-%Y")

days=abs((d2-d1).days)

print("Number of days between date 1 and date 2 =",days)