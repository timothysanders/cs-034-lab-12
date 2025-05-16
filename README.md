# PCC CS-034: Lab 12

## Group Members and Roles
Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

- Michael Jung
  - Initiate CRM for the EnrollmentManager class
  - Initiate and develop the pseudocode for both class Set and class EnrollmentManager
  - Review and edit the design documentation
  - Add docstrings comments
  - Review and debug the concrete implementatioin
    
- Megan Ng:
  - Participate in the development and the reconstruction of UML/CRC & DATA FLOW
  - Rationalize the choice of underlying data structure (BST-based Set)
  - Participate in the development of pseudocode for both class Set and class C
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
- class BSTNode, Set (implemented with a standard BST), CourseEnrollment

### Data Flow
- Create two instances of `EnrollmentManager`: `course_a`, `course_b`
- Get students’ information from the given CSV files by calling the method `read_roster()` in class `EnrollmentManager` and store them in lists `students_a`, and `students_b`
- By calling the method `add_student()` in class `EnrollmentManager` to enroll students for course_a and course_b, respectively
- By calling the methods `get_common_students()`, `get_students_only_in_course_a()`, `get_students_only_course_b()`, `get_all_students()` defined in the class `EnrollmentManager` to operate common set-like behaviors defined in the class Set, including `add()`, `difference()`, `intersection()`
- By calling the method `find_student()` defined in the class `EnrollmentManager` to operate set-like membership testing `contains()`, a method defined in the class Set

## 3. Project Implementation

### 1) Our team has built a Course Enrollment Manager `EnrollmentManager` that uses our BST-based `Set` class to:

- Enroll and Disenroll students for two different courses: course A, course B
    - `add(element)`
    - `remove(element)`
- Track students enrolled for either course A or course B
    - `contains(element)`
- Track students only in course A or course B
  - `difference(otherSet)`
- Track students in both courses 
    - `intersection(otherSet)`
- Track all studnets across both course
   - `union(otherSet)`
- Manage Enrollment Roster to read from a CSV file
  ```
    def write_roster(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'name', 'courses']  # Define the header
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
            writer.writeheader()  # Write the header row
            for student in self.students:  
                # Assuming 'student' is a dictionary with 'id', 'name', 'courses'
                writer.writerow(student)  
    ```
- Manage Enrollment Roster to write into a CSV file
  ```
    def read_roster(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)  # Use DictReader
            for row in reader:
                # Add student to the CourseEnrollment
                self.add_student(row)
  ```

### 2) Test Cases 

Requirement
- Design Document (PDF or Markdown) including:
  - Class diagram (UML) or CRC cards for your `Set` class and the `EnrollmentManager` class 
  - Pseudocode for each `Set` operation
  - Data-flow sketch showing how CSV input flows through your manager into sets and outputs
Submit as `design.pdf` (or `design.md`).


## 3. Deliverables

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
