#1

num1=eval(input("Enter first number:"))
num2=eval(input("Enter second number"))
print("The sum of the Two Numbers is:-",num1+num2)

#2

num=int(input("Enter a Number"))
if num>0:
    if num//2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")
elif num==0:
    print("The entered number is neither Odd nor Even")
else:
    print("This is a Negative Number")

#3

num=int(input("Enter a Number"))
if num > 0:
    fact=1
    for i in range(1,num+1):
        fact*=i
    print("Factorial of the Number is",fact)
elif num ==0:
    print("Factorial of the Number is 1")
else:
    print ("Factorial of a Negative Number cannot be determined")

#4

person_name:input("Enter Your Name:")
print("Hello,",person_name,"! Nice to meet you.")

#5

content =input("Enter Text")

with open('sample_text.txt', 'w') as file:
    file.write(content)

print("Text has been written to sample_text.txt")

#6

with open('sample_text.txt', 'r') as file:
    content = file.read()

print(content)

#7

s=input("Enter a String:")
print("The Length of the String is:-",len(s))

#8

s1=input("Enter first String:")
s2=input("Enter second String:")
print(s1+s2)

#9

s1=input("Enter first String:")
s2=input("Enter second String:")
if s2 in s1:
    print(s2,"is a Substring of",s1)
else:
    print(s2,"is not a Substring of",s1)

#10

s=input("Enter String:")
if s.isupper():
    print("Entered string is already in uppercase")
else:
    print(s,"in uppercase:",s.upper())

#11

n = int(input("Enter a number: "))
a, b = 0, 1
print("First", n, "numbers in the Fibonacci sequence:")
for i in range(n):
    print(a)
    a, b = b, a + b

#12

n = int(input("Enter a number: "))
sum=0
while n>0:
    last_digit=n%10
    sum+=last_digit
    n//=10
print("Sum of digits of the entered number is:",sum)

#13

import datetime
now = datetime.datetime.now()
current_year = now.year
birth_year = int(input("Enter your birth year: "))
if birth_year>current_year:
    print("Wrong birth year entered!")
elif birth_year==current_year:
    print("You are a new born! (Born this year)")
else:
    print("Your age:",current_year-birth_year,"years")

#14

lines = []
print("Enter multiple lines of text (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("You entered:")
for line in lines:
    print(line)

#15

import csv
filename = 'username.csv'
with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(', '.join(row))

#16

s=input("Enter a string:")
all_freq = {}
for i in s:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print("Count of all characters in entered string is :\n ",all_freq)

#17

s=input("Enter a string:")
print("Entered string in title case:",s.title())

#18
str1=input("Enter first String:")
str2=input("Enter second String:")  
if len(str1) != len(str2):  
       flag= False 
elif sorted(str1) == sorted(str2):  
        flag=True  
else:  
        flag=False    
if flag:  
    print("The two strings are anagrams.")  
else:  
    print("The two strings are not anagrams.")

#19

s=input("Enter a string:")
l=[]
for i in s:
    l.append(i)
for i in l:
    if i in '''"!-:;"',.?\""''' :
       l.remove(i)
s1=""
for i in l:
    s1+=i
print("String without punctuation marks:",s1)


#20

try:
    l = []
    while True:
        l.append(int(input("Enter list of numbers and enter any non-integer character to stop entering")))
except:
    print("list of numbers:",l)
    print("sum of numbers:",sum(l))

#21

try:
    l = []
    while True:
        l.append(int(input("Enter list of numbers and enter any non-integer character to stop entering....")))
except:
    print("list of numbers:",l)
    e=int(input("Enter any element:"))
    print("The occurrences of",e,"in",l,"is:",l.count(e))

#22

try:
    l = []
    while True:
        l.append(int(input("Enter list of numbers and enter any non-integer character to stop entering....")))
except:
    print("list of numbers:",l)
    print("The maximum value in",l,"is:",max(l))
    print("The minimum value in",l,"is:",min(l))

#23

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp = eval(input("Enter temperature to be conversted:"))
scale =input("Enter C for celsius to farenheit conversion and F for farenheit to celsius conversion")

if scale.upper() == 'C':
    print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
elif scale.upper() == 'F':
    print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
else:
    print("Invalid scale!")

#24

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

num1 = int(input("Enter first number:") )
num2 = int(input("Enter second number:") )
operator = input("Enter any operator (+,-,*,/)")
print("The result is:",calculator(num1, num2, operator))

#25

def copy_file_contents(source, destination):
    with open(source, 'r') as src:
        contents = src.read()
    with open(destination, 'w') as dest:
        dest.write(contents)

source = 'sample_text.txt'
destination = 'destination.txt'
copy_file_contents(source, destination)
print(f"Contents copied from {source} to {destination}")

#26

string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

starts_with, ends_with = check_prefix_suffix(string, prefix, suffix)

if starts_with:
    print(f"The string starts with the prefix '{prefix}'.")
else:
    print(f"The string does not start with the prefix '{prefix}'.")

if ends_with:
    print(f"The string ends with the suffix '{suffix}'.")
else:
    print(f"The string does not end with the suffix '{suffix}'.")

#27

s=input("Enter a string:")
l=[]
for i in s:
    l.append(i)
print("List of characters of string is:",l)
