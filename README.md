# PCC CS-034: Lab 12
## 1. Objective
By the end of this lab, you will:
- Deepen your understanding of the Set abstract data type (ADT)
- Design and implement a concrete Set class (using your choice of underlying structure)
- Apply that Set to solve a small real-world problem
## 2. Project Description
Your team will build a Course Enrollment Manager that uses your Set implementation to track which students are enrolled in which courses, with no duplicate enrollments. You must:
- Implement a `Set` class supporting:
  - `add(element)`
  - `remove(element)`
  - `contains(element)`
  - `union(otherSet)`
  - `intersection(otherSet)`
  - `difference(otherSet)`
- Use your `Set` to manage enrollment for two courses:
  - Load each course’s roster from a CSV file of Student IDs 
  - Compute and display:
    - Students in both courses
    - Students are only in course A
    - Students are only in course B
    - All students across both courses
- Provide a simple CLI or script that reads in two CSVs and prints the above.
  
  - Course Roster Management (Write/Read) implemented in the class CourseEnrollment
  ```
    def write_roster(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for student in self.students:
                writer.writerow(['Student ID', 'Student Name', 'Courses'])

    def read_roster(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                student_id, student_name, courses = row
  ```
## 3. Design
### Requirement
- Design Document (PDF or Markdown) including:
  - Class diagram (UML) or CRC cards for your `Set` class and the `EnrollmentManager` class 
  - Pseudocode for each `Set` operation
  - Data-flow sketch showing how CSV input flows through your manager into sets and outputs
Submit as `design.pdf` (or `design.md`).

### Implement Set class with Standard BST 
In this lab, our primary focus is demonstrating set operations—union, intersection, difference—through a custom implementation of a Set class for a Course Enrollment Manager. While hash-table-based Sets offer excellent average O(1) performance, in realistic systems, their performance can potentially degrade due to hash collision. Since our goal is not to achieve the fastest set operations, we will implement our Set class using a binary search tree (BST) instead of a hash table. This approach ensures reasonably efficient operations with O(log N) time complexity and provides the benefit of being able to iterate over students in sorted order, such as by ID. To keep the BST implementation straightforward and as simple as possible—without adding balancing logic like that found in Treaps, AVL trees, or Red-Black trees—we will use a standard, unbalanced BST. This choice avoids unnecessary complexity for small to medium-sized datasets, which is suitable for our demo purposes.

### Design Rubric (25 points)
| Criterion                          | Excellent (5)                                           | Good (4)                 | Fair (3)                               | Poor (≤2)                              |
|------------------------------------|---------------------------------------------------------|--------------------------|----------------------------------------|----------------------------------------|
| UML/CRC completeness (5 pt)        | All classes, methods, and attributes are clearly shown  | Minor omissions          | Missing one class or key method        | Major omissions or incorrect structure |
| Pseudocode clarity (5 pt)          | Detailed, easy-to-follow pseudocode for every op        | Mostly clear, minor gaps | Some operations are missing or unclear | Little or no pseudocode provided       |
| Data-flow sketch (5 pt)            | Clearly shows all major data movements                  | Mostly clear             | Missing one or two data flows          | Absent or very confusing sketch        |
| Rationale & discussion (5 pt)      | Explains trade-offs (e.g., underlying structure choice) | Some rationale           | Rationale is shallow or incomplete     | No rationale                           |
| Organization & presentation (5 pt) | Professional formatting, error-free                     | A few formatting issues  | Some typos/structure problems          | Hard to read, disorganized             |

## 4. Implementation
### Deliverables
- Source code in a GitHub repo or zip, containing:
  - `Set.py` with your Set implementation
  - `EnrollmentManager.py` (or equivalent) With the CLI/script
  - Two sample CSV files (`courseA.csv`, `courseB.csv`)
  - `README.md` With build/run instructions and sample output
- Automated tests for your Set methods (using `unittest`, `pytest`, `JUnit`, etc.)
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
