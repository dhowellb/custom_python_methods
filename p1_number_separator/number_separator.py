import os
import random

class NumberSeparator:
    def __init__(self, input_file_name="numbers.txt", even_file_name="even.txt", odd_file_name="odd.txt"):
        self.input_file_name = input_file_name
        self.even_file_name = even_file_name
        self.odd_file_name = odd_file_name