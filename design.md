#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575

Part 1: UML/CRC

```mermaid
classDiagram
    class BSTNode {
        -key
        -element
        -parent: BSTNode = None
        -left: BSTNode = None
        -right: BSTNode = None
        +__init__(element, key, parent=None)
        +__str__()
        +get_successor()
        +get_predecessor()
    }
    
    class BSTSet {
        -storage_root: BSTNode
        -get_key: function
        +__init__(get_key_function=None)
        +__iter__()
        +_in_order_with_elements(node)
        +add(new_element)
        +contains(new_element)
        +remove(element)
        +union(other_set)
        +intersection(other_set)
        +difference(other_set)
        +to_list()
    }
    
    class CourseEnrollmentExtended {
        -students: BSTSet
        +__init__()
        +add_student(student)
        +remove_student(student)
        +find_student(student)
        +get_common_students(other_course)
        +get_students_only_in_course_a(other_course)
        +get_students_only_in_course_b(other_course)
        +get_all_students(other_course)
        +write_roster(filename)
        +read_roster(filename, file_obj)
    }
    
    BSTNode --> BSTNode : parent, left, right
    BSTSet o-- BSTNode : storage_root
    CourseEnrollmentExtended --> BSTSet : students
```
