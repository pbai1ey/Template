#!/usr/bin/env python3
"""
Entry point for the Python template project.
"""
from persistence import load_state, save_state


def main() -> None:
    """Main application entry point."""
    print("Hello from your new Python project!")
    # Add your code here

    # Load previous state
    state = load_state()
    run_count = state.get("run_count", 0) + 1
    print(f"This is run #{run_count}")

    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input, using default.")
        num = 42
    thing = "world"
    print(f"Hello, {thing}!")
    array = [1, 2, 3, 4, 5]
    print(f"Here is an array: {array}")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Here is a matrix: {matrix}")
    dict_example = {"key1": "value1", "key2": "value2"}
    print(f"Here is a dictionary: {dict_example}")
    list_comprehension = [x * 2 for x in range(5)]
    print(f"Here is a list comprehension: {list_comprehension}")
    for i in range(num):
        print(f"Loop iteration {i}")
    if_condition = "even" if num % 2 == 0 else "odd"
    print(f"The number {num} is {if_condition}.")
    while_loop_counter = 0
    while while_loop_counter < num:
        print(f"While loop iteration {while_loop_counter}")
        while_loop_counter += 1
    try:
        result = 10 / 2
        print(f"Division result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Execution of try-except block is complete.")

    # Save state before exit
    save_state({"run_count": run_count, "last_num": num, "last_result": if_condition})


if __name__ == "__main__":
    main()
