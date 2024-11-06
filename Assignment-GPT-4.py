# 1. Simple Question: Find the Sum of Digits in a Number
#
from operator import itemgetter

def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number = number // 10  # Using floor division for integer/round division
    return sum_digits


num = int(input("Enter a number: "))
sum_digits = sum_of_digits(num)
# to get the result in single digit
if sum_digits >= 10:
    print(sum_of_digits(sum_digits))
else:
    print(sum_digits)


# 2. Simple Question: Find Common Elements in Two Lists
# Problem:
# Write a Python program to find and display the common elements between two lists. For example, given the lists [1, 3, 5, 7, 9] and [3, 4, 5, 6], the output should be [3, 5].
#

while True:

    list1_in = input("Enter numbers separated by a space: ")
    list1_tmp = list1_in.split(' ')
    list1 = [int(number) for number in list1_tmp if number.strip(' ')]

    list2_in = input("Enter numbers separated by a space: ")
    list2_tmp = list2_in.split(' ')
    list2 = [int(number) for number in list2_tmp if number.strip(' ')]

    if len(list1) == len(list2):
        list3 = []
        for num in list1:
            if num in list2:
                list3.append(num)
        print("Common elements list: ", list(set(list3)))
        break
    else:
        print("Please enter equal numbered elements in each list")


# 3. Medium Question: Remove Duplicates from a List
# Problem:
# Write a Python program to remove duplicate elements from a list and return a list of unique values. For example, given the list [1, 2, 2, 3, 4, 4, 5], the output should be [1, 2, 3, 4, 5].
#


str_inp = input("Enter numbers separated by a space: ")
str_list_tmp = str_inp.split(' ')
str_list = [str1 for str1 in str_list_tmp if str1.strip(' ')]
print(set(str_list))


# 4. Medium Question: Find the Longest Word in a Sentence
# Problem:
# Write a Python program to find the longest word in a given sentence. For example, in the sentence "Automation testing is essential," the longest word is "Automation."
#

str_in = input("Enter a sentence: ")
words = str_in.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)

# 5. Hard Question: Sort a List of Dictionaries by a Key
# Problem:
# Write a Python program to sort a list of dictionaries based on a specified key. For example, if given a list of dictionaries like [{‘name’: ‘Alice’, ‘age’: 25}, {‘name’: ‘Bob’, ‘age’: 20}], sort it by the age key, so the output would be [{‘name’: ‘Bob’, ‘age’: 20}, {‘name’: ‘Alice’, ‘age’: 25}].
#

list_dict = [{'Name': 'Alice', 'Age': 25}, {'Name': 'Bob', 'Age': 20}, {'Name': 'Mary', 'Age': 32}]

dict_keys = sorted(list_dict[0].keys())
key_to_sort = dict_keys[0]


#sorted_list = sorted(list_dict, key=lambda k: k[key_to_sort], reverse=True)

sorted_list = sorted(list_dict, key=itemgetter(key_to_sort))
print(sorted_list)


