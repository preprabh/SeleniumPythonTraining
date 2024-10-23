# 1. Write a Python program to remove all special characters from a string except for alphabets and numbers.
# Breakdown:
#
# Iterate through each character of the string.
# Use a condition to check if the character is alphanumeric, and keep it if true.
import string

in_str = input("Enter a string: ")
if str.isalnum(in_str):
    print("String: ", in_str)
else:
    special = []
    for char in in_str:
        if char in string.punctuation:
            special.append(char)
    print(in_str.replace(''.join(special), ''))


# 2. Write a Python function that accepts a list of numbers and returns the second largest number.
# Breakdown:
#
# Sort the list, but handle the case where there are duplicates.
# Find the second largest number using logic that skips over any duplicates.


def second_largest_number(in_list):
    no_dup = list(set(in_list))
    no_dup.sort(reverse=True)
    if len(no_dup) > 1:
        return no_dup[1]
    else:
        return no_dup[0]


nums = input("Enter some numbers separated by space")
nums_list = nums.split(' ')
stripped_list = [num for num in nums_list if num.strip()]
print(second_largest_number(stripped_list))


# 3. Write a Python program to merge two dictionaries. If there is a common key, sum the values.
# Breakdown:
#
# Loop through both dictionaries.
# If a key exists in both, add their values; otherwise, just add the key-value pair to the result.

dict1 = {'Apple': 'Fruit', 'Orange': 'Fruit', 'Tomato': 'Fruit'}
dict2 = {'Pumpkin': 'Vegetable', 'Potato': 'Vegetable', 'Tomato': 'Vegetable'}
dict3 = dict()


for key1 in dict1.keys():
    if key1 in dict2.keys():
        dict3[key1] = dict1[key1] + dict2[key1]
    else:
        dict3[key1] = dict1[key1]

for key2 in dict2.keys():
    if key2 in dict1.keys():
        dict3[key2] = dict2[key2] + dict1[key2]
    else:
        dict3[key2] = dict2[key2]

print(dict3)


# 4. Write a Python program to read a text file and count the number of lines that contain the word "error".
# Breakdown:
#
# Open and read the file line by line.
# Check if the word "error" is present in each line.
# Keep a count of the lines that match.


def count_word(lines, word):
    count = 0
    for line in lines:
        if word in line:
            count += 1
    return count


word = input("Enter the word to be searched from the file: ")
file_path = r"C:\Users\preet\Downloads\sample.txt"
try:
    with open(file_path) as file:
        lines = file.readlines()
except FileNotFoundError as e:
    print("Exception", e)
except Exception as e:
    print("Exception", e)
print(count_word(lines, word))

# 5. Write a Python class called Car with attributes like model, year, and price. Add a method apply_discount that
# reduces the price by a given percentage. Breakdown:
#
# Use OOP concepts to define the class and methods.
# The method should adjust the price attribute based on the discount percentage provided.

class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def apply_discount(self, percentage):
        discount = (self.price * percentage) / 100
        disc_price = self.price - discount
        return disc_price


nexon = Car('xza', 2020, 1800000)
print(nexon.apply_discount(10))
