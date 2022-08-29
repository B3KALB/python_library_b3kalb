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