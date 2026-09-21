#Check if a number is positive, negative, or zero.

n=int(input("Enter your number : "))
if n>0:
    print("Its a positive number...")
elif n<0:
    print("Its a negative number... ")
elif n==0:
    print(" the value of number is 0... ")
else:
    print("Invalid number...")            


#Check whether a number is even or odd.

num=int(input("Enter your number : "))
if num%2==0:
    print("This is a even number ...")
else:
    print("This is a odd number ...")    



#Find the greater of two numbers.

n1=int(input("Enter number 1 : "))
n2=int(input("Enter number 2 : "))
print("The value of n1 is :",n1)
print("The value of n2 is :",n2)

if n1>n2:
    print("N1 is greater than n2...")
else:   
    print("n2 is greater than n1...") 



#Find the greatest of three numbers.
n1=13
n2=56
n3=23
print("The value of n1 is : ",n1)
print("The value of n2 is : ",n2)
print("The value of n3 is : ",n3)
if n1>n2 and n1>n3:
    print("n1 is the greatest number of three numbers...")
elif n2>n1 and n2>n3:
    print("n2 is the greatest number of three numbers...")
elif n3>n1 and n3>n2:
    print("n3 is the greatest number of three numbers...")   
else:
    print("sorry invalid output ...!")     




#Check if a person is eligible to vote (age ≥ 18).
age=int(input("Enter your age : "))
if age>=18:
    print("You are eligible to vote...")
else:
    print("You are not eligible for vote...")    

#Check whether a year is a leap year.
year=int(input("Enter year : "))
if year%4==0:
    print("This is a leap year...: ",year)
else:
    print("This is not a leap year...:",year)    

#Check if a character is a vowel or consonant.

letter=(input("Enter your alphabet : "))
if letter.lower() in('a','e','i','o','u'):
    print("it,s a vowel ...")
else:
    print("its a consonent...")    


#Check whether a number is divisible by 5 and 11.
num=int(input("Enter your number : "))
if num%5==0 and num%11==0:
    print("This number is divisible by 5 and 11 : ",num)
else:
    print("This is a number not divisible by 5 and 11 : ",num)    



#Check if a number is a multiple of both 3 and 7.
n=int(input("Enter your number: "))
if n%3==0 and n%7==0:
    print("This number is multiple of both 3 and 7 : ",n)
else:
    print("the number is not multiple of 3 and 7...",n)    






#assign grades based on marks :
#90-100:A
#80-89:B
#70-79:C
#60-69:D
#below 60:F

marks=int(input("Enter your marks :  "))

if marks>=90 and marks<=100:
    print("You have got A grade")

elif marks>=80 and marks<=89 :
    print("You have got B grade ")

elif marks>=70 and marks<=79:
    print("You have got C grade ")

elif marks >=60 and marks<=69:
    print("You have got D grade ")  

else:
    print("You are failed")    




#check if a character is uppercase or lowercase

char=input("Enter a character : ")

if 'A'<=char<='Z':
    print(" This is a Uppercase letter")

elif 'a'<=char<='z' :
    print("This is a Lowercase letter")

else:
    print("This is not an alphabet")       





#find whether the entered alphabet is a vowel using if-elif.

letter=input("Enter a alphabet : ")

if letter in ('a','e','i','o','u'):
    print("This is a vowel ")

elif letter in ('A','E','I','O','u'):
    print("this is a vowel ")

else:
    print("It is not a vovel it might be consonent") 



#check if three sides can form a tringle

s1=int(input("Enter side 1 length : "))
s2=int(input("Enter side 2 length : "))
s3=int(input("Enter side 3 length : "))

if s1+s2+s3==180 :
    print("This three sides can form a triangle")

else:
    print("This sides can not form a triangle ")    





#determine the type of triangle (Equilateral , isoscales, scalene .)

a=int(input("Enter length of side 1 : "))
b=int (input ("Enter length of side 2 : "))
c=int(input("Enter length of side 3 : "))

if a==b==c:
    print("This is an Equilateral ...")

