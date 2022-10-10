last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

#Creating gradebook with subjects and grades in 2D list.

gradebook = [["physics", 98], ["calculus", 97],["poetry", 85],["history", 88]]
print(gradebook)

#More subjects and new grade.

subjects.append("computer science")
grades.append("100")
gradebook.append(["visual arts", 93])

#Modify gradebook.

gradebook[-1][1] = 95
print(gradebook)

# Pass/Fail Poetry Class

gradebook[2].remove(85)
gradebook[2].append("Pass")

# One Big Gradebook. Merge into one master list

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)