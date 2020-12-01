
"""
lists
"""



myUniqueList = []
myLeftovers = []


def addToList(animal):
    if animal in myUniqueList:
        addToLeftovers(animal)
        return False
    else:
        myUniqueList.append(animal)
        return True

def addToLeftovers(animal):
  myLeftovers.append(animal)




# Test the addToList function
print(myUniqueList) # []
print(addToList("dog")) # Returns True
print(myUniqueList) # ['dog']
print(myLeftovers) # []

# Adding the element that already exists
print(addToList("dog")) # Returns False
print(myUniqueList) # ['dog']
print(myLeftovers) # ['dog']

# Adding a new element
print(addToList("cat")) # Returns True
print(myUniqueList) # ['dog', 'cat']
print(myLeftovers) # ['dog']


# Adding the element that already exists
print(addToList("cat")) # Returns False
print(myUniqueList) # ['dog', 'cat']
print(myLeftovers) # ['dog', 'cat']

# Adding a new element
print(addToList("goat")) # Returns True
print(myUniqueList) # ['dog', 'cat', 'goat']
print(myLeftovers) # ['dog']

# Adding a new element
print(addToList("monkey")) # Returns True
print(myUniqueList) # ['dog', 'cat', 'goat', 'monkey']
print(myLeftovers) # ['dog']



"""

EZEBUIRO UCHECHUKWU VINCENT 

"""