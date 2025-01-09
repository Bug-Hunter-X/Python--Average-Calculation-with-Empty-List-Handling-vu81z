# Python Average Calculator

This repository contains a Python function designed to calculate the average of a list of numbers.  It includes robust error handling to gracefully manage cases where the input list is empty.

## Function: `calculate_average(numbers)`

The `calculate_average` function takes a list of numbers as input and returns their average.  If the input list is empty, it returns 0 to prevent a `ZeroDivisionError`.

## How to Use

1.  Clone this repository.
2.  Import the `calculate_average` function into your project.
3.  Pass a list of numbers to the function to obtain the average.

## Example Usage

```python
from average_calculator import calculate_average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")  # Output: The average is: 30.0

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average is: {average}")  # Output: The average is: 0
```