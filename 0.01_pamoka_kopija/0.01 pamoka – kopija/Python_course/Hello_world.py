#--------------------Variables ✘--------------------
# first_name = 'Bro' #assigning a vriable
# last_name = 'Code'
#full_name = first_name +""+ last_name
#print("Hello" +full_name)  #don't put '', "" in print!
#print("Hello"+name)

# age = 21
# age += 1
# # print(age)
# print("Your age is: "+str(age))

# height = 250.5
# print("Your height is " +str(height)+ " cm")
# print(type(height))

# human = True
# print("Are you a human: "+str(human))
# print(type(human))

# "Strings which stores series of charecters"
# int=which store whole integers
# float=which store floating point numbers a numeric value whith a decimal
# bool=which store True or False
#--------------------Multiple assignment 🔠--------------------
# name = 'Bro'
# age = 21
# attractive = True
# name, age, attractive ='Bro', 21, True

# print(name)
# print(age)
# print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)
#--------------------String methods 〰️--------------------
# name = 'Bro Code'

# print(len(name))   #len=Calculates the lenght of a string
# print(name.find('o')) #find=finds the character or number in () (starting from zero)
# print(name.capitalize()) Capitalizes letters
# print(name.upper()) Prints in upper case letters
# print(name.lower()) Prints in lower case letters\
# print(name.isdigit()) Checks if there is any digits in the string
# print(name.isalpha()) Checks if string contains only alphabetical letters
# print(name.count('o')) Counts how many selected letters are in your string
# print(name.replace('o','a')) Replaces the selected letters to other letters you typed in your string\
# print(name*3) By adding * prints the string by what number you've selcted 
#--------------------Type cast 💱--------------------
# x = 1 #int
# y = 2.0 #float
# z = '3' #string

# x = str(x)
# y = str(y)
# z = str(z)

# print("X is "+str(x))
# print("Y is "+str(y))
# print(z*3)
#--------------------User input ⌨️--------------------
name = input("What is your name?:")
age = int(input("How old are you?: "))
height = float(input("How tall are you?:"))

print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")