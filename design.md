#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575

## Part 1: UML/CRC

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
    
    class Set {
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
    
    class EnrollmentManager {
        -students: Set
        +__init__()
        +__str__()
        +add_student(student)
        +remove_student(student)
        +find_student(student)
        +get_all_students(other_course)
        +get_common_students(other_course)
        +get_students_only_in_one_course(other_course, primary_course)
        +write_roster(filename)
        +read_roster(filename)
    }
    
    BSTNode --> BSTNode : parent, left, right
    Set o-- BSTNode : storage_root
    EnrollmentManager --> Set : students
```

## Part 3: Data Flow Sketch
```mermaid
flowchart TD
    subgraph Input_CSVs
        A1[courseA.csv]
        A2[courseB.csv]
    end

    subgraph EnrollmentManager_Instances
        B1[course_a: EnrollmentManager]
        B2[course_b: EnrollmentManager]
    end

    subgraph Read_And_Parse
        C1["read_roster(courseA.csv)"]
        C2["read_roster(courseB.csv)"]
    end

    subgraph Add_Students
        D1["add_student(student) to course_a"]
        D2["add_student(student) to course_b"]
    end

    subgraph Set_Operations
        E1["get_common_students()"]
        E2["get_students_only_in_one_course()"]
        E3["get_students_only_in_one_course()"]
        E4["get_all_students()"]
    end

    subgraph Membership_Testing
        F1["find_student(id)"]
    end

    A1 --> C1 --> B1
    A2 --> C2 --> B2
    C1 --> D1
    C2 --> D2
    D1 --> B1
    D2 --> B2

    B1 --> E1
    B2 --> E1
    B1 --> E2
    B2 --> E3
    B1 --> E4
    B2 --> E4

    B1 --> F1
    B2 --> F1
```