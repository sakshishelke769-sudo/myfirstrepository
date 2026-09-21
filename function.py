#functions in python
# def greet():
#     print("Good afternoon everyone...")
# greet()  


#function with return value
# def addtion():
#     return 27+14

# result=addtion()
# print("addition is : ",result)


#function with arguments and parameters..

# def addition():
#     return a+b

# result= addition(4,6)

# print(result)

# print(addition(9,3))

# print(addition(32,13))


#multiple parameters ...

# def addition(a,b,c,d,e):
#     return a+b*c/d*e
# result=addition(2,4,3,6,5)
# print(result)

# print(addition(4,2,7,9,6))


# def my_max(a,b):
#      if a>=b:
#           return a
#      elif b>=a:
#           return b
#      else:
#           print("Invalid Number..")

# print(my_max(6,4))   

# square = lambda x:x*x
# print(square(7))

# print(square(3))

# hello = lambda name: f"How are you {name}"
# print(hello("sakshi"))      


# def Evenod(num):
#     if num%2==0:
#         return ("It is an even number...")
#     else:
#         return ("It is a odd number...")
    
# print(Evenod(34))  

# print(Evenod(17))

# def largest(num1,num2):
#     if num1>=num2:
#         print("Num1 is gretest and value of num1 is :",num1)
#     elif num2>=num1:
#         print("Num2 is greatest and value of num2 is : ",num2)

#     else:
#         print("There is nno greater number...")

# print(largest(55,23))            


# def print_numbers(n):
#     for i in range(1,n+1):
#      print(i)

# print(print_numbers(20)) 


def sum_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=i

    return sum

print(sum_n(10)) 
print(sum_n(15))









        





