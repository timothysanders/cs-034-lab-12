#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575
from Set import BSTNode
from Set import Set
from EnrollmentManager import EnrollmentManager
from EnrollmentManager import get_student_id

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
