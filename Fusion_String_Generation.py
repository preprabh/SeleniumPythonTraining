import random

print("Welcome to the Fusion Restaurant")
cuisine = input("Enter your favourite cuisine: ")
fruit = input("Enter your favourite fruit: ")

dish = []

for i in range(random.randint(5, 10)):
    letter = random.choice(cuisine.upper()+fruit.upper())
    dish.append(letter)

print("Please try our specially curated dish ", ''.join(dish))

