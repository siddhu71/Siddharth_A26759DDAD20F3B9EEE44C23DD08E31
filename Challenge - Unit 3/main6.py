class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name}, Roll Number: {self.roll_number}, CGPA: {self.cgpa}"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with a list of student objects
students = [
    Student("Alice", "101", 3.75),
    Student("Bob", "102", 3.9),
    Student("Charlie", "103", 3.6),
    Student("David", "104", 3.8),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(student)
