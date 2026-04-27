import os
import random

class NumberSeparator:
    def __init__(self, input_file_name="numbers.txt", even_file_name="even.txt", odd_file_name="odd.txt"):
        self.input_file_name = input_file_name
        self.even_file_name = even_file_name
        self.odd_file_name = odd_file_name
    def generate_dummy_data(self):
        if not os.path.exists(self.input_file_name):
            print("Generating input file with random integers...")
            with open(self.input_file_name, "w") as target_file_object:
                for i in range(20):
                    random_integer = random.randint(1, 100)
                    target_file_object.write(f"{random_integer}\n")