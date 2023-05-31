#python data structures
# The 4 built-in data structures in python are lists, tuples, sets, and dictionaries

# lists

nums = [1,2,-10,6,58,123,55,-70]

print(len(nums)) #to get how many element in a list

nums.append(9) #to add element at the end of the list

nums.insert(5,6) #adding number 6 in index number 5

nums.pop(4) #removing the element in the index number 4

nums.remove(-70) #removing the element -70 specificly

###############################################################

# Tuples
 

fruits = ("Orange","Apples","Banana","Kiwi")

print(len(fruits)) # to get how many elements in a tuple


#tuples are unchangeable unless it turned into a list

listOfFruits = list(fruits) #casting the tuple to a list

listOfFruits.append("cherry")

fruitsTuple = tuple(listOfFruits) #casting the list to a tuple

################################################################

# Sets

grades = {20,25.5,36,10,True,"Orange"}

#sets are unordered. So, they have no index.
#duplicates are not allowed.
#sets are unchangeable unless it turned into a list.

gradeList = list(grades)
gradeList.append(-17)

listOfGrades = set(gradeList)

print(listOfGrades)

################################################################

#dictionaries

phoneDirectory = {"Ali":24177777777,"Ahmed":258999999,"Mohamed":691111111}
print(phoneDirectory["Ali"])

#OR

studentData=dict(name = "Ali", ID = 258999999, phone = 691111111 )
print(studentData)

#dictionaries are ordered and changeable.
#duplicates are not allowed.

print(len(phoneDirectory))



