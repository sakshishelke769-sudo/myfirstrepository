#Write a Python program to check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#Write a program to find the largest of three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number:", largest)


#Write a program to check whether a given number is prime.

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")



#Write a program to print the Fibonacci series up to n terms.

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c


#Write a program to find the factorial of a number using a loop.

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial:", factorial)



#Write a program to reverse a string without using [::-1].

string = input("Enter a string: ")

reverse = ""

for char in string:
    reverse = char + reverse

print("Reversed string:", reverse)


#Write a program to check whether a string is a palindrome.

string = input("Enter a string: ")

reverse = ""

for char in string:
    reverse = char + reverse

if string == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")



#Write a program to count the number of vowels and consonants in a string.

string = input("Enter a string: ")

vowels = 0
consonants = 0

for char in string:
    if char.lower() in "aeiou":
        vowels = vowels + 1
    elif char.isalpha():
        consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)



#Write a program to find the sum of all elements in a list.

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total = total + num

print("Sum:", total)



#Write a program to find the largest and smallest element in a list without using max() or min().

numbers = [10, 25, 5, 40, 15]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)



# Write a program to remove duplicate elements from a list.

numbers = [1, 2, 2, 3, 4, 3, 5, 1]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List after removing duplicates:", unique)



# Write a program to count how many times each element appears in a list using a dictionary.

numbers = [1, 2, 2, 3, 1, 4, 2, 3]

count = {}

for num in numbers:
    if num in count:
        count[num] = count[num] + 1
    else:
        count[num] = 1

print(count)



#Write a program to find the second-largest number in a list.

numbers = [10, 25, 5, 40, 30]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)


#Write a program to sort a list without using sort() or sorted().

numbers = [5, 2, 8, 1, 3]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)



#Write a function that accepts a list of numbers and returns a list containing only the even numbers.

def even_numbers(numbers):
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    return even


numbers = [1, 2, 3, 4, 5, 6, 8]

result = even_numbers(numbers)

print("Even numbers:", result)



#Write a program to find the frequency of each character in a string.

string = input("Enter a string: ")

frequency = {}

for char in string:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)


#Write a program to check whether two strings are anagrams of each other.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")


#Write a program to find all duplicate values in a list.

numbers = [1, 2, 3, 2, 4, 5, 1, 3, 6]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate values:", duplicates)



#Write a program that takes a sentence and finds the longest word.

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)



# Create a simple student marks program that:
# accepts marks for 5 subjects,
# calculates the total and percentage,
# assigns a grade,and displays whether the student passed or failed.

m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
m4 = int(input("Enter marks for Subject 4: "))
m5 = int(input("Enter marks for Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    result = "Passed"
else:
    result = "Failed"

print("Total marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)
