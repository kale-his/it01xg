#!/usr/bin/env python3
## Genererades av github copilot 2026-08-13
"""
Program to calculate the mean of a list of numbers.
"""

def calculate_mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.
    
    Args:
        numbers: A list of numeric values
        
    Returns:
        The mean of the numbers, or None if the list is empty
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def main():
    """Main function to handle user input and display the mean."""
    print("Mean Calculator")
    print("-" * 40)
    
    try:
        # Get input from user
        user_input = input("Enter numbers separated by spaces: ")
        
        # Convert input to list of numbers
        numbers = [float(x) for x in user_input.split()]
        
        if not numbers:
            print("Error: No numbers provided.")
            return
        
        # Calculate and display the mean
        mean = calculate_mean(numbers)
        print(f"\nNumbers: {numbers}")
        print(f"Mean: {mean}")
        
    except ValueError:
        print("Error: Please enter valid numbers separated by spaces.")


if __name__ == "__main__":
    main()
