class LifeLogger:

    def __init__(self, output_file_name="mylife.txt"):
        self.output_file_name = output_file_name
    def write_entries(self):
        with open(self.output_file_name, "w") as output_file_object:
            pass
            while True:
                user_input_line = input("Enter line: ")
                output_file_object.write(user_input_line + "\n")
                user_choice = input("Are there more lines y/n? ")
                if user_choice.strip().lower() != 'y':
                    break
        print("Entries successfully saved.")
if __name__ == "__main__":
    logger_instance = LifeLogger()
    logger_instance.write_entries()