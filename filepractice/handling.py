# try:
#     num=int(input("Enter your number : "))
#     result=10/num
#     print(result)
# except ZeroDivisionError:
#     print("You can not divide a number by zero")

#value error:
# try :
#     num=int(input("Enter your value : "))
#     result=10/num
#     print(result)
# except ValueError:
#     print("Invalid value")    


# try:
#     num=int(input("Enter your number : "))
#     result=10/num
#     print(result)

# except ZeroDivisionError:
#     print("you can not divide a number by zero ...")

# except ValueError:
#     print("You can not put any invalid value ..")

# else:
#     print("Program executed successfully...!")          
 

#file handling...
#file not found error 

# try:
#     file=open('home.txt','r')
#     s=file.read()
#     print(s)
# except FileNotFoundError:
#     print("File not found !")   
    

import module

print(module.add(10,5))

print(module.sub(15,5))

print(module.mul(3,8))

print(module.div(10,2))