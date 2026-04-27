import os
import random

class NumberTransformer:

    def __init__(self, input_file_name="integers.txt", double_file_name="double.txt", triple_file_name="triple.txt"):
        self.input_file_name = input_file_name
        self.double_file_name = double_file_name
        self.triple_file_name = triple_file_name