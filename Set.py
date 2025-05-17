#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575
#----------------------------------------------

import csv
import random

class BSTNode:
    """
    BST nodes are used to implement our Set.

    Attributes
    ----------
    key : by default the key is the element itself unless otherwise specified
    element : string
    parent : BSTNode
    left : BSTNode
    right : BSTNode

    Methods
    -------
    get_successor()
        Returns the in-order successor node of a given node (leftmost node in the right subtree).
    get_predecessor()
        Returns the in-order predecessor node of a given node (rightmode node in the left subtree).
    """
    def __init__(self, element, key, parent=None):
        self.key = key
        self.element = element
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        """
        Returns a string representation of a BSTNode's key and element.
        
        Parameters
        ----------
        self

        Returns
        -------
        str
        """
        return f"({self.key}, {self.element})"
         
    def get_successor(self):
        """
        Returns the in-order successor of this node in the BST.

        Returns
        -------
        BSTNode
        """
        # If right child exists, successor is the leftmost node in right subtree
        if self.right:
            successor = self.right
            while successor.left:
                successor = successor.left
            return successor

        # If no right child, go up until we find a node that is a left child
        # Otherwise traverse up the tree until a parent is encountered from the left
        current = self
        while current.parent and current == current.parent.right:
            current = current.parent

        # Either we found a parent for which current is a left child, or we
        # reached root (no successor)
        return current.parent


    def get_predecessor(self):
        """
        Returns the in-order predecessor of this node in the BST.
    
        Returns
        -------
        BSTNode
        """
        # Case 1: If left child exists, go down to rightmost node in left subtree
        if self.left:
            predecessor = self.left
            while predecessor.right:
                predecessor = predecessor.right
            return predecessor
        
        # Case 2: If no left child, go up to the first parent for which current node
        # is its right child, that is, up the tree unitl a parent is encountered from
        # the right
        current = self
        while current.parent and current == current.parent.left:
            current = current.parent

        return current.parent  # Could be None if this is the minimum node



class Set:
    """
    The Set abstract data type is implented using BST Nodes.

    Attributes
    ----------
    storage_root : BSTNode
    get_key : function (by default the element itself is returned as the key)

    Methods
    -------
    __iter__()
        Returns the minimum node in the BST.
    _in_order_with_elements()
        Traverses the BST in-order (left, parent, right).
    add(element)
        Inserts an element to the Set using BST logic.
    contains(element)
         Searches the BST for an element. Returns True if the element exists in the set and False if it does not.
    remove(element)
        Removes an element from the Set using BST logic.
    union(other_set)
        Returns the union of the self set and other set.
    intersection(other_set)
        Returns the intersection of the self set and other set.
    difference(other_set)
        Returns the difference of the self set and other set.    
    get_id_key(dictionary)
        Return the ID of a student in the set as the key.
    """
    def __init__(self, get_key_function=None):
        self.storage_root = None
        self.get_key = get_key_function if get_key_function else lambda el: el


    def __iter__(self):
        """
        Returns the minimum node in the BST
        
        Returns
        -------
        BSTNode
        """
        yield from self._in_order_with_elements(self.storage_root)

    def _in_order_with_elements(self, node):
        """
        Traverses the BST in order
        
        Parameters
        ----------
        node : BSTNode
        
        Returns
        -------
        Any
        """
        if node:
            yield from self._in_order_with_elements(node.left)
            yield node.element
            yield from self._in_order_with_elements(node.right)


    def add(self, element):
        """
        Insert an element into the Set.

        Parameters
        ----------
        element : Any

        Returns
        -------
        None
        """

        key = self.get_key(element)

        def _insert(node, element, key):
            if not node:
                return BSTNode(element, key)
            if key < node.key:
                node.left = _insert(node.left, element, key)
            elif key > node.key:
                node.right = _insert(node.right, element, key)

            return node

        self.storage_root = _insert(self.storage_root, element, key)


    def contains(self, element):
        """
        Searches the Set to see if an element is contained in the Set.

        Parameters
        ----------
        element : Any

        Returns
        -------
        bool
        """
        key = self.get_key(element)

        def _search(node, key):
            if not node:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)

        return _search(self.storage_root, key)


    def remove(self, element):
        """
        Removes an element from the set.

        Parameters
        ----------
        element : Any

        Returns
        -------
        None
        """
        key = self.get_key(element)

        def _delete(node, key):
            if not node:
                print("Empty Set")
                return None               
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                successor = node.get_successor()
                node.key = successor.key
                node.element = successor.element
                node.right = _delete(node.right, successor.key)
            return node

        self.storage_root = _delete(self.storage_root, key)


    def union(self, other_set):
        """
        Return the union of two sets.

        Parameters
        ----------
        other_set : Set

        Returns
        -------
        Set
        """
        result = Set(self.get_key)
        for element in self:
            result.add(element)
        for element in other_set:
            result.add(element)
        return result


    def intersection(self, other_set):
        """
        Return the intersection of two sets.

        Parameters
        ----------
        other_set : Set

        Returns
        -------
        Set
        """
        result = Set(self.get_key)
        for element in self:
            if other_set.contains(element):
                result.add(element)
        return result


    def difference(self, other_set):
        """
        Return the difference of two sets.

        Parameters
        ----------
        other_set : Set

        Returns
        -------
        Set
        """
        result = Set(self.get_key)
        for element in self:
            if not other_set.contains(element):
                result.add(element)
        return result

    def to_list(self):
        return [node.element for node in self] 

