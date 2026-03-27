def student_info(**kwargs):
    print("Student Details:")
    for key, value in kwargs.items():
        print(f"{key} -> {value}")

student_info(name="John", age=20, marks=85, grade="A")