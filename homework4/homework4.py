# File: homework4.py

# -- 3: Lists --
# -- 3.1 List Operations
foods = ["pho", "pasta", "mac&cheese", "soup", "burger"]

print(foods[1])

print(foods[-1])

foods.append("steak")
print(foods)

foods.insert(0, "apple")
print(foods)

foods.remove("mac&cheese")
print(foods)

print(len(foods))

for food in foods:
    print(food.upper())

# print(foods[])

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

# -- 3.2 Slicing and Striding --
numbers = list(range(0,21))

