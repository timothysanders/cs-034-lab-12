#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575


import csv
import random
from BSTNode import BSTNode
from Set import Set

'''
class BSTNode:
    def __init__(self, element, key, parent=None):
        self.key = key
        self.element = element
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return f"({self.key}, {self.element})"

    def get_successor(self):
        """
        Returns the in-order successor of this node in the BST.
        """
        # If right child exists, successor is the leftmost node in right subtree
        if self.right:
            successor = self.right
            while successor.left:
                successor = successor.left
            return successor
        else:
            current = self
            while current.parent and current == current.parent.right:
                current = current.parent
            return current.parent

    def get_predecessor(self):
        """
        Returns the in-order predecessor of this node in the BST.
        """
        # Case 1: If left child exists, go down to rightmost node in left subtree
        if self.left:
            predecessor = self.left
            while predecessor.right:
                predecessor = predecessor.right
            return predecessor
        else:
            current = self
            while current.parent and current == current.parent.left:
                current = current.parent
            return current.parent


class Set:
    def __init__(self, get_key_function=None):
        self.storage_root = None
        self.get_key = get_key_function if get_key_function else lambda el: el


    def __iter__(self):
        yield from self._in_order_with_elements(self.storage_root)

    
    def _in_order_with_elements(self, node):
        if node:
            yield from self._in_order_with_elements(node.left)
            yield node.element
            yield from self._in_order_with_elements(node.right)


    def to_list(self):
        return list(iter(self))


    def add(self, new_element):
        new_element_key = self.get_key(new_element)

        def _insert(node, element, key):
            if not node:
                return BSTNode(element, key)
            if key < node.key:
                node.left = _insert(node.left, element, key)
                if node.left:
                    node.left.parent = node
            elif key > node.key:
                node.right = _insert(node.right, element, key)
                if node.right:
                    node.right.parent = node
            return node

        self.storage_root = _insert(self.storage_root, new_element, new_element_key)

    
    def contains(self, element):
        key = self.get_key(element)

        def _search(node, key):
            if not node:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.storage_root, key)

    
    def remove(self, element):
        key = self.get_key(element)

        def _delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                successor = node.get_successor()
                node.key = successor.key
                node.element = successor.element
                node.right = _delete(node.right, successor.key)
            return node

        self.storage_root = _delete(self.storage_root, key)

    
    def union(self, other_set):
        result = BSTSet(self.get_key)
        for element in self:
            result.add(element)
        for element in other_set:
            result.add(element)
        return result

    
    def intersection(self, other_set):
        result = BSTSet(self.get_key)
        for element in self:
            if other_set.contains(element):
                result.add(element)
        return result


    def difference(self, other_set):
        result = BSTSet(self.get_key)
        for element in self:
            if not other_set.contains(element):
                result.add(element)
        return result
'''
def get_student_id(student):
    return student['id']


class EnrollmentManager:
    def __init__(self):
        self.students = BSTSet(get_student_id)
        self.courses = BSTSet()


    def write_roster(self, filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['id', 'name', 'courses']
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

    def get_students_only_in_course_a(self, other_course):
        return self.students.difference(other_course.students)

    def get_students_only_in_course_b(self, other_course):
        return other_course.students.difference(self.students)

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

    # Create new CourseEnrollment objects to read from the rosters
    course_a_from_roster = CourseEnrollment()
    course_b_from_roster = CourseEnrollment()

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

