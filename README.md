# PCC CS-034: Lab 12

## Group Members and Roles
Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

- Michael Jung
  - Initiate CRM for class EnrollmentManager
  - Initiate and develop the pseudocode for both class Set and class EnrollmentManager
  - Initiate the concrete implementation of class Set
  - Review and edit the design documentation
  - Add docstrings comments
  - Review and debug the concrete implementation
    
- Megan Ng:
  - Participate in the development and the reconstruction of UML/CRC & DATA FLOW
  - Rationalize the choice of underlying data structure (BST-based Set)
  - Participate in the development of pseudocode for both class Set and class EnrollmentManager
  - Edit the presentation of design document
  - Initiate and participate the concrete implementations for both class Set and EnrollmentManager
  - Review and debug the concrete implementation

- Tim Sanders:
  - Participate in the development and the reconstruction of UML/CRC & DATA FLOW
  - Provide graphical diagram for UML/CRC & DATA FLOW
  - Review and edit the design documentation
  - Review and debug the concrete implementation
  - Implement test and integrate the entire script

## 1. Objective
By the end of this lab, we have:
- Deepened our understanding of the Set abstract data type (ADT)
- Designed and implemented a concrete BST-based Set class
- Applied our BST-based Set to simulate the real-world Course Enrollment Manage System
  
## 2. Project Design

### Implement Set class with Standard BST 
In this lab, our primary focus is demonstrating set operations—union, intersection, difference—through a custom implementation of a Set class for a Course Enrollment Manager. While hash-table-based Sets offer excellent average O(1) performance, in realistic systems, their performance can potentially degrade due to hash collision. Since our goal is not to achieve the fastest set operations, we will implement our Set class using a binary search tree (BST) instead of a hash table. This approach ensures reasonably efficient operations with O(log N) time complexity and provides the benefit of being able to iterate over students in sorted order, such as by ID. To keep the BST implementation straightforward and as simple as possible—without adding balancing logic like that found in Treaps, AVL trees, or Red-Black trees—we will use a standard, unbalanced BST. This choice avoids unnecessary complexity for small to medium-sized datasets, which is suitable for our demo purposes.


### Architecture for Course Enrollment Manage System
- class BSTNode, Set (implemented with a standard BST), EnrollmentManager

### Data Flow
- Create two instances of `EnrollmentManager`: `course_a`, `course_b`
- Get students’ information from the given CSV files by calling the method `read_roster()` in class `EnrollmentManager` and store them in lists `students_a`, and `students_b`
- By calling the method `add_student()` in class `EnrollmentManager` to enroll students for course_a and course_b, respectively
- By calling the methods `get_common_students()`, `get_students_only_in_one_course(self, other, primary_course='a')`, `get_all_students()` defined in the class `EnrollmentManager` to operate common set-like behaviors defined in the class Set, including `add()`, `difference()`, `intersection()`
- By calling the method `find_student()` defined in the class `EnrollmentManager` to operate set-like membership testing `contains()`, a method defined in the class Set

## 3. Project Implementation

