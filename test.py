#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575
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
    test_left_child.parent = test_node
    test_node.right = test_right_child
    test_right_child.parent = test_node
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
    assert test_node.left.parent == test_node
    assert test_node.left.right is None
    assert test_node.left.left is None

def test_node_right_child(test_node):
    assert test_node.right.key == 1020
    assert test_node.right.element == "Tim"
    assert test_node.right.parent == test_node
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
