# Write a Python program to print the below patterns:


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print(" ")


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


for i in range(1, 6):
    for j in range(1, 6):
        if i >= j:
            print(j, end=' ')
    print("")

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for i in range(1, 6):
    for j in range(5, 0, -1):
        if i >= j:
            print(j, end=' ')
    print("")


# Write a Python program to count the occurrences of a specific character in a given string.
sentence = input("Enter a sentence: ")
letter = input("Which letter do you want to count?")
print(sentence.count(letter))

# Write a Python program to reverse a given string. # range[:5]

sentence = input("Enter a sentence: ")
print("Reverse string is: ", sentence[::-1])

# Write a Python program to check if a given string is a palindrome or not. for e.g. - 123321 pep

sentence = input("Enter a string to check palindrome: ")
if sentence.lower() == sentence[::-1].lower():
    print("Yay!! It's a Palindrome")
else:
    print("Not a Palindrome!")


# Write a Python program to remove all whitespaces from a given string.

sentence = input("Enter a sentence: ")
print("All whitespaces removed: ", "".join(sentence.split()))
