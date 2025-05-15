#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575

🧩 Part 1: UML/CRC
| Class                         | BSTNode                                           |
|------------------------------------|---------------------------------------------------------|--------------------------|----------------------------------------|----------------------------------------|
| Fields       | All classes, methods, and attributes are clearly shown  | Minor omissions          | Missing one class or key method        | Major omissions or incorrect structure |
| Behaviors         | Detailed, easy-to-follow pseudocode for every op        | Mostly clear, minor gaps | Some operations are missing or unclear | Little or no pseudocode provided       |
| Data-flow sketch (5 pt)            | Clearly shows all major data movements                  | Mostly clear             | Missing one or two data flows          | Absent or very confusing sketch        |
| Rationale & discussion (5 pt)      | Explains trade-offs (e.g., underlying structure choice) | Some rationale           | Rationale is shallow or incomplete     | No rationale                           |
| Organization & presentation (5 pt) | Professional formatting, error-free                     | A few formatting issues  | Some typos/structure problems          | Hard to read, disorganized             |


🔷 BSTNode Class

Class:                     BSTNode
Fields:          element            key
Behaviors:       get_successor()




🔷 Set Class
Class: 
Set
Fields:
storage_root
get_key
Behaviors:
add()
remove()
_min_value_node()
__iter__()
_in_order_with_elements()
contains()
union()
intersection()
difference()
to_list()



🔷 EnrollmentManager Class
Class: 
EnrollmentManager
Fields:
course_a
course_b
Behaviors:
load_student_roster()
students_in_both_courses()
students_only_in_course_a()
students_only_in_course_b()
all_students()









```mermaid
classDiagram
    class BSTNode {
        -element
        -key
        -parent = None
        -left
        -right
        +get_successor()
    }
    
    class BSTIterator {
        -root
        +__next__()
        +next()
    }
    
    class Set {
        -storage_root
        -get_key
        +add()
        +remove()
        +min_value_node()
        +__iter__()
        +to_list()
        +contains()
        +union()
        +intersection()
        +difference()
    }
    
    class EnrollmentManager {
        -course_a
        -course_b
        +load_student_roster()
        +students_in_both_courses()
        +students_only_in_course_a()
        +students_only_in_course_b()
        +all_students()
    }
    
    Set *-- BSTNode : contains
    BSTIterator ..> BSTNode : uses
    Set --> BSTIterator : creates
    EnrollmentManager --> Set : uses
```
