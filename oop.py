# 🛠 Hands-On Assignment: Object-Oriented Python Practice
# Objective:
# Practice creating Python classes, using object-oriented 
# programming (OOP) concepts, and working with common 
# Python data types like lists, tuples, sets, and dictionaries.

# Instructions:
# Create a Python script.
# Implement all tasks using classes, objects, and methods.
# Include comments to explain your code.
# Submit the Github Repository with your completed work.

# Part 1: Class Definition

# Define a class called Student with the following attributes:
# name (string), email (string), grades (list of integers).
class Student:
    """Student class representing a student with name, email, and grades."""
    
    def __init__(self, name, email, grades):
        """ Initialize the Student class with attributes: name, email, and grades """
        self.name = name
        self.email = email      
        self.grades = grades  # List of grades
        
    # add_grade(self, grade): Adds a single grade to the student's grades list.
    def add_grade(self, grade):
        """ Adds a single grade to the student's grades list. """
        self.grades.append(grade)
    
    # average_grade(self): Returns the average of the grades.
    def average_grade(self):
        """ Returns the average of the grades. """
        if not self.grades:
            return 0
        # Calculate and return the average grade
        return sum(self.grades)/len(self.grades)
    
    # display_info(self): Prints the student’s name, email, 
    # and grades.
    def display_info(self):
        """ Prints the student’s name, email, and grades. """
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        
    # Part 4: Tuple Practice - Add a method to the Student class 
    # called grades_tuple(self) that returns the grades 
    # as a tuple.
    def grades_tuple(self):
        """ Returns the grades as a tuple. """
        return tuple(self.grades)
    
# Part 2: Working with Objects

# Create 3 student objects with different names, emails, 
# and initial grades.

print("\nPart 2: Working with Objects\n")
print("Creating Student Objects\n")

""" Creating three student objects with different names, emails, and initial grades """
student1 = Student("Alice Nelson", "alice.nelson@example.com", [85, 90, 78, 100])
student2 = Student("Mike Brady", "mike.brady@example.com", [88, 92, 79, 95])
student3 = Student("Carol Brady", "carol.brady@example.com", [90, 85, 88, 92])

# Create a list of all students for easy iteration
students = [student1, student2, student3]

# Add 2 new grades to each student using the add_grade method.
students[0].add_grade(95)
students[0].add_grade(87)
students[1].add_grade(91)
students[1].add_grade(89)
students[2].add_grade(93)
students[2].add_grade(90)

# Print the information and average grade for each student using display_info.
print("Printing Student Information\n")
print("Student 1 Info:")
student1.display_info()
print(f"Average Grade: {student1.average_grade()}")
print("\nStudent 2 Info:")
student2.display_info()
print(f"Average Grade: {student2.average_grade()}")
print("\nStudent 3 Info:")
student3.display_info()
print(f"Average Grade: {student3.average_grade()}") 

# Part 3: Dictionary & Set Integration

# Create a dictionary called student_dict 
# that maps each student’s email to their 
# corresponding Student object.

""" Creating a dictionary that maps each student's email to their corresponding Student object """
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

# Write a function get_student_by_email(email) 
# that retrieves a student object 
# from the dictionary safely using .get().

def get_student_by_email(email, student_dict):
    """ Retrieves a student object from the dictionary safely using .get(). """
    return student_dict.get(email)

# Demonstrate retrieving a student by email and printing their info.
print("\nPart 3 - Retrieving Student by Email:\n")
email_to_lookup = "alice.nelson@example.com"
student = get_student_by_email(email_to_lookup, student_dict)
if student:
    student.display_info()
else:
    print("Student not found.")
    
# Create a set of all unique grades 
# across all students and print it.
unique_grades = set()
for student in student_dict.values():
    unique_grades.update(student.grades)
    
print("\nUnique Grades Across All Students: ", unique_grades)

# Part 4: Tuple Practice
# Add a method to the Student class called grades_tuple(self) 
# that returns the grades as a tuple.

# Refer to the grades_tuple method in the Student class above.

# Demonstrate that tuples are immutable by trying to change 
# a value (catch the exception with try/except and print a 
# message).

try:
    grades_tuple = student1.grades_tuple()
    print("\nPart 4: Tuple Practice - Grades Tuple for Student 1: ", grades_tuple)
    grades_tuple[0] = 100  # Attempt to change the first grade
except TypeError:
    print("Cannot modify a tuple. Tuples are immutable.")
    
# Part 5: List Operations

# Remove the last grade from each student’s grades list using .pop().
if students[0].grades:
    students[0].grades.pop()
if students[1].grades:
    students[1].grades.pop()
if students[2].grades:
    students[2].grades.pop()

print("\nPart 5: List Operations - After Removing Last Grade:\n")
students[0].display_info()
print("\n")
students[1].display_info()
print("\n")
students[2].display_info()

# Access and print the first and last grade for each student.
print("\nFirst and Last Grades for Each Student:\n")
for student in students:
    if student.grades:
        print(f"{student.name} - First Grade: {student.grades[0]}, Last Grade: {student.grades[-1]}")
    else:
        print(f"{student.name} has no grades.")

# Print the number of grades each student has using len().
print("\nThe Number of Grades Each Student Has: \n")
for student in students:
    print(f"{student.name} has {len(student.grades)} grades.")

# Part 6: Bonus (Optional)
# Use regular expressions to validate that each student’s email 
# follows the format: name@domain.com.
import re

print("\nPart 6 Bonus - Email Validation\n")
for student in students:
    if re.match(r"[a-zA-Z0-9._%+-]+@[\w-]+\.[a-zA-Z]{2,}$", student.email):
        print(f"{student.email} is a valid email.")
    else:
        print(f"{student.email} is NOT a valid email.")

# Count how many grades are above 90 across all students.
high_achievers_count = 0
for student in students:
    high_achievers_count += sum(1 for grade in student.grades if grade > 90)

print(f"\nNumber of grades above 90 across all students: {high_achievers_count} \n")
