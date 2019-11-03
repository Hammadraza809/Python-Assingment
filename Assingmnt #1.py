import datetime
import sys
#Q#1
print("Twinkle,twinle, little star,\n"+
      "\t How I wonder what you are!\n"+
      "\t \t Up above the world so high,\n"+
      "\t \t Like a diamond in the sky.\n"+
      "Twinkle, twinkle, little star,\n"+
      "\t How I wonder what you are")
#Q#2
print("Python Version is: "+sys.version)

#Q#3
print("Current date and time is: "+str(datetime.datetime.now()))

#Q#4
raduis = int(input("Please enter raduis of circle:\n"))
print("Area of the circel is: "+str(3.41*(raduis**2)))

#Q#5
f_name = input("Enter your First Name:\n")
l_name = input("Enter your Last Name:\n")
print(l_name+" "+f_name)

#Q#6
first_no = int(input("Enter first number:\n"))
sec_no = int(input("Enter second number:\n"))
print(str(first_no+sec_no))
