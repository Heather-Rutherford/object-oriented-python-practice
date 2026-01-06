## 🛠 Hands-On Assignment: Object-Oriented Python Practice

## Overview

The objective of this exercise was to create a script and practice creating Python classes, using object-oriented programming (OOP) concepts, and working with common Python data types like lists, tuples, sets, and dictionaries.

## Requirements

- Python 3.7 or higher

## Installation and running the script

1. Clone the repository:
   ```bash
   git clone https://github.com/Heather-Rutherford/object-oriented-python-practice
   ```
2. Navigate to the project directory:
   ```bash
   cd todo-app
   ```

## Running the Application

Run the application using Python:

```bash
python oop.py
```

## Instructions

Create a Python script.
Implement all tasks using classes, objects, and methods.
Include comments to explain your code.
Submit the Github Repository with your completed work.

## Parts of the assignment

Five parts of the assignment plus a bonus part (Part 6) are described below.

## Part 1: Class Definition

Create a class called Student with the following attributes:
name (string)
email (string)
grades (list of integers)
Add the following methods:
add_grade(self, grade): Adds a grade to the grades list.
average_grade(self): Returns the average of all grades.
display_info(self): Prints the student’s name, email, and grades.

## Part 2: Working with Objects

Create 3 student objects with different names, emails, and initial grades.
Add 2 new grades to each student using the add_grade method.
Print the information and average grade for each student using display_info.

## Part 3: Dictionary & Set Integration

Create a dictionary called student_dict that maps each student’s email to their corresponding Student object.
Write a function get_student_by_email(email) that retrieves a student object from the dictionary safely using .get().
Create a set of all unique grades across all students and print it.

## Part 4: Tuple Practice

Add a method to the Student class called grades_tuple(self) that returns the grades as a tuple.
Demonstrate that tuples are immutable by trying to change a value (catch the exception with try/except and print a message).

## Part 5: List Operations

Remove the last grade from each student’s grades list using .pop().
Access and print the first and last grade for each student.
Print the number of grades each student has using len().
Part 6: Bonus (Optional)
Use regular expressions to validate that each student’s email follows the format: name@domain.com.
Count how many grades are above 90 across all students.
