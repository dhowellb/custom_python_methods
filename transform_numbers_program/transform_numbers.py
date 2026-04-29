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
        # Dito dapat nakapasok sa loob ng TRY ang pag-open at pag-process
        try:
            with open(self.input_file_name, "r") as input_file_object, \
                 open(self.double_file_name, "w") as double_file_object, \
                 open(self.triple_file_name, "w") as triple_file_object:
                
                for current_line in input_file_object:
                    cleaned_line = current_line.strip()
                    
                    # Fix para ma-skip ang blank lines at iwas ValueError
                    if not cleaned_line:
                        continue
                        
                    current_number = int(cleaned_line)
                    
                    # Logic mo: kapag even, naka-square. Kapag odd, naka-cube.
                    if current_number % 2 == 0:
                        squared_value = current_number ** 2
                        double_file_object.write(f"{squared_value}\n")
                    else:
                        cubed_value = current_number ** 3
                        triple_file_object.write(f"{cubed_value}\n")
                        
            print("Transformation complete.")
            
        # Ito lang ang trabaho ng except: mag-print ng error kapag wala yung file
        except FileNotFoundError:
            print(f"Error: {self.input_file_name} not found.")

if __name__ == "__main__":
    print("Start na ang number transformer program...")
    transformer_instance = NumberTransformer()
    # Naka-comment out para hindi ma-overwrite ang sarili mong integers.txt
    # transformer_instance.generate_dummy_data()
    transformer_instance.process_and_transform()