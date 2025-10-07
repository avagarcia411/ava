# File: homework3.py

# -- 3: Print Functions --
# -- 3.1 Say Goodbye --
def say_goodbye(name):
    print("Goodbye,", name) 

# -- 3.2 Area of a Circle --
def area_of_circle(radius): 
    pi = 3.14
    area = pi * (radius ** 2)
    print(f"{area}")


# -- 4: Return Functions --
# -- 4.1 Subtract, Multiply, Divide --
def subtract(a, b):
    return a - b

def multiply(c , d):
    return c * d

def divide(e, f):
    return e / f 


# -- 5: Conditionals --
# -- 5.1 What Should I Wear? --
def high_low_temp(temps):
    min_temp = min(temps)
    max_temp = max(temps)
    return (min_temp, max_temp)

# -- 5.2 Check if it's the Weekend --
def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False

# -- 5.3 Fuel Efficiency Calculator --
def fuel_efficiency(distance, fuel):
    return distance/fuel

# -- 5.4 Secret Code --
def encrypt(number):
    last_digit = number % 10
    reminader = number // 10
    
    new_string = str(last_digit) + str(reminader)
    new_number = int(new_string)
    return new_number


# -- 6: Loops --
# -- 6.1 Oski Stole Your Power --
def calculate_power(x, y):
    result = 1
    for _ in range(y):
        result *= x
    return result 

# -- 6.2 Min & Max with Loops --
# -- 6.2.1 For Loops --
def min_value(list): # [1, 5, 3]
    min = list[0]
    for value in list:
        if value < min:
            min = value
    
    return min


def max_value(list): # [1, 5, 3]
    max_value = list[0]
    for value in list:
        if value > max_value:
            max_value = value
    
    return max_value

# -- 6.2.2 While Loops --
def min_while(numbers):
    i = 0
    min = numbers[0]
    while i < len(numbers):
        if numbers[i] < min:
            min = numbers[i]
        i+=1
    return min


def max_while(numbers):
    i = 0
    max = numbers[0]
    while i < len(numbers):
        if numbers[i] > max:
            max = numbers[i]
        i+=1
    return max


# -- 6.3 Calculate the Sum --
def sum_digits(number):
    sum = 0

    while number != 0:
        sum += number % 10
        number = number // 10

    return sum


# -- 7: Running Your Script --
def encrypt(number):
    last_digit = number % 10
    reminader = number // 10
    
    new_string = str(last_digit) + str(reminader)
    new_number = int(new_string)
    return new_number

print(encrypt(12345)) # the result is 51234 (12345 with the last digit moved to the front)
