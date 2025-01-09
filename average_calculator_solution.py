def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers) 

#Test cases
print(calculate_average([10,20,30]))
print(calculate_average([]))