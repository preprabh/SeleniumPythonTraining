# Question 1:
# Write a Python program to print numbers from 1 to 10 using a for loop.

for i in range(11):
    print(i)

# Question 2:
# Create a program that prints the multiplication table of a given number using a while loop.

num = int(input("Which number's multiplication do you need?"))
i = 1
while num > 0 and i <= 10:
    print(i, '*', num, '=', i * num)
    i = i + 1

# Question 3:
# Write a Python script to find the sum of all even numbers between 1 and 50 using a for loop.

sum_even = 0
for i in range(51):
    if i % 2 == 0:
        sum_even += i
print("Sum of all even numbers from 1 to 50 is:", sum_even)

# Question 4:
# Implement a program that prints the Fibonacci sequence up to the 10th term using a while loop.
# 1,1,2,3,5,8,13,21.....

fib = [1, 1]
num = int(input("Till which number to print Fibonacci series: "))
i = 2
while i < num:
    next_number = fib[i - 2] + fib[i - 1]
    if next_number <= num:
        fib.append(next_number)
    else:
        break
    i += 1
print("Fibonacci Series till ", num, ": \n", fib)

# def fibonacci_unto_n(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#
# n = int(input("Enter a number: "))
# fibonacci_unto_n(n)

# Question 5:
# Create a program that checks if a number is a prime number using a for loop.

num = int(input("Enter a number to check if it's prime or not: "))

prime = 1
if num >= 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, " is not a prime number")
            prime = 0
            break
else:
    print("Invalid number")

if prime == 1:
    print(num, " is a prime number")

# Question 6:
# Write a Python script to print the square of numbers from 1 to 5 using a while loop.
#
num = 1
while 1 <= num <= 5:
    sq = num * num
    print(sq)
    num += 1

# Question 7:
# Implement a program to find the largest element in a list using a for loop.

num_list = [56, 67, 98, 23, 45, 1200, 2500, 10000, 23, 78]

i = 1
largest = 0
for i in range(len(num_list)):
    if largest < num_list[i - 1] < num_list[i]:
        largest = num_list[i]
        break
    elif num_list[i - 1] < largest < num_list[i]:
        largest = largest
        break
    else:
        largest = num_list[i - 1]
        break
print(largest)


# Question 8:
# Write a Python function that takes a list of numbers and returns the product of all the elements using a while loop.
# [2,3,4,5] = 120

def product_list(prod_list):
    prod = 1
    for element in range(len(prod_list)):
        prod = prod * prod_list[element]
    return prod


num_list_mul = []
print("Enter 10 numbers, with each number in a line")

for i in range(10):
    numbers = int(input())
    num_list_mul.append(numbers)
print("List is : ", num_list_mul)
result = product_list(num_list_mul)
print(result)
