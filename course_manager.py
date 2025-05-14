#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575


import csv
from bst import BSTSet

def get_student_record_key(student):
    return student["id"]

class CourseEnrollmentExtended:
    def __init__(self):
        self.students = BSTSet(get_student_record_key)

    def add_student(self, student):
        self.students.add(student)

    def remove_student(self, student):
        self.students.remove(student)

    def find_student(self, student):
        return self.students.contains(student)

    def get_common_students(self, other_course):
        return self.students.intersection(other_course.students)

    def get_students_only_in_course_a(self, other_course):
        return self.students.difference(other_course.students)

    def get_students_only_in_course_b(self, other_course):
        return other_course.students.difference(self.students)

    def get_all_students(self, other_course):
        return self.students.union(other_course.students)

    def write_roster(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name"])
            writer.writeheader()
            for student in self.students:
                writer.writerow(student)

    def read_roster(self, filename=None, file_obj=None):
        source = file_obj if file_obj else open(filename, 'r')
        with source:
            reader = csv.DictReader(source)
            for row in reader:
                self.add_student({"id": row["id"], "name": row["name"]})
