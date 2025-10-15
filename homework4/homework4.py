# File: homework4.py

# -- 3: Lists --
# -- 3.1 List Operations
foods = ["pho", "pasta", "mac&cheese", "soup", "burger"]

print(foods[1])

print(foods[-1])

foods.append("steak")

foods.insert(0, "apple")

foods.remove("mac&cheese")

print(len(foods))

for food in foods:
    print(food.upper()) # I got a bug when trying to print out this function because I tried to print it twicw using print(foods[]) which didnt work. I fixed this by deleting that code and using the print function that is on the code currently. (I forgot to copy my error message) :(

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

# -- 3.2 Slicing and Striding --
numbers = list(range(0,21))

def get_first_15(numbers):
    return(numbers[:16])
step1 = get_first_15(numbers)  # My error was figuring out how to call this function. I was calling it incorrectly by writing print(numbers). I fixed it by calling the function correctly by writing print(step1).  (I forgot to copy my error message) :(
    
def get_every_5th(lst):
    return(lst[::5])
step2 = get_every_5th(step1)

def reverse_and_stride(lst):
    reversed_list = lst[-1::-1] # I got an error when trying to print the reversed list because I put [::-1]. I fixed this by putting [-1::-1] instead. (I forgot to copy my error message) :(
    return reversed_list [::3]
step3 = reverse_and_stride(step2)  


# -- 3.3 Nested Lists --
nums = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

# -- 3.3.1 Nested List Operations --
print(nums[2])

print(nums[1][1])

nums.append([10, 11, 12])
print(nums)

def sum_nested(nested_list):
    total = 0
    for row in nested_list:
        for item in row:
            total += item
    return total
result = sum_nested(nums)
print(result)


# -- 3.4 Create a 5x5 List --
def create_5x5_list():
    list_5x5 = []
    number = 1
    for _ in range (5):
        row = []
        for _ in range (5):
            row.append (number)
            number += 1
        list_5x5.append (row)
    return list_5x5
my_list = create_5x5_list()

def replace_multiples_of_3(input_list):
    updated_list = [row[:] for row in input_list]
    for i in range(len(updated_list)):
        for j in range(len(updated_list[i])):
            if updated_list [i][j] % 3 == 0:
                updated_list[i][j] = "?"
    return updated_list

my_updated_list = replace_multiples_of_3(my_list)

def sum_not_question_marks(input_list):
    total_sum = 0
    for row in input_list:
        for element in row:
            if element != "?":
                total_sum += element
    return total_sum
final_sum = sum_not_question_marks(my_updated_list)


# -- Dictionaries --
# -- 4.1 Dictionary Operations --
ages = {
"Katie": 30,
"Mariam": 42,
"Safia": 25,
"Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100

ages["Milana"] = 52

del ages["Mariam"]

for key, value in ages.items():
     print(f"{key}: {value}")


# -- 5.2 In Your VS Code Terminal: --
numbers = list(range(0,21))

def get_first_15(numbers):
    return(numbers[:16])
step1 = get_first_15(numbers)
    
def get_every_5th(lst):
    return(lst[::5])
step2 = get_every_5th(step1)

def reverse_and_stride(lst):
    reversed_list = lst[-1::-1]
    return reversed_list [::3]
step3 = reverse_and_stride(step2)

print(step1)
print(step2)
print(step3)
