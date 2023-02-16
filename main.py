''''
My name is Ramon Diaz, this was second project in codio platform. In this project....

IT 140- Project 2: Grocery List

The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop througth the grocery list
Section 3 - provide output to the console
'''

#Task: Create the empty data structure
grocery_item = {} #defines empty dictionary

grocery_history = [] # defines empty list

#Variable used to check if the while loop condition is met
stop = 'go'

while stop != 'q':# Creation of while loop as stop does not equal q

    #Accept input of the name of the grocery item purchased.
    item_name = input('Item Name')# accept item name

    #Accept input of the quantity of the grocery item purchased.
    quantity = input('Quantity purchased: ') #accept purchased quantity

    #Accept input of the cost of the grocery item input (this is a per-item cost)
    cost = input('Price per item') # accept item price

    #Using the update function to create a dictionary entry which contains the name, number price entered by the item
    #number and price entered by the user
    grocery_item['name'] = item_name
    grocery_item ['number'] = int(quantity)
    grocery_item['price'] = float(cost)
    #Add the grocery_item to the grocery_history list using append function
    grocery_history.append(grocery_item.copy())
    #Accept input from the user asking if they have finished entering grocery items.
    stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit :")

#Define variable to hold grand total called 'grand_total'
grand_total = 0
#Define  a 'for' loop.

for index, item in enumerate(grocery_history):

    #Calculate the total cost for the grocery_item.
    item_total = item['number'] * item['price']

    #Add the item_total to the grand_total
    grand_total += item_total

    #Output the information for the grocery item to match this example
    #2 apple @ $1.49 ea $2.98
    print('%d %s @ $%.2f ea $%.2f' % (item['number'], item['name'], item['price'], item_total))

    #Set the item_total equal to 0
    item_total = 0

#Print the grand total
print('Grand total: $%.2f' % grand_total)

