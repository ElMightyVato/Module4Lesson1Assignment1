"""
Objective: The aim of this assignment is to enhance your proficiency in using Python modules, both standard and custom, 
with a specific focus on importing with aliases.

Task 1: Custom Module with Aliases 

Problem Statement: Create a custom module named `text_utils.py` with functions for string manipulation 
(e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions. 
"""

import text_utils as tu # using tu as an aislise so it's not so long to type

def main():
    user_input = input("Enter a string to manipulate: ")

    reversed_string = tu.reverse_string(user_input)
    print(f"Reversed string: {reversed_string}")

    capitalized_string = tu.capitalize_string(user_input)
    print(f"Capitalized string: {capitalized_string}")

if __name__ == "__main__":
    main()