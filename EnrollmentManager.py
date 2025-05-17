#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575

import csv
from Set import Set

# get_key_function for the initialize Set based on BST
# =====================================================
def get_student_id(student):
    return student['id']


class EnrollmentManager:
    """
    Enrolls students in courses using the Set class.

    Attributes
    ----------
    students : Set
    courses : Set

    Methods
    -------
    write_roster(filename)
        Opens a CSV file and writes the roster of students to the file.
    read_roster(filename)
        Opens a CSV file and reads in the roster of students from the file.
    add_student(student)
        Uses the add() method from the Set class to add a student to the set of students.
    remove_student(student)
        Uses the remove() method from the Set class to remove a student from the set of students.
    find_student(student_id)
        Uses the contains() method from the Set class to find a student from the set of students based on ID.
    get_all_students(other_course)
        Uses the union() method from the Set class to return the union of students from two courses.   
    get_common_students(other_course)
        Uses the intersection() method from the Set class to return the intersection of students from two courses.   
    get_students_only_in_one_course(other, primary_course='a')
        Uses the difference() method from the Set class to return students who are only in one course.   
    add_course(course)
        Adds a course to the set of courses.   
    remove_course(course)
        Removes a course from the set of courses. 
    get_all_courses()
        Returns
    get_courses_for_student(student)
        Returns the courses a student is enrolled in by finding the intersection between all courses and the student's courses.    
    __str__()
        Returns a string listing all the students and courses            
    """
    def __init__(self):
        self.students = Set(get_student_id)
        self.courses = Set()


    def write_roster(self, filename: str) -> None:
        """
        Opens a csv file and writes in the roster including a student's name and id.
        
        Parameters
        ----------
        filename : str
        
        Returns
        -------
        None
        """
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

    def read_roster(self, filename: str) -> None:
        """
        Opens a csv file and reads in the roster of students.
        
        Parameters
        ----------
        filename : str
        
        Returns
        -------
        None
        """
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
    
    def add_student(self, student) -> None:
        """
        Adds a student to the Set of students.

        Parameters
        ----------
        student : key-value pair of id and name

        Returns
        -------
        None
        """
        self.students.add(student)

    def remove_student(self, student) -> None:
        """
        Removes a student from the Set of students.
        
        Parameters
        ----------
        student : key-value pair of id and name
        
        Returns
        -------
        None
        """
        self.students.remove(student)

    def find_student(self, student: str) -> bool:
        """
        Finds a student from the Set of students.
        
        Parameters
        ----------
        student: str
            key-value pair of id and name
        
        Returns
        -------
        bool
        """
        return self.students.contains(student)

    # Methods for set operations (union, intersection, difference) would
    # need to take other BSTSet instances as arguments, representing
    # the rosters of specific courses (like the sets loaded from CSVs).
    def get_all_students(self, other_course: "EnrollmentManager") -> "Set":
        """
        Returns the union of two Sets of students in two different courses
        (students that are in course a and course b combined).
        
        Parameters
        ----------
        other_course : EnrollmentManager
        
        Returns
        -------
        Set
        """
        return self.students.union(other_course.students)

    def get_common_students(self, other_course: "EnrollmentManager") -> Set:
        """
        Returns the intersection of two Sets of students in two different courses
        (students that are in both course a and course b).
        
        Parameters
        ----------
        other_course : EnrollmentManager
        
        Returns
        -------
        Set
        """
        return self.students.intersection(other_course.students)

    def get_students_only_in_one_course(self, other: "EnrollmentManager", primary_course: str ='a') -> "Set":
        """
        Returns the difference of two Sets of students in two different courses (Either students
        only in course a or course b). 
        
        Parameters
        ----------
        other : EnrollmentManager
        primary_course : str

        Returns
        -------
        Set

        Raises
        ------
        ValueError
            If the primary_course value specified is not 'a' or 'b'
        """
        if primary_course.lower() == 'a':
            # Students in self.students but not in other.students
            return self.students.difference(other.students)
        elif primary_course.lower() == 'b':
            # Students in other.students but not in self.students
            return other.students.difference(self.students)
        else:
            # Handle invalid primary_course value, e.g., raise an error
            raise ValueError("primary_course must be 'a' or 'b'")

    def add_course(self, course):
        """
        Adds a course to the Set of courses.
        
        Parameters
        ----------
        course : Set
        
        Returns
        -------
        None
        """
        self.courses.add(course)

    def remove_course(self, course):
        """
        Removes a course from the Set of courses.
        
        Parameters
        ----------
        course : Set
        
        Returns
        -------
        None
        """
        self.courses.remove(course)

    def get_all_courses(self):
        """
        Returns all the courses from the Set of courses.
        
        Returns
        -------
        list
        """
        return self.courses.to_list()

    def get_courses_for_student(self, student):
        """
        Returns a Set containing the courses that a student is enrolled in
        
        Parameters
        ----------
        student : key-value pair of student id and name
        
        Returns
        -------
        Set
        """
        return self.courses.intersection(student.courses)


    def __str__(self):
        """
        Returns a string representation of the Set of students and Set of courses
        
        Returns
        -------
        str
        """
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
        "Only in Course A": course_a.get_students_only_in_one_course(course_b).to_list(),
        "Only in Course B": course_a.get_students_only_in_one_course(course_b, primary_course="b").to_list(),
        "All students across both courses": course_a.get_all_students(course_b).to_list()
    }

    for key, value in test_output.items():
        print(f"{key}: {value}")
    print()

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

