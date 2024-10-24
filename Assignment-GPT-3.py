# 1. Simple Question: Find the Maximum Number in a List
# Write a Python program that takes a list of numbers and returns the maximum number.
#
# Example:
# Input: [12, 5, 9, 42, 3]
# Output: 42
#

num = input("Enter numbers separated by a space: ")
num_list_tmp = num.split(' ')
num_list = [int(number) for number in num_list_tmp if number.strip(' ')]
print(max(num_list))

# 2. Simple Question: Check if a String is a Palindrome
# Write a Python program to check if a given string is a palindrome (a word that reads the same forwards and backwards).
#
# Example:
# Input: "racecar"
# Output: True
#

str = input("Enter a string to check if it's palindrome or not: ")
if str.lower() == str[::-1].lower():
    print("It's a palindrome")
else:
    print("Not a palindrome")


# 3. Medium Question: Count Vowels in a String
# Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string.
#
# Example:
# Input: "Automation Testing"
# Output: 8
#

in_str = input("Enter a string: ")
vow_count = 0
for char in in_str:
    if char in ('a', 'e', 'i', 'o', 'u'):
        vow_count += 1
print("Vowel Count is: ", vow_count)

# 4. Medium Question: Reverse a List
# Write a Python program that takes a list of integers and returns a new list with the elements in reverse order.
#
# Example:
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
#
num = input("Enter numbers separated by a space: ")
num_list_tmp = num.split(' ')
num_list = [int(number) for number in num_list_tmp if number.strip(' ')]
print(num_list[::-1])

# 5. Hard Question: Find the First Non-Repeating Character in a String
# Write a Python program that finds the first character in a string that doesn’t repeat.
#
# Example:
# Input: "automation"
# Output: 'u'

in_str = input("Enter a string: ")
for char in in_str:
    if in_str.count(char) == 1:
        print(char)
        break

# 6. Simple Question: Sum of Even Numbers in a List
# Problem:
# Write a Python program to find the sum of all even numbers in a given list. For example, given the list [1, 2, 3, 4, 5, 6], the sum of even numbers should be 12 (2 + 4 + 6).
#

in_list = [3,4,5,6,7,8,9,10]
sum_even = 0
for num in in_list:
    if num % 2 == 0:
        sum_even += num
print("Sum of even numbers is: ", sum_even)


# 7. Simple Question: Check if a String Contains a Substring
# Problem:
# Write a Python program to check if a given substring exists within a string. For example, check if the word "test" exists in the string "this is a test case."
#

in_str = input("Enter a sentence: ")
in_substr = input("Enter a word to be checked in the sentence: ")
if in_substr in in_str:
    print(f"Yaayy!! '{in_substr}' is present in '{in_str}'")
else:
    print("Ooops!! the word is not present in the sentence")


# 8. Medium Question: Merge Two Lists and Remove Duplicates
# Problem:
# Write a Python program to merge two lists and remove any duplicate elements. For example, merging [1, 3, 5, 7] and [3, 7, 9, 11] should result in [1, 3, 5, 7, 9, 11].
#

list1 = [2, 3, 4, 5, 6, 7, 2, 1, 3]
list2 = [2, 3, 6, 7, 8, 9, 10, 11, 1, 23, 5]

print(list(set(list1 + list2)))

# 9. Medium Question: Find the Factorial of a Number Problem: Write a Python program to calculate the factorial of a
# given number. The factorial of a number n is the product of all positive integers less than or equal to n. For
# example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
#

def factorial(num1):
    if num1 == 0 or num1 == 1:
        return 1
    else:
        return num1 * factorial(num1 - 1)


num = int(input("Enter a number: "))
print(factorial(num))

# 10. Hard Question: Find All Pairs of Numbers That Sum to a Target
# Problem:
# Write a Python program to find all pairs of numbers in a list that add up to a given target value. For example, given the list [1, 2, 3, 4, 5, 6] and the target 7, the program should return pairs like (1, 6), (2, 5), and (3, 4).

in_list = [4, 5, 6, 7, 8, 3, 2, 1, 1, 2, 3, 4]
target_value = int(input("Enter a number :"))
num_pair = []
for i in range(len(in_list)):
    for j in range(1, len(in_list)):
        if in_list[i] + in_list[j] == target_value:
#            if (in_list[i], in_list[j]) or (in_list[j], in_list[i]) not in num_pair:
#                num_pair.append((in_list[i], in_list[j]))
            if (in_list[i], in_list[j]) not in num_pair:
                if (in_list[j], in_list[i]) not in num_pair:
                    num_pair.append((in_list[i], in_list[j]))
# Print only the pairs
for pair in num_pair:
    print(pair)