elif a==b or b==c or a==c :
    print("This is an isoscales triangle...")

elif a!=b!=c:
    print("This is an scalene triangle ...")

else:
    print("There is no triangle is formed...")             
     




#find the gretest among four numbers 

n1=int(input("Enter your first number : "))
n2=int(input("Enter your second number : "))
n3=int(input("Enter your third number :  "))
n4=int(input("Enter your forth number : "))

if n1>=n2 and n1>=n3 and n1>=n4 :
    print("Frist number is gretest among four numbers ..")

elif n2>=n1 and n2>=n3 and n2>=n4 :
    print("Second number is greatest among four numbers ...") 

elif n3>=n1 and n3>=n2 and n3>=n4 :
    print("Third number is greatest among four numbers...")

else:
    print("Forth number is greatest among four numbers... ")     



#check whether the number is three digit number
num=int(input("Enter any number : "))
if 100>=num and num<=999:
    print("it is a three digit number...",num)
else:
    print("its not a three digit number...",num)    



#Calculate electricity bill using slab rates.
units=int(input("Enter electricity units : "))

if units<=100:
    bill=units*5
elif units<=200:
    bill=(100*5)+(units-100)*7
else:
    bill=(100*5)+(100*7)+(units-200)*10

print("Electricity bill=",bill)          

#Calculate income tax based on income slabs.  

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


#Check if a student passes (minimum 35 marks in each subject).
m1=int(input("Enter marks of subject 1 : "))
m2=int(input("Enter marks of subject 2 : "))
m3=int(input("Enter marks of subject 3 : "))

if m1>=35 and m2>=35 and m3>=35:
    print("Pass")
else:
    print("Fail")    



#Find whether a number is within a given range.
num=int(input("Enter your number : "))
if num>=10 and num<=50:
    print("Number is within a given range..")
else:
    print("Number is not in range...")    



#Build a simple calculator using if-elif-else (+, -, *, /).
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =", a / b)
else:
    print("Invalid operator")


#Determine the season based on the month number.
month = int(input("Enter month number: "))

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month >= 3 and month <= 5:
    print("Summer")
elif month >= 6 and month <= 8:
    print("Monsoon")
elif month >= 9 and month <= 11:
    print("Autumn")
else:
    print("Invalid month")



#Check if a year is a century leap year.
year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("Century Leap Year")
    else:
        print("Century Year but Not a Leap Year")
else:
    print("Not a Century Year")



#Find the number of days in a month.
month=int(input("Enter month number : "))

if month==2:
    print("28 or 29 days ")
elif month==4 or month==6 or month==9 or month==11:
    print("30 days")
elif month>=1 and month<=12:
    print("31 days")
else:
    print("Invalid month")            


#Check whether a password meets minimum conditions (length, digits, etc.)

password = input("Enter password: ")

if len(password) >= 8:
    has_digit = False

    for ch in password:
        if ch >= '0' and ch <= '9':
            has_digit = True

    if has_digit:
        print("Strong Password")
    else:
        print("Password must contain at least one digit")
else:
    print("Password must be at least 8 characters long")



#Determine ticket price based on age category.


age = int(input("Enter age: "))

if age < 5:
    print("Ticket Price = Free")
elif age <= 18:
    print("Ticket Price = 100")
elif age <= 60:
    print("Ticket Price = 200")
else:
    print("Ticket Price = 150")


#Calculate discount based on purchase amount.


amount = int(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 2000:
    discount = amount * 10 / 100
else:
    discount = 0

print("Discount =", discount)
print("Final Amount =", amount - discount)


#Check if a person is eligible for a driving license (age and eyesight condition).
age = int(input("Enter age: "))
eyesight = input("Is eyesight good? (yes/no): ")

if age >= 18 and eyesight == "yes":
    print("Eligible for Driving License")
else:
    print("Not Eligible")



#Create a login system with username and password validation

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")



# Create a menu-driven program using if-elif-else with options like:
# Addition
# Subtraction
# Multiplication
# Division
# Exit

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