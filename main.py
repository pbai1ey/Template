#!/usr/bin/env python3
"""
Entry point for the Python template project.
"""


def main() -> None:
    """Main application entry point."""
    print("Hello from your new Python project!")
    # Add your code here
    num = 42
    print(f"The answer to life, the universe, and everything is {num}.")
    array = [1, 2, 3, 4, 5]
    print(f"Here is an array: {array}")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Here is a matrix: {matrix}")
    dict_example = {"key1": "value1", "key2": "value2"}
    print(f"Here is a dictionary: {dict_example}")
    list_comprehension = [x * 2 for x in range(5)]
    print(f"Here is a list comprehension: {list_comprehension}")
    for i in range(3):
        print(f"Loop iteration {i}")
    if_condition = "even" if num % 2 == 0 else "odd"
    print(f"The number {num} is {if_condition}.")
    while_loop_counter = 0
    while while_loop_counter < 3:
        print(f"While loop iteration {while_loop_counter}")
        while_loop_counter += 1


if __name__ == "__main__":
    main()
