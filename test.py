#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575
import csv

import pytest

from Set import BSTNode
from Set import Set
from EnrollmentManager import EnrollmentManager
from EnrollmentManager import get_student_id

@pytest.fixture
def test_node():
    test_node = BSTNode(element="Miles", key=1010)
    test_left_child = BSTNode(element="Mae", key=1001)
    test_right_child = BSTNode(element="Tim", key=1020)
    test_node.left = test_left_child
    test_node.right = test_right_child
    return test_node

@pytest.fixture
def test_set():
    test_set = Set(get_key_function=str.lower)
    test_set.add(element="Tim")
    test_set.add(element="miles")
    test_set.add(element="mae")
    return test_set

@pytest.fixture
def test_course():
    test_course = EnrollmentManager()
    test_students = [{"id": 1001, "name": "Alice"}, {"id": 1002, "name": "Bob"}, {"id": 1003, "name": "Charlie"}]
    for student in test_students:
        test_course.add_student(student)
    return test_course

@pytest.fixture(scope="session")
def test_roster_file_a(tmp_path_factory):
    test_students = [{"id": 1001, "name": "Mae"}, {"id": 1002, "name": "Miles"}, {"id": 1003, "name": "Misty"}, {"id": 1013, "name": "Tim"}]
    fn = tmp_path_factory.mktemp("data") / "test_course.csv"
    with open(fn, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in test_students:
            writer.writerow(student)
    return fn

@pytest.fixture(scope="session")
def test_roster_file_b(tmp_path_factory):
    test_students = [{"id": 1011, "name": "Megan"}, {"id": 1012, "name": "Michael"}, {"id": 1013, "name": "Tim"}]
    fn = tmp_path_factory.mktemp("data") / "test_course.csv"
    with open(fn, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for student in test_students:
            writer.writerow(student)
    return fn
def test_node_initialization():
    test_node = BSTNode(element="Tim", key=1010)
    assert test_node.key == 1010
    assert test_node.element == "Tim"
    assert test_node.parent is None
    assert test_node.left is None
    assert test_node.right is None

def test_node_string_representation(test_node, capsys):
    print(test_node)
    captured = capsys.readouterr().out
    assert captured == "(1010, Miles)\n"

def test_node_left_child(test_node):
    assert test_node.left.key == 1001
    assert test_node.left.element == "Mae"
    assert test_node.left.right is None
    assert test_node.left.left is None

def test_node_right_child(test_node):
    assert test_node.right.key == 1020
    assert test_node.right.element == "Tim"
    assert test_node.right.right is None
    assert test_node.right.left is None

def test_node_get_successor(test_node):
    # BSTNode.get_successor() should return the left-most node of the right subtree
    # Since our subtree only contains one node, it should be 1020, "Tim"
    test_node_successor = test_node.get_successor()
    assert test_node_successor.key == 1020
    assert test_node_successor.element == "Tim"

def test_node_get_predecessor(test_node):
    # BSTNode.get_predecessor() should return the right-most node of the left subtree
    # Since our subtree only contains one node, it should be 1001, "Mae"
    test_node_predecessor = test_node.get_predecessor()
    assert test_node_predecessor.key == 1001
    assert test_node_predecessor.element == "Mae"

def test_set_storage_root(test_set):
    assert type(test_set.storage_root) == BSTNode
    assert test_set.storage_root.key == "tim"

def test_set_contains_membership(test_set):
    assert test_set.contains("TIM")
    assert test_set.contains("Tim")
    assert test_set.contains("tim")

def test_set_add(test_set):
    test_set.add("MISTY")
    assert test_set.contains("MISTY")
    assert test_set.contains("Misty")
    assert test_set.contains("misty")
    assert test_set.contains("miles")
    assert test_set.contains("mae")
    assert test_set.contains("tim")

def test_set_remove(test_set):
    assert test_set.contains("miles")
    assert test_set.contains("mae")
    assert test_set.contains("tim")
    test_set.remove("tim")
    assert not test_set.contains("tim")
    assert test_set.contains("miles")
    assert test_set.contains("mae")

def test_set_to_list(test_set):
    assert test_set.to_list() == ["mae", "miles", "Tim"]

def test_set_union(test_set):
    test_union_set = Set(get_key_function=str.lower)
    test_union_set.add("Tim")
    test_union_set.add("Megan")
    test_union_set.add("Michael")
    union_result_set = test_set.union(test_union_set)
    assert len(test_set.to_list()) == 3
    assert len(test_union_set.to_list()) == 3
    assert union_result_set.contains("miles")
    assert union_result_set.contains("mae")
    assert union_result_set.contains("michael")
    assert union_result_set.contains("megan")
    assert union_result_set.contains("tim")
    assert len(union_result_set.to_list()) == 5

def test_set_intersection(test_set):
    test_intersection_set = Set(get_key_function=str.lower)
    test_intersection_set.add("Tim")
    test_intersection_set.add("Megan")
    test_intersection_set.add("Michael")
    intersection_result_set = test_set.intersection(test_intersection_set)
    assert intersection_result_set.contains("tim")
    assert not intersection_result_set.contains("megan")
    assert not intersection_result_set.contains("miles")
    assert len(intersection_result_set.to_list()) == 1

def test_set_difference(test_set):
    test_difference_set = Set(get_key_function=str.lower)
    test_difference_set.add("Tim")
    test_difference_set.add("Megan")
    test_difference_set.add("Michael")
    difference_result_set = test_set.difference(test_difference_set)
    assert not difference_result_set.contains("tim")
    assert difference_result_set.contains("miles")
    assert difference_result_set.contains("mae")
    assert len(difference_result_set.to_list()) == 2

def test_read_roster(test_roster_file_a):
    test_enrollment_manager = EnrollmentManager()
    assert test_enrollment_manager.students.to_list() == []
    test_enrollment_manager.read_roster(test_roster_file_a)
    assert test_enrollment_manager.students.to_list() ==  [{"id": "1001", "name": "Mae"}, {"id": "1002", "name": "Miles"}, {"id": "1003", "name": "Misty"}, {"id": "1013", "name": "Tim"}]

def test_add_student(test_roster_file_a):
    test_enrollment_manager = EnrollmentManager()
    test_enrollment_manager.read_roster(test_roster_file_a)
    test_enrollment_manager.add_student({"id": "1030", "name": "Danielle"})
    assert {"id": "1030", "name": "Danielle"} in test_enrollment_manager.students.to_list()

def test_remove_student(test_roster_file_a):
    test_enrollment_manager = EnrollmentManager()
    test_enrollment_manager.read_roster(test_roster_file_a)
    test_enrollment_manager.remove_student({"id": "1001", "name": "Mae"})
    assert {"id": "1001", "name": "Mae"} not in test_enrollment_manager.students.to_list()

def test_find_student(test_roster_file_a):
    test_enrollment_manager = EnrollmentManager()
    test_enrollment_manager.read_roster(filename=test_roster_file_a)
    assert test_enrollment_manager.find_student({"id": "1001", "name": "Mae"})

def test_get_all_students(test_roster_file_a, test_roster_file_b):
    test_enrollment_manager_a = EnrollmentManager()
    test_enrollment_manager_a.read_roster(filename=test_roster_file_a)
    test_enrollment_manager_b = EnrollmentManager()
    test_enrollment_manager_b.read_roster(filename=test_roster_file_b)
    expected_students = [
        {'id': '1001', 'name': 'Mae'},
        {'id': '1002', 'name': 'Miles'},
        {'id': '1003', 'name': 'Misty'},
        {'id': '1011', 'name': 'Megan'},
        {'id': '1012', 'name': 'Michael'},
        {'id': '1013', 'name': 'Tim'}
    ]
    assert test_enrollment_manager_a.get_all_students(test_enrollment_manager_b).to_list() == expected_students

def test_get_common_students(test_roster_file_a, test_roster_file_b):
    test_enrollment_manager_a = EnrollmentManager()
    test_enrollment_manager_a.read_roster(filename=test_roster_file_a)
    test_enrollment_manager_b = EnrollmentManager()
    test_enrollment_manager_b.read_roster(filename=test_roster_file_b)
    expected_students = [
        {"id": "1013", "name": "Tim"}
    ]
    unexpected_students = [
        {"id": "1001", "name": "Mae"}
    ]
    assert test_enrollment_manager_a.get_common_students(test_enrollment_manager_b).to_list() == expected_students
    assert not test_enrollment_manager_a.get_common_students(test_enrollment_manager_b).to_list() == unexpected_students

def test_get_students_only_in_one_course(test_roster_file_a, test_roster_file_b):
    test_enrollment_manager_a = EnrollmentManager()
    test_enrollment_manager_a.read_roster(filename=test_roster_file_a)
    test_enrollment_manager_b = EnrollmentManager()
    test_enrollment_manager_b.read_roster(filename=test_roster_file_b)
    expected_students_a = [{'id': '1001', 'name': 'Mae'}, {'id': '1002', 'name': 'Miles'}, {'id': '1003', 'name': 'Misty'}]
    unexpected_students_a = [
        {"id": "1013", "name": "Tim"}
    ]
    expected_students_b = [
        {"id": "1011", "name": "Megan"}, {"id": "1012", "name": "Michael"}
    ]
    unexpected_students_b = [
        {"id": "1013", "name": "Tim"}
    ]
    assert test_enrollment_manager_a.get_students_only_in_one_course(test_enrollment_manager_b).to_list() == expected_students_a
    assert not test_enrollment_manager_a.get_students_only_in_one_course(test_enrollment_manager_b).to_list() == unexpected_students_a
    assert test_enrollment_manager_a.get_students_only_in_one_course(test_enrollment_manager_b, primary_course="b").to_list() == expected_students_b
    assert not test_enrollment_manager_a.get_students_only_in_one_course(test_enrollment_manager_b, primary_course="b").to_list() == unexpected_students_b

# Integrated demonstration of core class functionalities
# The integration test constructs the EnrollmentManager objects,
# reads course rosters from two CSV files, and demonstrates a set of functionality
if __name__ == "__main__":
    course_a = EnrollmentManager()
    course_b = EnrollmentManager()

    course_a.read_roster("courseA.csv")
    course_b.read_roster("courseB.csv")

    test_output = {
        "Students in both courses": course_a.get_common_students(course_b).to_list(),
        "Only in Course A": course_a.get_students_only_in_one_course(course_b).to_list(),
        "Only in Course B": course_a.get_students_only_in_one_course(course_b, primary_course="b").to_list(),
        "All students across both courses": course_a.get_all_students(course_b).to_list()
    }

    print("Integration Test Report")
    print("-----------------------")
    print()
    for key, value in test_output.items():
        print(f"    {key}:")
        print("    "+"-" * len(f"{key}:"))
        print(f"    {value}")
