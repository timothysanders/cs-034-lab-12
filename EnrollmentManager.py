#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575


import csv
import random
from BSTNode import BSTNode
from Set import Set

# get_key_function for the intialize Set based on BST
# =====================================================
def get_student_id(student):
    return student['id']


class EnrollmentManager:
    def __init__(self):
        self.students = Set(get_student_id)
        self.courses = Set()


    def write_roster(self, filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['id', 'name']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for student in self.students:
                    writer.writerow(student)
        except (IOError, OSError) as e:
            print(f"Error writing roster to file: {e}")
        except KeyError as e:
            print(f"Error: Student data missing required key '{e}'")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def read_roster(self, filename):
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.add_student(row)
        except (IOError, OSError) as e:
            print(f"Error reading roster from file: {e}")
        except KeyError as e:
            print(f"Error: CSV data missing required column '{e}'")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def add_student(self, student):
        self.students.add(student)

    def remove_student(self, student):
        self.students.remove(student)

    def find_student(self, student_id):
        return self.students.contains(student_id)

    def get_all_students(self, other_course):
        return self.students.union(other_course.students)

    def get_common_students(self, other_course):
        return self.students.intersection(other_course.students)

    def get_students_only_in_one_course(self, other, primary_course='a'):
        if primary_course == 'a':
            # Students in self.students but not in other.students
            return self.students.difference(other.students)
        elif primary_course == 'b':
            # Students in other.students but not in self.students
            return other.students.difference(self.students)
        else:
            # Handle invalid primary_course value, e.g., raise an error
            raise ValueError("primary_course must be 'a' or 'b'")

    def add_course(self, course):
        self.courses.add(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_all_courses(self):
        return self.courses.to_list()

    def get_courses_for_student(self, student):
        return self.courses.intersection(student.courses)


    def __str__(self):
        return f"Students: {self.students}\nCourses: {self.courses}"


if __name__ == "__main__":
    course_a = EnrollmentManager()
    course_b = EnrollmentManager()

    students_a = [{"id": 1001, "name": "Alice"}, {"id": 1002, "name": "Bob"}, {"id": 1003, "name": "Charlie"}]
    students_b = [{"id": 1002, "name": "Bob"}, {"id": 1003, "name": "Charlie"}, {"id": 1004, "name": "Eva"}]

    for student in students_a:
        course_a.add_student(student)
    for student in students_b:
        course_b.add_student(student)

    test_output = {
        "Students in both courses": course_a.get_common_students(course_b).to_list(),
        "Only in Course A": course_a.get_students_only_in_course_a(course_b).to_list(),
        "Only in Course B": course_a.get_students_only_in_course_b(course_b).to_list(),
        "All students across both courses": course_a.get_all_students(course_b).to_list()
    }

    for key, value in test_output.items():
        print()
        print(f"{key}: {value}")

    # Roster Management Demonstration
    roster_filename_a = "course_a_roster.csv"
    roster_filename_b = "course_b_roster.csv"

    print("Writing rosters to files...")
    course_a.write_roster(roster_filename_a)
    course_b.write_roster(roster_filename_b)

    # Create new EnrollmentManager objects to read from the rosters
    course_a_from_roster = EnrollmentManager()
    course_b_from_roster = EnrollmentManager()

    print("Reading rosters from files...")
    course_a_from_roster.read_roster(roster_filename_a)
    course_b_from_roster.read_roster(roster_filename_b)

    # Verify that the rosters were read correctly
    print("\nStudents in course_a_from_roster:")
    for student in course_a_from_roster.students:
        print(student)

    print("\nStudents in course_b_from_roster:")
    for student in course_b_from_roster.students:
        print(student)

