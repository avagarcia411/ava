# File: homework1. py

# --- 3.1 Variables and Data Types ---
a=10
print(a)
print(type(a)) # a is an intiger, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a number with a decimal

c = 3j
print(c)
print(type(c)) # c is a complex, the data type has a number and a letter

d = "hello"
print(d)
print(type(d)) # d is a string, a collection of words

e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a data type that can store a sequence of items

f = {"name": "Ava", "favorite fruit": "apple"}
print(f)
print(type(f)) # f is a dictionary, a data type that stores data in pairs of keys and its corresponding value

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, a list of items with a defined order

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a data type that can store a sequence of items 

i = True
print(i)
print(type(i)) # i is a Boolean, a data type that represents two possible values: True or False

j = None
print(j)
print(type(j)) # j is a NoneType, a data type that represents the absence of a value

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a data type that can store a sequence of items

l = str(14)
print(l)
print(type(l)) # l is a string, a collection of words

m = 1e4
print(m)
print(type(m)) # m is a float, a number with a decimal 

#Questions 3.1:
# 1. I found 9 data types.
# 2. Intiger, float, complex, string, list, dictionary, tuple, Boolean, and NoneType
# 3. Variables b and m are both floats, variables d and l are both strings, and variables e, h, and k are all lists
# 4. The data type of l is a string. It is not an intiger because str() automatically converts the intiger and represents it as a string
# 5. I chose to create the data type set. 
thisset = {"hi", "hello", "hey"}
print(thisset)
print(type(thisset)) # This is a data type set which is a data type that is used to store multiple items in a single variable.


