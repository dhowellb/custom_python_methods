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
    def process_and_transform(self):
        try:
            pass
        except FileNotFoundError:
            print(f"Error: {self.input_file_name} not found.")
            with open(self.input_file_name, "r") as input_file_object, \
                 open(self.double_file_name, "w") as double_file_object, \
                 open(self.triple_file_name, "w") as triple_file_object:
                for current_line in input_file_object:
                    current_number = int(current_line.strip())
                    if current_number % 2 == 0:
                        squared_value = current_number ** 2
                        double_file_object.write(f"{squared_value}\n")
                    else:
                        cubed_value = current_number ** 3
                        triple_file_object.write(f"{cubed_value}\n")
            print("Transformation complete.")
if __name__ == "__main__":
    transformer_instance = NumberTransformer()
    transformer_instance.generate_dummy_data()
    transformer_instance.process_and_transform()