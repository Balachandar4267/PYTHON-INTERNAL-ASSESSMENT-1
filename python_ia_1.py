# -*- coding: utf-8 -*-
"""PYTHON IA 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zUf1GQzSEbmJpPiC3U1dhGKapVkVNoDz
"""

#1
length=float(input("Enter the length cm:"))
breadth=float(input("Enter the breadth in cm:"))
area = length * breadth
print("The area of the rectangle:",area)

#2
weight = float(input("Enter the weight in kg:"))
height = float(input("Enter the height in ms:"))
BMI = weight/(height **2)
print("The BMI for the person is",BMI)
if (BMI <19):
  print("under weight")
elif (20 >= BMI <= 25):
  print("Normal Weight")
else:
  print("Obese")

#3
a={}
name=input("Enter the name of the student:")
marks=int(input("Enter the marks:"))
a[name]=marks
print(a)

#4
age=int(input("Enter the age of the person:"))
if(age < 18):
  print(age,"Minor")
elif(18 >= age <= 55):
  print(age,"Adult")
else:
  print(age,"Senior")

#5
num=[]
for i in range(1,51):
  if(i%2==0):
    num.append(i)
print(num)

#6
a=input("Enter the password:")
if((a in "%s") and (a in (1,2,3,4,5,6,7,8,9,0)) and len(a)>12):
  print("Your password is correct")
else:
  print("Kindly type your password again")

#7
def average_number(lis):
  return lis
lis=[1,2,3,4,5]
sum=0
for i in range(len(lis)+1):
  sum=sum+i
a=average_number(lis)
b=sum/len(lis)
print(b)

#8
def vowels_count(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
input_string = "Balachandar"
print("Number of vowels:", vowels_count(input_string))

#9
import datetime
a=datetime.datetime.now().time()
print("The current time of the system is:",a)

#10
try:
  a=float(input("Enter the number1:"))
  b=float(input("Enter the number2:"))
  print("The addition of two numbers:",a+b)
except:
  print("You have entered the string.Please try again")

#11
try:
  a=int(input("Enter the number:"))
  print(a)
except:
  print("You have entered the string instead of integer")

#12
try:
  a=float(input("Enter the number1:"))
  b=float(input("Enter the number2:"))
  c=a/b
  print(c)
except:
  print("Zero division Error")

#13
a=open("/content/drive/MyDrive/IA Python 1.txt",'w')
script="Hello, Python!"
a.writelines(script)
a.close()

#14

a=open("/content/drive/MyDrive/filees.txt")
b=a.read()
print(b)

#15
a=open("/content/drive/MyDrive/filees.txt",'w')
dell =[]
for i in range(1,3):
  num = input("Enter the number:")
  dell.append(num)
a.writelines(dell)
a.close()