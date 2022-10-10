# Your code below:

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
# Replace Adam with Calla.
garden_waitlist[-1]
garden_waitlist[+1] = "Calla"
print(garden_waitlist)

#Replace Alisha with Alex.

garden_waitlist[-3]
garden_waitlist[+3] = "Alex"
print(garden_waitlist)

# Your code below:

order_list = ["Celery", "Orange Juice","Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)

#Remove duplicates.

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)

#Remove a missing item from a list?

new_store_order_list.remove["Onions"]

#Your code below:

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83],["Ellie", 101.5]]
print(class_name_test)
sams_score = (class_name_test[2][1])
print(sams_score)
ellies_score = (class_name_test[-1][-1])
print(ellies_score)

#Your code below:

incoming_class = [["Kenny", "American", 9],["Tanya","Russian", 9],["Madison","Indian", 7]]

#Madison went up a grade.

incoming_class[2][2] = 8
print(incoming_class)

#Change Kenny's nickname.

incoming_class[-3][-3] = "Ken"
print(incoming_class)

# Your code below:

first_names = ["Ainsley","Ben","Chani","Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

#2D

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
customer_data[2][2] = False
customer_data[1].remove(False)

#Add 2 lists.

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
