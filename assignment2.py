# Even or Odd Function
# Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".


def evenodd(n):
    if n%2==0:
        return f"this is an Even number..."
    else:
        return f"this is an Odd number..."

print(evenodd(6))    


#Largest of Two Numbers
#Write a function largest(a, b) that returns the larger number.

def largest(a, b):
    if a>=b:
        return f"{a} this is a largest number"
    elif b>=a:
        return f"{b} this is a largest number"
    else:
        return f"Invalid number..."

print(largest(10,3))    


#Print Numbers
#Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

def print_numbers(n):
    for n in range(1,n+1):
        print(n)

print(print_numbers(10))   


# Sum of Numbers
# Write a function sum_n(n) that returns the sum of numbers from 1 to n.


def sum_n(n):
    sum=0

    for i in range(1,n+1):
        sum+=i

    return sum

print(sum_n(15))    


# Multiplication Table
# Write a function table(n) that prints the multiplication table of n from 1 to 10.

def table(n):
    for i in range(1,11):
        print( f"{n} x {i} = {n*i}")
    
table(5)  


# Count Even Numbers
# Write a function that takes a list and returns how many even numbers it contains.
# Example:
# count_even([1, 2, 3, 4, 6])
# Output:3

def count_even(numbers):
    count =0

    for num in numbers:
        if num%2==0:
            count+=1

    return count
print("The count of even numbers is :  ")
print(count_even([3,2,8,6,9,4,12])) 



# Find Maximum
# Without using max(), write a function that returns the largest number in a list.

def my_max(numbers=0):
    largest=0
    for num in numbers:
        if num>largest:
            largest=num
    return largest
print("the largest number in a list is : ")
print(my_max([3,2,6,10,45]))        


# FizzBuzz
# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

def numbers():
    for i in range(1,101):

     if i%3==0 and i%5==0 : 
        return"FizzBuzz"
     elif i%3==0:
        print("Fizz")
     elif i%5==0 :
        print("Buzz")
     else:
        print(i)     

print(numbers()) 


#Write a function that returns True if a string is a palindrome.

def palindrome(text):
    if text==text[::-1]:
        return f"it is a palindrome..."
    else:
        return f"Not a palindrome..."
print(palindrome("madam"))
print(palindrome("hello")) 
 

#Write a function that counts the vowels in a string

def vowels(text):
    count=0
    for ch in text.lower():
        if ch in"aeiou":
         count=count+1
    return count
print(vowels("Hello how are you ..what are u doing  ... "))     


#Write a function that returns the second largest number in a list without using sort()

def second_largest(numbers):
    largest=0
    second=0

    for num in numbers:
        if num>largest:
            second=largest
            largest=num

        elif num>second:
            second=num

    return second
print(second_largest([10,20,5,40,30]))            
    

# Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

import random

def game():
    number=random.randint(1,10)

    while True:
        guess =int(input("Guess a number (1 to 10):"))

        if guess ==number:
            return"Correct! You guess the number."
        elif guess<number:
            print("Too Low !")
        else:
            print("Too High !")

print(game())
                


# Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"

def grade(marks):
    if marks >=90:
        return"A"
    elif marks>=80:
        return"B"
    elif marks>=70:
        return"C"
    elif marks>=60:
        return"D" 
    else:
        return"F"

marks=int(input("Enter your marks : ")) 

result=grade(marks)

print("Grade:",result)