# --- 3.2 Booleans ---
print(10>9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
print(bool("abc")) # True,the bool will evaluate a string that is not considered empty as true
print(bool(123)) # True, and number other than zero is considered truth in Boolean
print(bool(['apple', 'cherry', 'banana'])) # True, the list is not empty (I also had to format the list differently becuause I ran into an error)
print(bool(True)) # True, true is already a Boolean value representing true
print(bool(False)) # False, false is already a Boolean value representing false
print(bool(0)) # False, the value 0 represents "nothing"
print(bool("")) # False, the bool will evaluate an empty string as false
print(bool(" ")) # True, the bool will evaluate a string that is not considered empty as true
print(bool(())) # False, empty dictionaries are considered false
print(bool([])) # False, empty dictionaries are considered false
print(bool({})) # False, empty dictionaries are considered false
print(bool(True and False)) # False, the bool will only return true in the "and" statement if both options are true
print(bool(True and True)) # True, both options must be true
print(bool(False and False)) # False, both options must be false
print(bool(True or False)) # True, true is first in "true or false"
print(bool(True or True)) # True, there are only two options, both being true
print(bool(False or False)) # False, there are only two options, both being false
print(bool(not(False))) # True, not false means true
print(bool(not(True))) # False, not true means false

#Questions 3.2:
# 1. I notice that strings that is not empty is true, and a string that is empty is false. Empty dictionaries or lists will be false.
# 2. The expressions bool("") and bool(" ") surprised me the most, I thought they would have the same answer before I saw the results
# 3. print(bool(['yes', 'no'])) This is true because a list that is not empty will return as true
# 4. print(bool(0+0)) This is false because 0+0 is still equal to 0, which means it will return as false


# --- 3.3 Operators ---
# -- 3.3.1 Arithmetic Operators --
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs division
print(5 % 2) # 1, % returns the remainder of the division from the left number by the right number
print(3 ** 2) # 9, ** performs the square of the first number
print(15 // 2) # 7, // performs floor division (divides the first number by the second and rounds the result down to nearest whole number)

# -- 3.3.2 Comparison Operators --
print(5 == 2) # False, 5 is not equal to 2
print(10 != 10) # False, != represents "not equal to", so since 10 is equal to 10, it will return as false
print(2 < 5) # True, 2 is less than 5
print(12 > 5) # True, 12 is greater than 5
print(5 <= 6) # True, 5 is less than or equal to 6
print(1 >= 10) # False, 1 is not greater than or equal to 10

# -- 3.3.3 Assignments Operators --
x = 5
x += 5 
print(x) # 10, this is a shorthand for x = x + 5

x = 5
x -= 4
print(x) # 1, this is a shorthand for x = x - 4

x = 5
x *= 3
print(x) # 15, this is a shorthand for x = x times 3

# -- 3.3.4 Logical Operations --
# 1. The operator "and" is used to combine conditional statements 
o = 5 
p = 6
q = 7
print((o<p) and (p<q)) # This is true because 5 is greater than 6, and 6 is greater than 7
print((o<q)and(p>q)) # This is false because 5 is greater than 7 (true) but 6 is not greater than 7 (false)

# 2. The operator "or" is used to combine two or more expressions
o = 5 
p = 6
q = 7
print((o<p) or (p>q)) # This is true because 5 is less than 6. Even though the second statement is wrong, the or means that it will still be seen as true
print((o>q) or (p>q)) # This is false because both 5 is greater than 7 and 6 is greater than 7 are both false statements

# 3. The operator "not" "performs boolean negation", meaning that is the evaluation is true, the return will be false, and vice verse

# More Questions:
# 1. / will perform division, and // will perform floor division (divides the first number by the second and rounds the result down to nearest whole number)
# 2. % just returns the remainder of the division, and // rounds the result from the division, not gives the remainder
# 3. You would use % (if you calculate (15 % 6) you will get the result of 3, which is the remainder of 15 divided by 12)
# 4. Assignment operators assign values to variables. These are ways to perform an operation (like subtraction or multiplication) and update the variable in one step


# --- 3.4 Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1:3]) # Prints: el
print(my_string[0:5:2]) # Prints: hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello

#Questions:
# 1. Slicing is a way to extract a portion of a sequence. I sliced my string for the manipulations 2 through 9.
# 2. 
name = "Oski"
print("Hello, my name is", name)

# 3.
name = "Oski"
print(f"Hello, my name is", name)

# 4. The output for the two questions above are the same, but the second print statement has an f-string. An f-string makes formatting more readable by allowing direct embedding of variables 


# --- 3.5 Terminal Commands ---
# cd
# Changes directories. Use it to move from one folder to another 
# Example: cd Desktop

# ls
# Lists contents of a directory. 
# Example: use ls to list the contents of the python_decal_fa25/yourname/ folder structure

# ls -a
# Lists the contents of the directory and the rights and owner
# Example: use ls to see who the owner of python_decal_fa25 is

# mkdir
# Makes directories. 
# Example: mkdir homework1

# cat
# Concatenate files. Joins the contents of multiple files and prints them to the standard output
# Example: cat datatypes.py

# pwd
# Print the current working directory, aka print the folder you are currently in
# Example: use pwd to see that you are currently in /Users/ava

# cd ..
# Change the current working directory to its parent directory
# Example: use cd .. to move from the directory ava to python_decal_fa25

# cd .
# Change directory to the current directory
# Example: cd . homework1

# cd ∼ 
# Changes the current directory to the home directory
# Example: cd desktop

# cp
# Used to copy files and directories
# Example: cp homework1

# mv
# Move or rename files and folders
# Example: mv [homework1] [python_decal_25]

# rm
# Remove files and directories
# Example: rm homework1

# clear
# Remove all elements from a data structure, like a list or set
# Example: 
# my_set = {"hi", "hello"}
# my_set.clear()
# print(my_set)


# grep
# Used to search for specific text patterms within files
# Example: grep "hello" homework1


# Questions:
# 1.
# range is used to generate a sequence of intigers starting from 0 by default to n where n is not included in the generated numbers. 
for i in range(12):
    print(i)

# round is used to round a number to a given precision in decimal digits.
print(round(5.252525, 2)) # The result is 5.25 because we wanted to round that number to have two decimal places

# capitalize is used to capitalize the first letter of the string if it's lowercase.
my_string = "go bears"
capitalized_string = my_string.capitalize ()
print(capitalized_string)

# 2. ls lists the contents, while ls -a lists the contents and the rights and owner

# 3. A hidden file means that Git knowd about the existance of the file and is keeping a history of its changes

# 4. 
# -o lets you run a script while ignoring the assert statements. This is used to enforce certain conditions that the program may need to function correctly
# -w is used to ignore all the warnings that a program could throw. You can turn off warnings temporarily if you want to focus on development
# -x is used to skip the first line in a script. Useful for ignoring comments that could be present at the start of a script