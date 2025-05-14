#Group Members: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

#Date: 5/11/25

#Course: Spr25_CS_034 CRN 39575



# Revised Implement from Megan
#-------------------------------
import csv
import random

class BSTNode:
    def __init__(self, element, key, parent=None):
        self.element = element
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def get_successor(self):
        if self.right:
            successor = self.right
            while successor.left:
                successor = successor.left
            return successor
        else:
            current = self
            parent = current.parent
            while parent and current == parent.right:
                current = parent
                parent = current.parent
            return parent

    def replace_child(self, current_child, new_child):
        if current_child is self.left:
            self.left = new_child
            if self.left:
                self.left.parent = self
        elif current_child is self.right:
            self.right = new_child
            if self.right:
                self.right.parent = self

#class BSTIterator:
    #def __init__(self, root):
        # Start at the leftmost (minimum) node
        #self.node = self._min_node(root)

    #def _min_node(self, node):
        #while node and node.left:
            #node = node.left
        #return node

    #def __iter__(self):
        #return self

    #def __next__(self):
        #if not self.node:
            #raise StopIteration()
        #current = self.node.element
        #self.node = self.node.get_successor()
        #return current


class Set:
    def __init__(self, get_student_record_key=None):
        self.storage_root = None
        self.get_key = get_student_record_key( if get_student_record_key else lambda el: el

    def add(self, new_element):
        new_key = self.get_key(new_element)

        def insert(node, element, key):
            if not node:
                return BSTNode(element, key)
            if key < node.key:
                node.left = insert(node.left, element, key)
                if node.left:
                    node.left.parent = node
            elif key > node.key:
                node.right = insert(node.right, element, key)
                if node.right:
                    node.right.parent = node
            return node

        self.storage_root = insert(self.storage_root, new_element, new_key)

    def contains(self, element):
        key = self.get_key(element)

        def search(node, key):
            if not node:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return search(node.left, key)
            else:
                return search(node.right, key)

        return search(self.storage_root, key)

    def remove(self, element):
        key = self.get_key(element)

        def delete(node, key):
            if not node:
                return None
            if key < node.key:
                node.left = delete(node.left, key)
            elif key > node.key:
                node.right = delete(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                successor = self._min_value_node(node.right)
                node.key = successor.key
                node.element = successor.element
                node.right = delete(node.right, successor.key)
            return node

        self.storage_root = delete(self.storage_root, key)

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def union(self, other):
        result = BSTSet(self.get_key)
        for el in self:
            result.add(el)
        for el in other:
            result.add(el)
        return result

    def intersection(self, other):
        result = BSTSet(self.get_key)
        for el in self:
            if other.contains(el):
                result.add(el)
        return result

    def difference(self, other):
        result = BSTSet(self.get_key)
        for el in self:
            if not other.contains(el):
                result.add(el)
        return result

    #def __iter__(self):
        #return BSTIterator(self.storage_root)

    # Prefer this implementation other than the one applying BSTIterator
    
    def iter(self):
        yield from self._in_order(self.storage_root)

    def _in_order(self, node):
        if node:
            yield from self._in_order(node.left)
            yield node.key
            yield from self._in_order(node.right)

    def to_list(self):
        return list(iter(self))



def get_student_id(student):
    return student



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
