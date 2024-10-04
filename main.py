# Function to calculate the sum of numbers in a list
def sum_of_numbers(numbers):
    total = 0  # Initialize total to 0
    for number in numbers:
        total += number  # Add each number to the total
    return total

# Sample list of numbers
numbers_list = [5, 10, 15, 20, 25]

# Calling the function and printing the result
result = sum_of_numbers(numbers_list)
print("The sum of the numbers is:", result)
