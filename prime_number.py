#number 1
# Check if a number is prime
import math 
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


#number 2
# Generate Fibonacci sequence up to n-th position

Fibonacci_sequence = [0, 1]
n = int(input("What position in the Fibonacci sequence do you want to see? "))
if n < 0:
    print("Please enter a non-negative integer.")
elif n == 0:
    print("Fibonacci sequence at position 0 is 0")
elif n == 1:
    print("Fibonacci sequence at position 1 is 1")
else:
    for i in range(2, n + 1):
        next_value = Fibonacci_sequence[i - 1] + Fibonacci_sequence[i - 2]
        Fibonacci_sequence.append(next_value)
    print(f"Fibonacci sequence at position {n} is {Fibonacci_sequence[n]}")


#number 3
# Determine life stage based on age

    age = int(input("Enter the age of the person: "))
    if age <= 2:
        print("That person is a baby")
    elif 2 < age <= 3:
        print("That person is a toddler")
    elif 4 <= age <= 12:
        print("That person is a kid")
    elif 13 <= age <= 19:
        print("That person is a teenager")
    elif 20 <= age <= 64:
        print("That person is an adult")
    elif age >= 65:
        print("That person is an elder")
    else:
        print("That person is an unknown age")



#number 4
# Determine ticket price based on age

    age = int(input("Enter the age of the person: "))
    if age < 0:
        print("Invalid age")
    elif 1 <= age <= 2:
        print("The ticket price is $0")
    elif 3 <= age <= 12:
        print("The ticket price is $10")
    elif age >=13:
        print("The ticket price is $15")
    else:
        print("The ticket price is unknown")

#number 5
# Print a triangle pattern

rows = 5
for i in range(1, rows + 1):
        print(" "*(rows - i) + "* "*i)
