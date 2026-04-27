class LifeLogger:

    def __init__(self, output_file_name="mylife.txt"):
        self.output_file_name = output_file_name
    def write_entries(self):
        with open(self.output_file_name, "w") as output_file_object:
            pass
            while True:
                user_input_line = input("Enter line: ")
                output_file_object.write(user_input_line + "\n")