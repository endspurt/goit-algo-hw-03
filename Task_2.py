import random

def get_numbers_ticket(min, max, quantity):
    # Validate input parameters
    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1):
        print("Invalid input parameters.")
        return []

    # Generate a list of unique random numbers using random.sample
    numbers = random.sample(range(min, max + 1), quantity)

    # Return the sorted list of numbers
    return sorted(numbers)

# Example usage of the function
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery ticket numbers:", lottery_numbers)

