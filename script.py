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