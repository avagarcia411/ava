# -- 3: Homework 1 + 2 Review --
# -- Vocabulary Review --
# 1. Git vs. GitHub: Git is a version control system that tracks your changes in your code over time and works locally on your computer. It also lets you make changes. GitHub is a website that hosts Git repositories online and lets you share, store, and collaborate on projects.
# 2. Terminal vs Command Line: the terminal is an application that provides an interface for interacting with your computer's operating system. The command line is the specific line in the terminal where you enter commands. You can type instrictions for your computer to execute.
# 3. Local vs. Remote Repository: the local repository is a copy of your project on your own computer. A remote repository is a central version that can be shared and collaborated on.
# 4. Version Control: how you track and manage changes to files and projects over time. 
# 5. Staging Area: the in between area where changes are prepared before being commited to the repository.
# 6. git add: tells the repository that we have made a change.
# 7. git commit: commiting our move and looks like a deletion to Git.
# 8. git push: saves your changes remotely.
# 9. git status: tells you the status of your repository.
# 10. git pull: updates your local repository with changes from a remote repository.
# 11. pwd: print the current working directory, aka print the folder you are currently in.
# 12. ls: lists contents of a directory. 
# 13. cd: changes directories. Use it to move from one folder to another.
# 14. nano: a text editor that you can operate directly in the terminal.
# 15. touch: creates empty files.
# 16. mv: move or rename files and folders.
# 17. rm: remove files and directories.
# 18. cat: concentrate files. Joins the contents of multiple files and prints them to the standard output.

# -- 3.2 A Directory Tree --
# Questions:

# - You can use the cwd command to tell you your current working directory.

# - The ls command will list all the files in the current working directory.

# - cd .., and then git pull

# - mv homework.py ../judy_decal/homework/

# - cd ../judy_decal/homework/

# - Use the cat homework.py command to see the contents.

# - git add . , git commit -m "Finished Homework" , git push

# - git pull , git push

# - cd Recent/


# -- 4: Homework 3 Review -- 
# -- 4.1 Data Types --
def get_data_type(data):
    return str(type(data)).split("'")[1]

# -- 4.2 Conditionals --
def even_or_odd(integer):
    if integer % 2 == 0:
        return "Even"
    else: 
        return "Odd"
    

# -- 5: Loops --
def sum_digits(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


# -- 6: Homework 4 Review --
# -- 6.1 Lists --
def duplicate_list(list):
    duplicated_list = []
    for item in list:
        duplicated_list.append(item)
        duplicated_list.append(item)
    return duplicated_list

# -- 6.2 Debugging --
def square(num): # they forgot to add the : to the end of the first line
    return num * num


# -- 7: Running Your Code --
def duplicate_list(list):
    duplicated_list = []
    for item in list:
        duplicated_list.append(item)
        duplicated_list.append(item)
    return duplicated_list
print(duplicate_list(['a', 'b', 'c']))