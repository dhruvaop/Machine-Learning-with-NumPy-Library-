str = "Python"
for i in str:
    print(i)
    L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter the number"))
for i in L1:
    c = n*i
    print(c)
print("Hello world")
a = 10  # this is first var
b = 20  # this is second var
c = a+b
print("Addition is: ", c)
name = input("Enter your name: ")
print("Your name: ", name)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a+b
print("Addition is: ", c)
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a > b and a > c:
    print("a is largest")
if b > a and b > c:
    print("b is largest")
if c > a and c > b:
    print("c is largest")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are elligible to vote")
else:
    print("Sorry! you have to wait")

str = "python"
for i in str:
    print(i)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list1:
    print("hello")

for i in range(1, 11):

    print(i)
    if i == 5:
        break
i = 1
while i <= 5:
    print(i)
    i = i+1
n = int(input("Enter the number"))
for i in range(1, 11):
    c = n*i
    print(n, "*", i, "=", c)
    n = int(input("Enter the number"))
for i in range(2, n, 2):
    print(i)

    n = int(input("Enter the number"))
while n > 0:

    print(n)
    if n == 10:
        break
    n = n-1

for i in range(10):  # range(start,stop,step) 0 to stop-1
    print(i)

for i in range(1, 10):  # 1 to stop-1
    print(i)

for i in range(3, 33, 3):  # start to stop-step   incremented by step
    print(i)

    n = 1
while n <= 5:
    print(n)
    n = n+1
else:
    print("Loop is exhausted")

L1 = [10, 20, 30, "India", "US"]
print(type(L1))

# The lists are Ordered
L1 = [10, 20, 30, 40, 50]
L2 = [20, 30, 50, 40, 10]
print(L1 == L2)

# the element of the list can access by index
A1 = [100, 200, 300, 400, 500, "India"]
print(A1[3])

B1 = [100, 200, 300, 400, "India", "US"]

print(B1[3:6])  # start index to End index-1

print(B1[2:])

print(B1[:4])

# You can Update the list element,List are mutable
C1 = [10, 20, 30, 40, 50, 60]
C1[2] = 100
print(C1)

C1.append(200)  # Add in the last
print(C1)

C1.insert(2, 400)
print(C1)

D1 = [45, 46, 47, 48, 49, 50]
D1.remove(47)
print(D1)


C1 = [10, 20, 30, 40, 50, 60]
C2 = [100, 200, 300, 400]
print(C1*2)  # Repetition

print(C1+C2)  # Concatenattion

print(500 in C1)  # Membership

print(len(C1))  # Length

# Built in Fuction of List

S1 = [1, 2, 3, 4, 5]
S2 = [10, 20, 30, 40, 50]
print(max(S2))
print(len(S1))
print(min(S1))

"""Write the program to remove duplicate elements in the list

test_list = [1, 10, 3, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))
res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]
print("The list after removing duplicates : " + str(res))

"""
"""Write the program to find sum of the elements in the list

list1 = [5, 4, 3, 2, 1]
total = sum(list1)
print("Sum of all elements in given list: ", total)

"""
