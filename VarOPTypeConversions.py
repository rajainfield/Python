'''Start'''


'''Python has a simple syntax similar to the English language. And Case - Sensitive language.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick

Python uses indentation to indicate a block of code.It relies on indentation, using whitespace, to define scope; such as the scope of loops,
functions and classes.Other programming languages often use curly-brackets for this purpose'''

#The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
#You have to use the same number of spaces in the same block of code, otherwise Python will give you an error

'''Semicolons are optional in Python. You can write multiple statements on one line by separating them with ';'
but this is rarely used because it makes it hard to read:

Ex: print("Hello"); print("How are you?"); print("Bye bye!")

Text in Python must be inside quotes. You can use either " double quotes or ' single quotes:
unlike text, we don't put numbers inside double quotes
Ex: print("This will work!")
    print('This will also work!')
    print(2 +3)'''

#You can combine text and numbers in one output by separating them with a comma: print("I am", 35, "years old.") o/p:I am 35 years old.

'''By default, the print() function ends with a new line.

If you want to print multiple words on the same line, you can use the end parameter:
Ex: print("Hello World!", end=" ")
    print("I will print on the same line.")    

'''

#Variable: Variables are containers for storing data values.Python has no command for declaring a variable.
#A variable is created the moment you first assign a value to it.
'''Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.'''

# Variable types
x = 10        # int
y = 3.5       # float
z = "26"      # str

#Python allows you to assign values to multiple variables in one line:

a, B, c = "Orange", "Banana", "Cherry"
print(a);print(B);print(c)
D = E = F = 'Raja'
print(D);print(E);print(F)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

# Operators
sum_val = x + y   # Arithmetic
check = x > y     # Comparison
logic = (x > 5) and (y < 10)  # Logical

#If you want to specify the data type of a variable, this can be done with casting.

# Type Conversion
implicit = x + y        # int + float → float (implicit)
explicit = x + int(z)   # str → int (explicit)

#You can get the data type of a variable with the type() function.

print("Sum:", sum_val, type(sum_val))
print("Check:", check)
print("Logic:", logic)
print("Implicit:", implicit, type(implicit))
print("Explicit:", explicit, type(explicit))

#We can create the space character in the output by "+" "," and "Python " and "is " and "awesome, without them the result would be "Python is awesome".
#Mixing integers with string at output, avoid "+" use ","

'''---End---'''
