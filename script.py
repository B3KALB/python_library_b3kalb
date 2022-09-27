import math

# ceil for roundining up
math.ceil(9.94)

# class
class Bank_Account:
    def __init__(self,name, number, withdraw):
        self.name = name
        self.number = number
        self.withdraw = withdraw
        self.ballance = 1000

# class and definition 
class Car:
    manufacture = "Ferrari"
    model = 2019
    color = "red"

    def print_specs(self):
        print(self.manufacture)
        print(self.model)
        print(self.color)

    def change_color(self, new_color):
        self.color = new_color
        print("Color is now", self.color)

car = Car()
print(car.color)
car.change_color("yellow")
        
# hello list scramble
scrambled = ["X", "y", "3", "o", "e", "l", "5", "l", "a", "e", "f", "H", "z"]

hello = scrambled[-2:2:-2]
print(hello)

# words list [do you] [wanna dance?]
words = [ "Do", "you", "I", "we", "like", "wanna", "dance?"]

print(words[1::-1])
print(words[-2::])

# grab the 1's from the list and store it in a variable 
beats = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

downbeats = beats[::3]
print(downbeats)

# grab the "B" from the list and stor it in a variable
alphabet = [ "A", "B", "C"]
selection = alphabet[-2:-1:1]
print(selection)

# Podium placer 
bibs = [ 33, 35, 42, 16, 23, 57, 10, 22, 54, 4]
required = 3

podium = bibs[:required]
print(podium)

# jason quit
users = {"Dave": (27, "Manager"),
"Alexis": (33, "CEO"),
"Jason": (22, "Apprentice")}

del users["Jason"]
print(users)


# delete cookies
cookies = ["site_access", "adverts"]
permissions = (True, False, False)

if permissions [-1] == False:
    del cookies
    print("Cookies deleted")

# shopping list with update
shopping = ["bananas", "oranges", "lemons", "carrots", "beans"]

if len(shopping) > 3:
    del shopping [-1]

print(shopping)


# add dollars
latest = "dollars"
collection = ["pounds", "eruos", latest]
collection[-1] = latest
del latest
print(collection)


# side salad
side = "salad"
meal = ["Steak", "Chips", side]
del meal[-1]
print(side)

# scores
scores = [30, 50, 70, 60, 60]

if scores[-1] == scores[-2]:
    print("Entry same as previous item - is it a duplicate?")


# answers
answers = {"yes", "sometimes", "yes", "no", "sometimes"}

unique = set(answers)
print(unique)

# iris
iris_species = ["setosa", "setosa", "siberian"]

print(set(iris_species))

# program - update today to day of week
def show_programme(day):
    for event in day:
        print(f"Today: {event}")

monday = ["Swan Lake", "Ravel - Piano Concerto"]
tuesday = ["La Boheme"]

show_programme(monday)
show_programme(tuesday)

# help customers
def help_customers(customers):
    counter = 1
    while counter < customers :
        print(f"Customer no{counter} go to the next free desk")
        counter +=1
help_customers(3)

#show instructions 
def show_instructions(ingredients):
    for item in ingredients :
      print(f"Stir in: {item}")
    
cake = ["flour", "softened butter", "milk", "sugar", "eggs"]
show_instructions(cake)
print("Throw it in the pan!")

# LOST MY JOB OVER THIS ONE
# 
# find the two that add up tp target
nums = [2,7,11,15,9,3] 
target = 14

for i in range(len(nums)):
    for b in range(len(nums)):
        if nums[i]+nums[b] == target:
            print("nums "+ str(i) + " nums " + str(b))
# MY VAR
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
target_value = int(input("Enter a target value 1-20: "))

def which_add_up(nums, target):
    print(f"The numbers are {nums}")
    for i in range(len(nums)):
        for b in range(len(nums)):
            if nums[i]+nums[b] == target:
                print("index "+ str(i) + " and index " + str(b) + f" equal {target}.")
                print(f"{nums[i]} + {nums[b]} = {target}")
which_add_up(nums, target_value)

        
# example 1
def python_is_great(var):
    incoming = str(var)
    print(f"Working: {incoming}")
    
    python_is_great()
    python_is_great(var)
    python_is_great("var")  
# example 2
im_a_variable = "I'm a value"

single_result = (math.ceil(9.94))
im_an_expression = single_result

python_is_great("I'm a value")
python_is_great(im_a_variable)
python_is_great(im_an_expression)
# example 3
def local_var_fun(var):
    here_we_go_again = str(var)
    print(f"Variable: {here_we_go_again}")

print(here_we_go_again)
# example 4
def fun_with_arg(unique_name):
    get_the_param = f"{unique_name}You cant get me!"
    print(get_the_param)

print(get_the_param)
# example 5
outside_var = 2 + 2

def new_funk():
    outside_var = 6 + 6
    print(outside_var)

new_funk()

print(outside_var)

# unit 2 question from Kenedy,
def new_line():

    print('.')

def this_is_it(funCall):
    
    funCall = print("Calls the function")
    
this_is_it(new_line())

# unit 3 cs 1101 Countup
def countup(n):
     if n >= 0:
          print('Blastoff!')
     else:
          print(n)
          countup(n+1)
          
countup(-3)

# # unit3 cs1101 LJ
#  ex1
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)
          
def countup(n):
     if n >= 0:
          print('Blastoff!')
     else:
          print(n)
          countup(n+1)
          
whole_num = input("Please enter an integer: ")

n = int(whole_num)

if n > 0:
    countdown(n)
elif n < 0:
    countup(n)
else:
     print('Blastoff!')

# ex2
# working
not_here = [1, 2, 3]

def run_time_error(it):
    
        print(f"Not today {it}!")

oops = not_here[2]

run_time_error(oops)

# <br>
print("--------")

# not working
not_here = [1, 2, 3]

def run_time_error(it):
    
        print(f"Not today {it}!")

oops = not_here[3]

run_time_error(oops)

# UNIT4-
import math

# EXAMPLE 1 hypotenuse

leg_x = float(input("leg X = "))# this sets our input x as a variable

leg_y = float(input("leg Y = "))#this sets our input y as a variable

def hypotenuse(x, y):# this creates our function and passes in the two arguments 
    z = math.sqrt(x**2 + y**2)# this does the heavy lifting by finding the sqr root of our two variables to the second power and added together
    print(f"The hypotenuse of leg Z = {round(z, 2)}")# this prints the value of variable z and i have rounded that to the nearest hundredth

hypotenuse(leg_x, leg_y)# this calls our function and passes in the two live variables as arguments