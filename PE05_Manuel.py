'''1) Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''

# Function definition
def make_shirt(size="Large", message="I love Python!"):
    print(f"The shirt size is {size} and the message on it is '{message}'.")
    
make_shirt("Medium")
make_shirt(message="Python is awesome!", size="Small")
make_shirt()


'''
2) Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''

#modified make_shirt() function is already provided above. Now we will call it with different arguments as per the requirement.
make_shirt()# Using default size and message
make_shirt("Medium")
make_shirt("Small", "Python is awesome!")


'''
3) Write a function called describe_city() that accepts the name of a city and its country.
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.'''

# Function definition
def describe_city(city, country="Iceland"):# Function with default parameter for country
    print(f"{city} is in {country}.")# Calling the function with different cities
describe_city("Reykjavik")# Using default country
describe_city("Akureyri")# Using default country
describe_city("Paris", "France")# Using a different country
describe_city("New York", "USA")# Using a different country

'''4) Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.'''

# Function definition
def show_messages(messages):
    for message in messages:
        print(message)
# List of messages
messages = ["Hello, World!", "Welcome to Python programming.", "Functions are great!"]
# Calling the function to show messages
show_messages(messages)

'''5) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
Sample String : 'The quick Brow Fox'
'''
# Function definition
def count_case_characters(input_string):# Count upper and lower case characters in the input strings
    upper_case_count = sum(1 for char in input_string if char.isupper())# Count upper case characters
    lower_case_count = sum(1 for char in input_string if char.islower())# Count lower case characters
    print(f"No. of Upper case characters : {upper_case_count}")
    print(f"No. of Lower case Characters : {lower_case_count}")
# Sample string
sample_string = 'The quick Brow Fox'
count_case_characters(sample_string)