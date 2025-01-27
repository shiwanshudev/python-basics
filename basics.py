print("Hello World!")

# Floor Division
floorDivision = 5//2

# Division
division = 5/ 2

print('Floor Division(//): ', floorDivision)
print('Division(/)', division)

remainder = 5 % 2
print('Remainder when 5 divided by 2 is (%): ', remainder)

fiveSquared = 5**2
print('Squared of 5 is: ', fiveSquared)

# Data Types in Python

#Integer
intVal = 5
print('Integer 5: ', intVal)

#Float
floatVal = 5.52
print('This is float value: ', floatVal)

#String
strVal = 'Hello World!'
print('For string we can use both single and double quotes: ', strVal)

#String Concatenation

str1="String 1"
str2="String 2"

print(str1 + ' ' + str2)

#Built In String Functions
#count
bigString='Never say NO, Never say, \'I cannot\', for you are INFINITE. All the power is WITHIN you. You can do anything.'
print('The no. of count of word "Never" in bigString: ',bigString.count('Never'))

#endswith
if bigString.endswith('anything.'):
    print('Ends with string "anything."')
else:
    print('Does not end with string "anything."')

# we can also use tuples here to give multiple values
print(bigString.endswith(('anything.', 'ng.')))

#String formatting with %
message = 'The brand of robot is %s and price is %d. If you go EMI option the price will increase @%.2f per year.'%('Havard', 900, 5.57)
print(message)

#String using format
message = "The brand of robot is {0:s} and price is {1:d}. If you go EMI option the price will increase @{2:.2f} per year.".format('Havard', 900, 5.57)
print(message)

message = "Hi! The brand is {}!".format('Stanford')
print(message)

#Type casting int, float and str.
print(int('5') + 5)
print(float('5.5') + 20)
print(str(5))

#Slicing a list
userAge = [19,20,21,22,23,24,25]
print(userAge[2:4])

#Stepper
print(userAge[1:5:2])

#Removing an index
del userAge[2]
print(userAge)

#Dict
person = {
    'name': 'Ram Kumar',
    'age': 28
}

print(person)

person1 = dict(
    name = 'Shyam Kumar',
    age = 29
)

print(person1)

#Deleting a key value pair
del person1['age']
print(person1)

#Printing multiple lines
print('''
Hello, my name is Ram Kumar.
I am 28 years old.
''')

#Input
name = input("What is your name?")
print('My name is', name + '.')

#Conditionals
a = 5
if(a>5):
    print('a is greater than 5.')
elif(a<5):
    print('a is less than 5.')
else:
    print('a is equal to 5.')

#and or not
if(a < 10  and a > 1):
    print('a is between 1 to 10 excluding 1 and 10.')

if(a == 5 or a == 10):
    print('a is either 5 or 10.')
if(not a == 10):
    print('a is not equal to 10.')

#inline if
b = 12 if a != 5 else 20
print(b)

#range
print(list(range(5)))
print(list(range(0,5,2)))

#for and while loops

for a in range(5):
    print(a)

pets=['Hamster', 'Dog', 'Cat', 'Girrafe', 'Deer']

for i,pet in enumerate(pets):
    print(i, pet)

count = 5
while(count > 0):
    print(count)
    count-= 1

person = {
    'name': 'Ram',
    'age': 28
}

for k in person:
    print(k, person[k])

try:
    num = 12/0
    print(num)
except Exception as e:
    print(e)

#Functions
def checkPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

if checkPrime(81):
    print('81 is prime')
else:
    print('81 is not prime')

if checkPrime(139):
    print('139 is prime')
else:
    print('139 is not prime')

#Local and Global Scopes
globalVar = 5
globalVar2=10
def checkScope():
    # print('No modification',globalVar) Cannot access local variable 'globalVar' where it is not associated with a value
    print('We can access global var but when we try to use it then reassign again, it is error. This is globalVar2 which is not modified inside the function.',globalVar2)
    localVar = 5
    globalVar = 10
    print('Assigned 10 to globalVar inside checkScope fn', globalVar)
# print(localVar) Out of Scope
checkScope()

#Variable length argument list
def addNos(*num):
    sum = 0
    for i in num:
        sum+=i
    return sum

print('Sum is',addNos(1,2,3,4,5))

#Keyworded Argument List, Basically Dict
def addNosKwargs(**kwargs):
    sum = 0
    for k in kwargs:
        sum += int(kwargs[k])
    return sum

print('Sum kwargs: ', addNosKwargs(one=1, two=2))

#Argument order: fargs, *args, **kwargs
#Import and modules

import greet
greet.greet()

# 2nd way
import greet as g
g.greet()

#3rd way
from greet import greet
greet()

#if in some folder
import os
import sys
modulePath = os.path.join(os.getcwd(),'myModule')
if(modulePath not in sys.path):
    sys.path.append(modulePath)
import hello
hello.hello()

#File Operation
f = open('fantasy-story.txt', 'r')
print(f.readline())
f.close()

f = open('fantasy-story.txt', 'r')
for line in f:
    print(line, end='')
f.close()

#Creates a new file called new.txt and adds Hello text.
f = open('new.txt', 'w') 
f.write('Hello')
f.close()

#Appends text and if file does not exist creates it.
f = open('new.txt', 'a')
f.write(' World!')
f.close()

#Opening and reading text files by buffer size
inputF = open('fantasy-story.txt','r')
outputF=open('fantasy-story-2.txt', 'w')

msg = inputF.read(10)

while len(msg):
    outputF.write(msg)
    msg = inputF.read(10) #Read 10 bytes of it

inputF.close()
outputF.close()

#Reading binary files
squirrel = open('squirrel-image.jpg','rb')
newSquirrel = open('squirrel-image-2.jpg', 'wb')

msg = squirrel.read(10)

while len(msg):
    newSquirrel.write(msg)
    msg = squirrel.read(10)

squirrel.close()
newSquirrel.close()

#Rename files by using OS 
import os
os.rename('rename.txt', 'newrename.txt')