# define a concrete get_key_function() which can be used as arguement for Set constructor
def get_id_key(dictionary):
    """
    Returns the id key of an element in a dictionary.

    Parameters
    ----------
    dictionary : dictionary (string and int pairs)

    Returns
    -------
    int
    """
    return dictionary["id"]


if __name__ == "__main__":
    a_students = [{"id": 1001, "name": "Alice"}, {"id": 1002, "name": "Bob"}, {"id": 1003, "name": "Charlie"}]
    b_students = [{"id": 1002,  "name": "Bob"}, {"id": 1003, "name": "Charlie"}, {"id": 1004, "name": "Eva"}]

    course_A = Set(get_id_key)
    course_B = Set(get_id_key)

    for student in a_students:
        course_A.add(student)
    for student in b_students:
        course_B.add(student)

    demo_output = {
        "Course A contains 'Bob'": course_A.contains({"id": 1002}),
        "Course B contains 'Charlie'": course_B.contains({"id": 1003}),
        "Course A before removing 'Charlie'": list(course_A),
    }

    course_A.remove(a_students[2])

    demo_output.update({
        "Course A after removing 'Charlie'": list(course_A),
        "Union of A and B": list(course_A.union(course_B)),
        "Intersection of A and B": list(course_A.intersection(course_B)),
        "Difference A - B": list(course_A.difference(course_B)),
        "Difference B - A": list(course_B.difference(course_A)),
    })

    for key, value in demo_output.items():
        print(f"{key}: {value}")

#=======================================================================================================================================

'''
# Michael's Implementation
#---------------------------

class Set:
    def __init__(self, get_key_function=None):
        self.storage_root = None
        if get_key_function == None:
            # By default, the key of an element is itself
            self.get_key = lambda el: el
        else:
            self.get_key = get_key_function

    def __iter__(self):
        if self.storage_root == None:
            return BSTIterator(None)
        minNode = self.storage_root
        while minNode.left != None:
            minNode = minNode.left
        return BSTIterator(minNode)
    
    def add(self, new_element):
        new_elementKey = self.get_key(new_element)
        if self.node_search(new_elementKey) != None:
            return False

        newNode = BSTNode(new_element, None)
        if self.storage_root == None:
            self.storage_root = newNode
        else:
            node = self.storage_root
            while node != None:
                if new_elementKey < self.get_key(node.data):
                    # Go left
                    if node.left:
                        node = node.left
                    else:
                        node.left = newNode
                        newNode.parent = node
                        return True
                else:
                    # Go right
                    if node.right:
                        node = node.right
                    else:
                        node.right = newNode
                        newNode.parent = node
                        return True

    def difference(self, other_set):
        result = Set(self.get_key)
        for element in self:
            if other_set.search(self.get_key(element)) == None:
                result.add(element)
        return result

    def filter(self, predicate):
        result = Set(self.get_key)
        for element in self:
            if predicate(element):
                result.add(element)
        return result

    def intersection(self, other_set):
        result = Set(self.get_key)
        for element in self:
            if other_set.search(self.get_key(element)) != None:
                result.add(element)
        return result

    def __len__(self):
        if self.storage_root == None:
            return 0
        return self.storage_root.count()

    def map(self, map_function):
        result = Set(self.get_key)
        for element in self:
            new_element = map_function(element)
            result.add(new_element)
        return result

    def node_search(self, key):
        # Search the BST
        node = self.storage_root
        while (node != None):
            # Get the node's key
            node_key = self.get_key(node.data)

            # Compare against the search key
            if node_key == key:
                return node
            elif key > node_key:
                node = node.right
            else:
                node = node.left
        return node

    def remove(self, key):
        self.remove_node(self.node_search(key))

    def remove_node(self, node_to_remove):
        if node_to_remove != None:
            # Case 1: Internal node with 2 children
            if node_to_remove.left != None and node_to_remove.right != None:
                successor = node_to_remove.get_successor()

                # Copy the data value from the successor
                dataCopy = successor.data

                # Remove successor
                self.remove_node(successor)

                # Replace node_to_remove's data with successor data
                node_to_remove.data = dataCopy

            # Case 2: Root node (with 1 or 0 children)
            elif node_to_remove is self.storage_root:
                if node_to_remove.left != None:
                    self.storage_root = node_to_remove.left
                else:
                    self.storage_root = node_to_remove.right

                if self.storage_root:
                    self.storage_root.parent = None

            # Case 3: Internal node with left child only
            elif node_to_remove.left != None:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.left)

            # Case 4: Internal node with right child only, or leaf node
            else:
                node_to_remove.parent.replace_child(node_to_remove, node_to_remove.right)

    def search(self, key):
        # Search the BST
        node = self.node_search(key)
        if node != None:
            return node.data
        return None

    def union(self, other_set):
        result = Set(self.get_key)
        for element in self:
            result.add(element)
        for element in other_set:
            result.add(element)
        return result
'''
