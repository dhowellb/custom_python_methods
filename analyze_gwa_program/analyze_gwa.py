import os

class GradeAnalyzer:

    def __init__(self, input_file_name="students.txt"):
        self.input_file_name = input_file_name
    def generate_dummy_data(self):
        if not os.path.exists(self.input_file_name):
            sample_student_records = [
                "Student_A, 1.25", "Student_B, 1.15", "Student_C, 1.75", "Student_D, 2.00",
                "Student_E, 2.25", "Student_F, 1.10", "Student_G, 1.90", "Student_H, 1.60",
                "Student_I, 1.45", "Student_J, 2.10", "Student_K, 1.30", "Student_L, 1.85",
                "Student_M, 1.40", "Student_N, 1.20", "Student_O, 2.05", "Student_P, 1.70",
                "Student_Q, 1.50", "Student_R, 2.50", "Student_S, 2.75", "Student_T, 1.55"
            ]
            print("Generating student records...")
            with open(self.input_file_name, "w") as target_file_object:
                for student_record in sample_student_records:
                    target_file_object.write(f"{student_record}\n")