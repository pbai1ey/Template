from typing import Union
from persistence import load_state, save_state

class BasicDemo:
    def __init__(self) -> None:
        self.state = load_state()
        self.run_count = self.state.get("run_count", 0) + 1
        print(f"This is run #{self.run_count}")

        try:
            self.num = int(input("Enter a number: "))
        except ValueError:
            print("Invalid input for number, using default.")
            self.num = 42

        self.noun = input("Enter a noun (e.g., 'world'): ") or "world"

    def show_string(self) -> None:
        print(f"Hello, {self.noun}! (Using num: {self.num})")

    def show_array(self) -> None:
        array = [i for i in range(1, self.num + 1)] if self.num <= 10 else [1, 2, 3, 4, 5]
        print(f"Here is an array based on {self.noun}: {array}")

    def show_matrix(self) -> None:
        matrix = [[self.num, self.num+1, self.num+2], [self.num+3, self.num+4, self.num+5], [self.num+6, self.num+7, self.num+8]]
        print(f"Here is a matrix incorporating {self.noun}: {matrix}")

    def show_dictionary(self) -> None:
        dict_example: dict[str, Union[str, int]] = {"key": "value", "num_key": self.num, "noun_key": self.noun}
        print(f"Here is a dictionary with {self.noun}: {dict_example}")

    def show_set(self) -> None:
        set_example = {self.num, self.num+1, self.num+2, hash(self.noun)}  # Using hash for demo; sets can hold mixed types if hashable
        print(f"Here is a set including {self.noun}: {set_example}")

    def show_tuple(self) -> None:
        tuple_example = (self.num, self.num+1, self.noun)
        print(f"Here is a tuple with {self.noun}: {tuple_example}")

    def show_comprehension(self) -> None:
        comprehension = [x * self.num for x in range(min(5, self.num))]
        print(f"Here is a list comprehension using {self.noun}: {comprehension}")

    def show_for_loop(self) -> None:
        for i in range(min(self.num, 5)):
            print(f"For loop iteration {i} with {self.noun} and num {self.num}.")

    def show_if_else(self) -> None:
        if self.num % 2 == 0:
            print(f"The number {self.num} is even, like a pair of {self.noun}s.")
        else:
            print(f"The number {self.num} is odd, unlike a single {self.noun}.")

    def show_while_loop(self) -> None:
        while_loop_counter = 0
        while while_loop_counter < min(self.num, 5):
            print(f"While loop iteration {while_loop_counter} with {self.noun} and num {self.num}.")
            while_loop_counter += 1

    def show_error_handling(self) -> None:
        try:
            result = self.num / (self.num if self.num != 0 else 1)
            print(f"Division result using {self.noun} and num: {result}.")
        except:
            print("Error avoided (e.g., division by zero).")

    def run(self) -> None:
        print("Starting basic demo...")
        self.show_string()
        self.show_array()
        self.show_matrix()
        self.show_dictionary()
        self.show_set()
        self.show_tuple()
        self.show_comprehension()
        self.show_for_loop()
        self.show_if_else()
        self.show_while_loop()
        self.show_error_handling()
        save_state({"run_count": self.run_count})

if __name__ == "__main__":
    demo = BasicDemo()
    demo.run()