
#print numbers from 1 - 50 using for loop:

for i in range(1,50):
    print(i)


#print numbers from 1-50 using while loop
count=50

while count>=0:
    print(count)

count-=1    



#print numbers from 50 to 1 using for loop
for i in range (50,0,-1):
    print(i)




#print numbers from 50-1 using while loop  

a=50

while a>=1:
    print(a)
    a=a-1
     


#print all even numbers from 1 to 100

for i in range(1,100):
    if i%2==0:

     print(i)

# print all odd numbers from 1 to 100

for i in range(1,100):
    if i%2!=0:
        print(i)

#print all numbers that are divisible by 5 from 1 to 100.
for i in range(1,100):
    if i%5==0:
        print(i)

   
#print the sum of numbers from 1 to 100..

sum=0
i=1

while i<=100:
    sum=sum+i
    i=i+1

# print("sum of no. from 1 to 50 is :",sum)

sum=1

for i in range(1,51):
    sum=sum+i
print("sum is :",sum)   


# print sum of all even numbers from 1 to 20 .
sum=0

for i in range(2,21,2):
    
      sum=sum+i
print("sum of all even numbers from 1 to 20 is :",sum)     


sum=0
i=2

while i<=20:
    sum=sum+i
    i=i+2
print("sum of even no. from 1-100 is:",sum)    



#print sum of all odd numbers from 1 to 20 .

sum=0
for i in range (1,20,2):
    sum=sum+i
print("sum of all odd numbers from 1 to 20 is :",sum)    


sum=0
i=1
while i<=20:
    sum=sum+i
    i=i+2
print("sum of odd no. from 1-20 is : ",sum)    


#print first 20 natural numbers
for i in range(1,21):
    print(i)

i=0
while i<=20:
    i=i+1
    print(i)    



#print the multiplication table of a number entered by the user.

table =int(input("Enter a nuber to create a table : "))

for i in range (1,11):
    print(table,"x",i,"=",table*i)

  
num=int(input("Enter a numer: "))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1


#print the cube of numbers from 1 to 10.
c=1
for i in range (1,10):
    c=c+1
    print("cube of ",c,"=",c*c*c )

#print square of numbers from 1 to 10.

s=1

for i in range(1,10):
    s=s+1
    print("square of ",s,"=",s*s)



#print numbers from 100 to 1, decreasing by 5 each time.

for i in range (100,0,-5):
    
    print(i)



#count how many numbers are there from 1 to N.

n=int(input("enter n : "))

count=0

for i in range(1,n+1):
    count=count+1

print("count of numbers from 1 to n is =",count)    




# print all the numbers from between 1 and 100 that are divisible by 3 and 4

for i in range(1,101):
    if i%3==0 and i%4==0:

     print(i)    
    

#print all numbers between 1 and N that are divisible by 2.

n=int(input("Enter the value of n : "))
print("all numbers between 1 and n that are divisible by 2 are :",)

for i in range (1,n+1):
    if i%2==0:
     print(i)

#print the frist 10 multi[plies of given numbers.
n=int(input("enter value of n : "))

print ("the first 10  multiples of a given numbers are : ")

for i in range(1,11):
    print(n*i)


#print the numbers between 1 and N that are divisible by 2.

n=int(input("enter the value of n: " ))

for i in range(1,n+1):
    if n%2==0:

     print(i)


#print the numbers from 1 to n , skipping numbers divisible by 3.
n=int(input("enter value of n : "))

for i in range(1,n+1):
    if i % 3==0:
        continue
    print(i)


#print the numbers from 1 to n and stop when the number reaches 20.

n=int(input("enter the value of n : "))

print("the numbers from 1 to n and stop when the numbers reaches 20 : ")

for i in range (1,n+1):
    if i==20:
        break
    print(i)



#print the following pattern
# 1
# 22
# 333
# 4444
# 55555

for i in range (1,6):
    for j in range(i):
        print(i,end="")
    print()    


for i in range (1,6):
    for j in range(i):
        print("*",end="")
    print()    


for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()   


for i in range(5,0,-1):
    for j in range(i):
        print(i,end="")
    print()    
