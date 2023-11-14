import tkinter as tk
from tkinter import *

# create a list to store items in a cart
cart_items = []


# function to create thank you window
def open_thank_window():
    # create a new window
    thank_window = tk.Toplevel(root)

    # set the size
    thank_window.geometry('500x250')

    # add a label
    thank_label = tk.Label(thank_window, text='Thank you for ordering from Bautista Pizza Palace!')
    thank_label.config(font=('Courier', 10))
    thank_label.pack()


# function to create specialty window
def open_specialty_window():
    # create a new window
    specialty_window = tk.Toplevel(root)

    # set the size
    specialty_window.geometry('500x500')

    # add a label
    specialty_label = tk.Label(specialty_window, text='Welcome to our Specialty Menu!')
    specialty_label.config(font=('Courier', 20))
    specialty_label.pack()

    # add price label
    specialty_label_label = tk.Label(specialty_window, text='Specialty Pizza any size: $17.99')
    specialty_label_label.config(font=('Courier', 16))
    specialty_label_label.pack()

    # add a button
    specialty_button = tk.Button(specialty_window, text='Click here to order a specialty pizza.', height=2, width=40, command=add_specialty_pizza)
    specialty_button.config(font=('Courier', 8))
    specialty_button.pack()

    # click this button to exit the program
    specialty_exit_button = tk.Button(specialty_window, text='Exit', command=specialty_window.destroy, height=2, width=40)
    specialty_exit_button.config(font=('Courier', 8))
    specialty_exit_button.pack()


# adding small pizza to cart
def add_small_pizza():
    cart_items.append('Small Pizza')
    cart_label.config(text='Cart: ' + ', '.join(cart_items))


# adding small pizza to cart
def add_medium_pizza():
    cart_items.append('Medium Pizza')
    cart_label.config(text='Cart: ' + ', '.join(cart_items))


# adding small pizza to cart
def add_large_pizza():
    cart_items.append('Large Pizza')
    cart_label.config(text='Cart: ' + ', '.join(cart_items))


# adding small pizza to cart
def add_hotdog():
    cart_items.append('Hotdog')
    cart_label.config(text='Cart: ' + ', '.join(cart_items))


# adding small pizza to cart
def add_specialty_pizza():
    cart_items.append('Specialty Pizza')
    cart_label.config(text='Cart: ' + ', '.join(cart_items))


# adding total cost of cart together
def calculate_total():
    total = 0
    for item in cart_items:
        if item == 'Small Pizza':
            total += 8.99
        elif item == 'Medium Pizza':
            total += 9.99
        elif item == 'Large Pizza':
            total += 10.99
        elif item == 'Hotdog':
            total += 1.99
        elif item == 'Specialty Pizza':
            total += 17.99
    total_label.config(text='Total: $' + str(round(total, 2)))
    open_thank_window()


# create a GUI window
root = tk.Tk()

# create a label for the cart
cart_label = Label(root, text='Cart:')
cart_label.config(font=('Courier', 16))
cart_label.pack()

# title of the GUI
root.title('Bautista Pizza Palace')

# set the size
root.geometry('500x600')

# click this button to open the special menu
button2 = tk.Button(root, text='Click this button to open the Specialty Menu', command=open_specialty_window)
button2.config(font=('Courier', 13))
button2.pack()

# order question
title = tk.Label(root, text='What would you like to order?')
title.config(font=('Courier', 20))
title.pack()

# add price label
small_label = tk.Label(root, text='Small Pizza: $8.99')
small_label.config(font=('Courier', 16))
small_label.pack()

# add price label
medium_label = tk.Label(root, text='Medium Pizza: $9.99')
medium_label.config(font=('Courier', 16))
medium_label.pack()

# add price label
large_label = tk.Label(root, text='Large Pizza: $10.99')
large_label.config(font=('Courier', 16))
large_label.pack()

# add price label
hotdog_label = tk.Label(root, text='Hot Dog: $1.99')
hotdog_label.config(font=('Courier', 16))
hotdog_label.pack()

# add total price label
cart_label = tk.Label(root, text='Cart: ')
cart_label.pack()

total_label = tk.Label(root, text='Total: ')
total_label.pack()

# click this button to order small pizza
small_button = tk.Button(root, text='Click here to order a small pizza.', height=2, width=35, command=add_small_pizza)
small_button.config(font=('Courier', 8))
small_button.pack()

# click this button to order medium pizza
medium_button = tk.Button(root, text='Click here to order a medium pizza.', height=2, width=35, command=add_medium_pizza)
medium_button.config(font=('Courier', 8))
medium_button.pack()

# click this button to order large pizza
large_button = tk.Button(root, text='Click here to order a large pizza.', height=2, width=35, command=add_large_pizza)
large_button.config(font=('Courier', 8))
large_button.pack()

# click this button to order hotdog
hotdog_button = tk.Button(root, text='Click here to order a hotdog.', height=2, width=35, command=add_hotdog)
hotdog_button.config(font=('Courier', 8))
hotdog_button.pack()

# click this button to submit order
submit_button = tk.Button(root, text='Submit your order.', height=2, width=35, command=calculate_total)
submit_button.config(font=('Courier', 8))
submit_button.pack()

# click this button to add your total cost
total_button = tk.Button(root, text='Calculate Total', height=2, width=35, command=calculate_total)
total_button.config(font=('Courier', 8))
total_button.pack()

# click this button to exit the program
exit_button = tk.Button(root, text='Exit', command=root.destroy, height=2, width=35)
exit_button.config(font=('Courier', 8))
exit_button.pack()

# start the GUI
root.mainloop()
