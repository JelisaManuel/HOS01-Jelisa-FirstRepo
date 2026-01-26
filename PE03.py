#guest lists #0       #1      #2 
guests = ["Harry", "Ron", "Luna"]
print(guests)

#Ron cant make it
guests[1] = "Daniel"
print(guests)

guests.insert(0, "Draco")
print(guests)

middle_index = len(guests) // 2
guests.insert(middle_index, "Frank")
print(guests)

guests.append("Ginny")
print(guests)

print("Final Guest List:", guests)

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can’t invite you to dinner.")

print("Guests still invited:", guests, "\n")

#list slicing
animals = ["dog", "cat", "elephant", "lion", "tiger", "giraffe", "zebra"]

# Print each animal
for animal in animals:
    print(animal)

print("The first three items in the list are:")
for animal in animals[0:3]:
    print(animal)

print("Three items from the middle of the list are:")
for animal in animals[2:5]:
    print(animal)

print("The last three items in the list are:")
for animal in animals[-3:]:
    print(animal)

#list with duplicates
numbers = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
duplicates = []
for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)
print("\n",duplicates)

'''
#this code allows user to input numbers and the finds duplicates in the list
user_input = input("Enter numbers (comma or space separated): ")
# Replace commas with spaces
clean_input = user_input.replace(",", " ")
# Convert to list of integers
numbers = list(map(int, clean_input.split()))
# Find duplicates
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
print("Duplicate numbers are:", duplicates)
'''

#tuple example representing a buffet menu
# Step 1: Original menu as a tuple
buffet_menu = ("pizza", "salad", "soup", "pasta", "bread")

# Step 2: Print original menu
print("\nOriginal buffet menu:")
for food in buffet_menu:
    print(food)

# Step 3: Attempt to modify an item (this would cause an error if uncommented)
# buffet_menu[0] = "burger"  # TypeError: 'tuple' object does not support item assignment

# Step 4: Create a new tuple with a revised menu
buffet_menu = ("pizza", "salad", "tacos", "sushi", "bread")

# Step 5: Print revised menu
print("\nRevised buffet menu:")
for food in buffet_menu:
    print(food)


#sorting a list of tuples based on the second element
data = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
sorted_data = sorted(data, key=lambda x: x[1])
print("\nSorted data by second element:", sorted_data)