### 1) Our team has built a Course Enrollment Manager `EnrollmentManager` that uses our BST-based `Set` class to:
- In class EnrollmentManager, implement the following methods based on the methods defined in class Set:
    - `add_student()` (using `add()` in Set)
    - `remove_student()` (using `remove()` in Set)
    - `find_student()` (using 'contains()` in Set)
    - `get_common_students()` (using `intersection()` in Set)
    - `get_students_only_in_one_course(self, other, primary_course='a')` (both using `difference()` in Set)
    - `get_all_students()` (using `union()` in Set)

- Instantiate two student sets: `students_a` for courseA, `students_b` for courseB

- Enroll and Disenroll students for two different courses: courseA, courseB
    - `students_a.add_student(element)` & `students_b.add_student(element)`
    - `students_a.remove_student(element)` & `students_b.remove_student(element)`
- Track students enrolled for either courseA or courseB
    - `students_a.find_student(element)` & `students_b.find_student(element)`
- Track students only in courseA or courseB
  - `get_students_only_in_one_course(self, other, primary_course='a')`
- Track students in both courses 
    - `get_common_students(students_a, students_b)`
- Track all students across both course
   - `get_all_students(students_a, students_b)`
- Manage Enrollment Roster to read from a CSV file
  ```
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
    ```
- Manage Enrollment Roster to write into a CSV file
  ```
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
  ```

### 2) Test Cases
- Each class module file, `Set.py` and `EnrollmentManager.py` contains a set of integrated tests that can be run directly in Python.
##### Set
```shell
python Set.py
```
- Expected output of the test is shown below
```text
Course A contains 'Bob': True
Course B contains 'Charlie': True
Course A before removing 'Charlie': [{'id': 1001, 'name': 'Alice'}, {'id': 1002, 'name': 'Bob'}, {'id': 1003, 'name': 'Charlie'}]
Course A after removing 'Charlie': [{'id': 1001, 'name': 'Alice'}, {'id': 1002, 'name': 'Bob'}]
Union of A and B: [{'id': 1001, 'name': 'Alice'}, {'id': 1002, 'name': 'Bob'}, {'id': 1003, 'name': 'Charlie'}, {'id': 1004, 'name': 'Eva'}]
Intersection of A and B: [{'id': 1002, 'name': 'Bob'}]
Difference A - B: [{'id': 1001, 'name': 'Alice'}]
Difference B - A: [{'id': 1003, 'name': 'Charlie'}, {'id': 1004, 'name': 'Eva'}]
```
##### EnrollmentManager
```shell
python EnrollmentManager.py
```
- Expected output of the test is shown below
```text
Students in both courses: [{'id': 1002, 'name': 'Bob'}, {'id': 1003, 'name': 'Charlie'}]
Only in Course A: [{'id': 1001, 'name': 'Alice'}]
Only in Course B: [{'id': 1004, 'name': 'Eva'}]
All students across both courses: [{'id': 1001, 'name': 'Alice'}, {'id': 1002, 'name': 'Bob'}, {'id': 1003, 'name': 'Charlie'}, {'id': 1004, 'name': 'Eva'}]

Writing rosters to files...
Reading rosters from files...

Students in course_a_from_roster:
{'id': '1001', 'name': 'Alice'}
{'id': '1002', 'name': 'Bob'}
{'id': '1003', 'name': 'Charlie'}

Students in course_b_from_roster:
{'id': '1002', 'name': 'Bob'}
{'id': '1003', 'name': 'Charlie'}
{'id': '1004', 'name': 'Eva'}
```
#### Unit Tests
- Unit tests for all modules are implemented with Pytest and can be run with the following command
```shell
pytest -vv test.py
```
- Sample output of the unit tests are shown below
```
========================================================= test session starts ==========================================================
platform darwin -- Python 3.13.2, pytest-8.3.5, pluggy-1.5.0 -- /Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13
cachedir: .pytest_cache
rootdir: /Users/tim/School/cs-034-lab-12
collected 21 items                                                                                                                     

test.py::test_node_initialization PASSED                                                                                         [  4%]
test.py::test_node_string_representation PASSED                                                                                  [  9%]
test.py::test_node_left_child PASSED                                                                                             [ 14%]
test.py::test_node_right_child PASSED                                                                                            [ 19%]
test.py::test_node_get_successor PASSED                                                                                          [ 23%]
test.py::test_node_get_predecessor PASSED                                                                                        [ 28%]
test.py::test_set_storage_root PASSED                                                                                            [ 33%]
test.py::test_set_contains_membership PASSED                                                                                     [ 38%]
test.py::test_set_add PASSED                                                                                                     [ 42%]
test.py::test_set_remove PASSED                                                                                                  [ 47%]
test.py::test_set_to_list PASSED                                                                                                 [ 52%]
test.py::test_set_union PASSED                                                                                                   [ 57%]
test.py::test_set_intersection PASSED                                                                                            [ 61%]
test.py::test_set_difference PASSED                                                                                              [ 66%]
test.py::test_read_roster PASSED                                                                                                 [ 71%]
test.py::test_add_student PASSED                                                                                                 [ 76%]
test.py::test_remove_student PASSED                                                                                              [ 80%]
test.py::test_find_student PASSED                                                                                                [ 85%]
test.py::test_get_all_students PASSED                                                                                            [ 90%]
test.py::test_get_common_students PASSED                                                                                         [ 95%]
test.py::test_get_students_only_in_one_course PASSED                                                                             [100%]

========================================================== 21 passed in 0.01s ==========================================================
```
Requirement
- Design Document (PDF or Markdown) including:
  - Class diagram (UML) or CRC cards for your `Set` class and the `EnrollmentManager` class 
  - Pseudocode for each `Set` operation
  - Data-flow sketch showing how CSV input flows through your manager into sets and outputs
Submit as `design.pdf` (or `design.md`).


## 4. Deliverables Package

- Source code in a GitHub repo or zip, containing:
  - `Set.py` with your Set implementation
  - `EnrollmentManager.py` (or equivalent) With the CLI/script
  - Two sample CSV files (`courseA.csv`, `courseB.csv`)
  - `README.md` With build/run instructions and sample output
- Automated tests for your Set methods (using `unittest`, `pytest`, `JUnit`, etc.)

### Design Rubric (25 points)
| Criterion                          | Excellent (5)                                           | Good (4)                 | Fair (3)                               | Poor (≤2)                              |
|------------------------------------|---------------------------------------------------------|--------------------------|----------------------------------------|----------------------------------------|
| UML/CRC completeness (5 pt)        | All classes, methods, and attributes are clearly shown  | Minor omissions          | Missing one class or key method        | Major omissions or incorrect structure |
| Pseudocode clarity (5 pt)          | Detailed, easy-to-follow pseudocode for every op        | Mostly clear, minor gaps | Some operations are missing or unclear | Little or no pseudocode provided       |
| Data-flow sketch (5 pt)            | Clearly shows all major data movements                  | Mostly clear             | Missing one or two data flows          | Absent or very confusing sketch        |
| Rationale & discussion (5 pt)      | Explains trade-offs (e.g., underlying structure choice) | Some rationale           | Rationale is shallow or incomplete     | No rationale                           |
| Organization & presentation (5 pt) | Professional formatting, error-free                     | A few formatting issues  | Some typos/structure problems          | Hard to read, disorganized             |



### Implementation Rubric (35 points)
| Criterion                              | Excellent (7)                                             | Good (6)                                 | Fair (4-5)                                  | Poor (≤3)                          |
|----------------------------------------|-----------------------------------------------------------|------------------------------------------|---------------------------------------------|------------------------------------|
| Correctness of Set operations (10 pt)  | All methods work, handle edge cases (empty, duplicates)   | Minor edge-case misses                   | Most methods work, but some bugs            | Many methods incorrect             |
| Use of underlying structure (5 pt)     | Clean, efficient (e.g., BST, hash table)                  | Acceptable but non-optimal               | Works, really suboptimal                    | Poor choice, overly brute-force    |
| EnrollmentManager functionality (5 pt) | Reads CSVs, computes all four sets correctly, neat output | Minor formatting or one case missing     | Only computes some of the required outputs  | Missing core functionality         |
| Testing coverage (5 pt)                | ≥90% coverage, meaningful unit tests                      | ≥75% coverage                            | Some tests, major methods are untested      | No or very few tests               |
| Code quality & style (5 pt)            | Well-documented, follows style guide, clean               | Mostly clean, minor style issues         | Some style violations or sparse comments    | Hard to follow, no comments        |
| README & usability (5 pt)              | Clear build/run instructions, sample runs                 | Works, but minor omissions in the README | README incomplete, user must guess commands | No README or unusable instructions |

Submission Instructions:
- Package your design and code into a single zip: `Module12_<GroupName>.zip`
- Include a top-level `README.md` Listing group members and roles.
