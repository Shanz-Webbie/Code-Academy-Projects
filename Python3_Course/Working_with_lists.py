inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

# How many items in the warehouse?

inventory_len = len(inventory)

first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]

#Count how many twin beds there are.

twin_beds = inventory.count("twin bed")

#Remove the 5th item in inventory.

removed_item = inventory.pop(4)

#Add new item to inventory.

inventory.insert(10, "19th Century Bed Frame")

#Sort the inventory.

inventory.sort()
print(inventory)