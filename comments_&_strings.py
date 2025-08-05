            ### Comments and Strings ###

# Obs.: Since chapter 3 (Comments) and chapter 4 (strings) are small chapters I´ll put them together!


    # Chapter 3 - Comments

# This is a comment (simple comment)
x = 10  # This is also a comment (inline comment)

'''This is a multi-line
comment'''
"""This is also a multi-line 
comment"""


"""This is a docstring one-liner"""

"""
This is a docstring
and it have multiple lines
"""

#IT IS IMPORTANT TO KNOW THAT """...""" or '''...''' ARE STRINGS, BUT IF THEY ARE ALONE AND NOT ATTRIBUTED THE INTERPRETER WILL
# IGNORE THE CONTENT AS IF THEY WERE COMMENTS, BUT THEY ARE NOT REALLY COMMENTS, IT IS JUST A TRICK.

    
    # Chapter 4 - Strings

# Creating strings
name = "Marcelo"
first_name = "Marcelo"
last_name = "Lucchesi"
triple_double_quotes = """multi-line
string"""

# Converting an interger to a string
number = 5
str(number)

# Backlashes - Escape Sequences
print("Hello\bWorld")  # \b (Backspace) -> HellWorld
print("Hello\nWorld")  # \n (Line feed) -> Hello
#World
print("Hello\rWorld")  # \r (Carriage Return) -> World
print("Hello\tWorld")  # \t (Tab) -> Hello    World

# Backlashes - Escape Quotes
print('This string has a single quote, \', in the middle') # This string has a single quote, ', in the middle

print ("This String has a single quote, ', in the middle") # It is better to mix single and double quotes in cases like this

