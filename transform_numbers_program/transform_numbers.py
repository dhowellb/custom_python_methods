import os
import random

class NumberTransformer:

    def __init__(self, input_file_name="integers.txt", double_file_name="double.txt", triple_file_name="triple.txt"):
        self.input_file_name = input_file_name
        self.double_file_name = double_file_name
        self.triple_file_name = triple_file_name
    def generate_dummy_data(self):
        if not os.path.exists(self.input_file_name):
            print("Generating integers file...")
            with open(self.input_file_name, "w") as target_file_object:
                for i in range(20):
                    random_integer = random.randint(1, 20)
                    target_file_object.write(f"{random_integer}\n")