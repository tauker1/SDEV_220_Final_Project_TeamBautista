# added all the comments and lines 60-74
import tkinter
from tkinter import *

root = Tk()
root.title('Burger Smash')
root.geometry('500x500')

# Creating the lists
toppings = ['Lettuce', 'Tomato', 'Onion', 'Bacon', 'Pickles']
sides = ['Fries', 'Chips', 'Mozzarella Sticks', 'Fried Pickles']
drinks = ['Soda', 'Coffee', 'Water', 'Beer']
EXIT = 'ZZZ'

# Creating the dictionary
menu_dict = {'Toppings': [], 'Sides': [], 'Drinks': []}


# Creating all three classes
class Toppings:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - Cost: ${self.price:.2f}'


class Sides:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} ${self.price:.2f}'


class Drinks:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - Cost: ${self.price:.2f}'


# Creating instances for various burger toppings, sides, and drinks
lettuce = Toppings('Lettuce', 0.50)
tomato = Toppings('Tomato', 0.50)
onion = Toppings('Onion', 0.50)
bacon = Toppings('Bacon', 2.00)
pickles = Toppings('Pickles', 0.75)

fries = Sides('Fries', 2.99)
chips = Sides('Chips', 2.50)
mozzarella_sticks = Sides('Mozzarella Sticks', 3.99)
fried_pickles = Sides('Fried Pickles', 3.50)

soda = Drinks('Soda', 1.99)
coffee = Drinks('Coffee', 1.25)
water = Drinks('Water', 0.50)
beer = Drinks('Beer', 8.99)

# Adding the toppings, sides, and drinks to the dictionary
menu_dict['Toppings'].extend([lettuce, tomato, onion, bacon, pickles])
menu_dict['Sides'].extend([fries, chips, mozzarella_sticks, fried_pickles])
menu_dict['Drinks'].extend([soda, coffee, water, beer])


# Creating the function to show the user the menus
def display_menu(menu_dict):
    for category, items in menu_dict.items():
        print(f'{category} Menu:')
        for item in items:
            print(f' {item}')
        print()


display_menu(menu_dict)


def add_to_burger(toppings):
    total = 0
    for topping in toppings:
        user_input = input('Please enter the toppings you would like to add: ')

        if user_input == 'ZZZ':
            break

        if topping == 'Lettuce':
            total += 0.40
        elif topping == 'Tomato':
            total += 0.50
        else:
            print(user_input)


add_to_burger(toppings)


root.mainloop()