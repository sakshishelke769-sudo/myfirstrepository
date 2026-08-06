# "x" : Create new file ;fails if it already created

# file=open('Nwefile.txt','x')
# file.write("Hello python..!")
# file.close()
# print("file created successfully . ")


#Rename file
# file=open('nostudy.txt','w')
# file.write("Hello python..!")
# file.close()
# import os
# os.rename('nostudy.txt','study.txt')
# print("file renamed successfuly..")

#Delete a file -os.remove()

import os 
os.remove('nostudy.txt')
print("File deleted successfuly ..")