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
and it has multiple lines
"""

# IT IS IMPORTANT TO KNOW THAT """...""" or '''...''' ARE STRINGS, BUT IF THEY ARE ALONE AND NOT ATTRIBUTED THE INTERPRETER WILL
# IGNORE THE CONTENT AS IF THEY WERE COMMENTS, BUT THEY ARE NOT REALLY COMMENTS, IT IS JUST A TRICK.

    

            # Chapter 4 - Strings

    # Creating strings #
name = "Marcelo"
first_name = "Marcelo"
last_name = "Lucchesi"
triple_double_quotes = """multi-line
string"""

# You can use help() function to see all the python documentation. -> Example: help(str) - shows documentation about strings

# Converting an integer to a string
number = 5
str(number)

# Backslashes - Escape Sequences
print("Hello\bWorld")  # \b (Backspace)         -> Output: 'HellWorld'
print("Hello\nWorld")  # \n (Line feed)         -> Output: 'Hello
#World'
print("Hello\rWorld")  # \r (Carriage Return)   -> Output: 'World'
print("Hello\tWorld")  # \t (Tab)               -> Output: 'Hello    World'

# Backslashes - Escape Quotes
print('This string has a single quote, \', in the middle') 
# Output: This string has a single quote, ', in the middle

print ("This String has a single quote, ', in the middle") # It is better to mix single and double quotes in cases like this
# Output: This string has a single quote, ', in the middle


    # String Methods #
name = "Marcelo"
name.capitalize()                       # Output: Marcelo           (capitalizes the first letter)
name.upper()                            # Output: MARCELO           (converts to uppercase)
name.lower()                            # Output: marcelo           (converts to lowercase)
name.swapcase()                         # Output: mARCELo           (swaps the case of each letter)
name.isalpha()                          # Output: True              (checks if all characters are alphabetic)
name.strip()                            # Output: Marcelo           (removes leading and trailing whitespace)
name.replace("Marcelo", "Marcelinho")   # Output: Marcelinho        (replaces the first string with the second string)
name.split()                            # Output: ['Marcelo']       (splits the string into a list of words)
name.split("e")                         # Output: ['Marc', 'lo']    (splits the string at the letter 'e')
name.find("a")                          # Output: 2                 (finds the first occurrence of 'a'  and returns its index)
name.index("a")                         # Output: 2                 (finds the first occurrence of 'a' and returns its index, raises an error if not found)
name.count("a")                         # Output: 2                 (counts the number of occurrences of 'a')

# You can use dir() function to see all the methods available for a string -> Example: print(dir(str))
    

    # String Formatting #

# Formatting using %s (printf-style) -> This type of formatting is not recommended anymore, but it is still used in some places
name = "Marcelo"
print("My name is %s" % name)  
# Output: My name is Marcelo

# Passing an integer into a string and automatically converting it to string
age = 18
print ("You must be at least %s years old to enter." % age)  
# Output: You must be at least 18 years old to enter.

# Using 2 printf-styles being one %i to guarantee that the value is an integer
name = "Marcelo"
age = 41
print("My name is %s and I am %i years old." % (name, age))  
# Output: My name is Marcelo and I am 41 years old.

# When using dictionary
print("Hello %(first_name)s. You must be at least %(age)i to continue." %{"first_name": name, "age": age})  
# Output: Hello Marcelo. You must be at least 18 to continue.


# Formating using .format() method
age = 18
name = "Marcelo"
print("Hello {}. You must be at least {} to continue!" .format(name, age))  
# Output: Hello Marcelo. You must be at least 18 to continue!
# This example uses positional arguments.

# Using named arguments
age = 18
name = "Marcelo"
print("Hello {first_name}. You must be at least {age} to continue!" .format(first_name=name, age=age)) 
# Output: Hello Marcelo. You must be at least 18 to continue!

# When using dictionary -> Double asterisks to unpack the dictionary
print("Hello {first_name}. You must be at least {age} to continue!" .format(**{"first_name" : name, "age":age})) 
# Output: Hello Marcelo. You must be at least 18 to continue!

# Repeating the same value
first_name = "Marcelo"
print("Hello {first_name}. Why do they call you {first_name}?" .format(first_name=first_name))  
# Output: Hello Marcelo. Why do they call you Marcelo?

# Interpolating values using numbers
print("Hello {1}. You must be at least {0} to continue!" .format(age, name))  
# Output: Hello 18. You must be at least Marcelo to continue!

# Using a formatted string
age = 18
first_name = "Marcelo"
greetings = "Hello {first_name}. You must be at least {age} to continue!"
greetings.format(first_name=first_name, age=age)  
# Output: Hello Marcelo. You must be at least 18 to continue!

# Specifying the string width and alignment
"{:<20}" .format("left aligned")  
# Output: 'left aligned      '      (20 characters wide, left aligned)
"{:>20}" .format("right aligned")  
# Output: '      right aligned'     (20 characters wide, right aligned)
"{:^20}" .format("centered")  
# Output: '       centered      '   (20 characters wide, centered)
"{example:>20}" .format(example="right aligned")  
# Output: '      right aligned'     (20 characters wide, right aligned)


# Using f-strings (Python 3.6+)
name = "Marcelo"
age = 41
f"Hello {name} You are {age} years old."
# Output: Hello Marcelo. You are 41 years old.

# Increasing the displayed value of the age variable
age = 41
f"{age + 2}"
# Output: 43

# Calling methods or functions
name = "Marcelo"
f"{name.lower()}"
# Output: marcelo

# Accessing dictionary values
sample_dict = {"name" : "Tom", "age" : 40}
f"Hello {sample_dict['name']}. You are {sample_dict['age']} years old."
# Output: Hello Tom. You are 40 years old.

# Backlash outside the expression -> Backslashes cant be used inside a f-string expression
name = "Marcelo"
print(f"My name is {name}\n")
# Output: My name is Marcelo

# Using the support for "=" -> shows the name and the value of the variable
username = "jdoe"
f"Your {username=}"
# Output: Your username="jdoe"

    
    # String Concatenation #
first_string = "My name is"
second_string = "Marcelo"
first_string + second_string
# Output: My name isMarcelo -> need to add space to the end of the first string

first_string = "My name is "
second_string = "Marcelo"
first_string + second_string
# Output: My name is Marcelo


# Using .join() method
first_string = "My name is"  # no ending space
second_string = "Marcelo"
" " .join([first_string, second_string])  # space added between quotes
# Output: My name is Marcelo

# Another example
first_string = "My name is"
second_string = "Marcelo"
"--" .join([first_string, second_string])
# Output: My name is--Marcelo


    # String Slicing #
"this is a string" [0:4]
# Output: this
"this is a string" [:4]
# Output: this
"this is a string" [-4:]  # Starts at the end of the string
# Output: ring


                                ### THE END ###