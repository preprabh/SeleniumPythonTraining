# 1. Write a Python program to find duplicate elements in a list.
from collections import defaultdict

elements = input("Enter some numbers separated by space")
elements_list = elements.split(' ')
stripped_list = [element for element in elements_list if element.strip()]
dup = [element for element in stripped_list if stripped_list.count(element) >= 2]
print(set(dup))


# 2. Write a Python function to reverse a string without using any built-in functions.
def reverse_string(str):
    rev_str = []
    for char in str[len(str) - 1::-1]:
        rev_str.append(char)
    print(''.join(rev_str))


str = input("Enter a string: ")
reverse_string(str)

# 3. Write a Python program to count the number of occurrences of each word in a given text file.

# Breakdown:
#
# Read a file line by line.
# Split each line into words.
# Use a dictionary to keep track of word frequencies.

file_path = r"C:\Users\preet\Downloads\sample.txt"
f = open(file_path, "r")
words_count = defaultdict(int)
lines = f.readlines()
for line in lines:
    words = line.split()
    for word in words:
        words_count[word] += 1

for word, cnt in words_count.items():
    print(f"{word} : {cnt}")


# 4. Write a Python program to find the largest and smallest numbers in a list without using built-in functions like
# min() or max().


def large_small(sample):
    largest = sample[0]
    smallest = sample[0]

    for num in sample:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest


numbers = input("Enter some numbers separated by space")
numbers_list = numbers.split(' ')
sample = [int(number) for number in numbers_list if number.strip()]

big, small = large_small(sample)
print("Largest : ", big)
print("Smallest: ", small)


# 5. Write a Python function that takes two lists and returns True if they have at least one common element.

def input_list():
    sample = input("Enter some numbers separated by space")
    sample_list = sample.split(' ')
    final_list = [int(number) for number in sample_list if number.strip()]
    return final_list


def compare_list(comp_list1, comp_list2):
    for num in comp_list2:
        if int(num) in comp_list1:
            return True
    return False


list1 = input_list()
list2 = input_list()
print(compare_list(list1, list2))
