'''Assignment - 8 Full Stack Web Development using Python MySirG

                   While Loop'''

# (Q.1) Write a python script to print MySirG 5 times on the screen
a=int(input("Enter your number:"))

while a:
 print("MysirG")
 a-=1
print()

# (Q.2) Write a python script to print first 10 natural numbers
i = 1
while(i<=10):
    print(i)
    i += 1

#(Q.3) Write a python script to print first 10 natural numbers in reverse order

number = int(input("Please Enter any Number: "))
i = number

print("List of Natural Numbers from {0} to 1 in Reverse Order : ".format(number)) 

while ( i >= 1):
    print (i, end = '  ')
    i = i - 1

# (Q.4) Write a python script to print first 10 odd natural numbers
i = 1

while(i <= 10):
    print(2 * i - 1)
    i = i + 1
# (Q.5) Write a python script to print first 10 odd natural numbers in reverse order
i = 10

while(i >= 1):
    print(i)
    i = i - 1
# (Q.6) Write a python script to print first 10 even natural numbers
i = 1
while(i <= 10):
    print(2 * i)
    i = i + 1
#(Q.7) Write a python script to print first 10 even natural numbers in reverse order

i = 10
while(i >= 2):
    print(2 * i)
    i = i - 1

# (Q.8)Write a python script to print squares of first 10 natural numbers Getting input from users

N = int(input("Enter value of N: "))

# calculating sum of square 
sumVal = 0
for i in range(1, N+1):
    sumVal += (i*i)

print("Sum of squares = ", sumVal)

# (Q.9)Write a python script to print cubes of first 10 natural numbers
# Python program for sum of the 

# cubes of first N natural numbers

# Getting input from user
N = int(input("Enter value of N: "))

# calculating sum of cubes 
sumVal =  (int)( pow(( (N * (N+1))/2 ) , 2) )
print("Sum of cubes =",sumVal)

# (Q.10)Write a python script to print first 10 multiples of 5
multiples=[] 
for i in range(1, 101): 
    if i%5==0: 
        multiples.append(i) 
print(multiples) 