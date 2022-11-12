first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  last_three_letters = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return last_three_letters

temp_password = password_generator(first_name, last_name)