"""
3C Lab4 Student solution - Sebastien Fauque
Topic: Binary Trees
Application: Finding Max in binary tree
Description: Package of a binary tree which can point to left and right
             children and preform some basic operations. Can traverse the
             tree in preorder, inorder,
             and postorder traversal.
Development environment: Ubuntu 20.04
Version: Python 3.12.1
Solution FIle: sebastienfauqueLab4.py
Date: 06/04/2024
"""

from enum import Enum


class TraverseOrder(Enum):
    """Enum to only allow traversing with predefined order types."""

    PREORDER = "preorder"
    INORDER = "inorder"
    POSTORDER = "postorder"


class TreeNode:
    """Individual nodes of the BST."""

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self) -> bool:
        """Returns bool if left child exists."""
        return self.leftChild

    def hasRightChild(self) -> bool:
        """Returns bool is right child exists."""
        return self.rightChild

    def isLeftChild(self) -> bool:
        """Returns True if the left child is self."""

        return self.parent and self.parent.leftChild == self

    def isRightChild(self) -> bool:
        """Returns True if the right child is self."""
        return self.parent and self.parent.rightChild == self

    def isRoot(self) -> bool:
        """Returns true if a parent node doesn't exist."""
        return not self.parent

    def isLeaf(self) -> bool:
        """Returns true if not a right or left child."""
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self) -> bool:
        """Returns True if Node has children."""
        return self.rightChild or self.leftChild

    def hasBothChildren(self) -> bool:
        """Returns True if both children nodes exist."""
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        """Replaces node with new data."""
        self.key = key
        self.val = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def spliceOut(self):
        """Removes item from BST and reorders with remaining vals."""
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        """Finds the next successor child to replace removed node."""
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        """Finds the node with the min value."""
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findMax(self):
        """Finds the node with the max value."""
        current = self
        while current.hasRightChild():
            current = current.rightChild
        return current.val


class BinarySearchTree:
    """The binary search tree data structure to store data."""

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, value) -> None:
        """Inserts a value into the BST."""
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._insert(key, value, currentNode=self.root)

        self.size += 1

    def _insert(self, key, value, currentNode=None) -> None:
        """Private method for inserting a node into this BST."""
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._insert(key, value, currentNode.leftChild)
            else:
                newNode = TreeNode(key, value, parent=currentNode)
                currentNode.leftChild = newNode
        else:
            if currentNode.hasRightChild():
                self._insert(key, value, currentNode.rightChild)
            else:
                newNode = TreeNode(key, value, parent=currentNode)
                currentNode.rightChild = newNode

    def search(self, key):
        """Finds a value in the BST given on the key."""
        if self.root:
            resultNode = self._search(key, self.root)

            if resultNode:
                return resultNode
        return None

    def _search(self, key, currentNode):
        """Private method for finding a node when given a key."""
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        else:
            if key < currentNode.key:
                if currentNode.hasLeftChild():
                    return self._search(key, currentNode.leftChild)
                else:
                    return None
            else:
                if currentNode.hasRightChild():
                    return self._search(key, currentNode.rightChild)
                else:
                    return None

    def delete(self, key):
        """Deletes a value from the BST."""
        if self.size < 1:
            raise KeyError("Error, key not in tree.")
        elif self.size > 1:
            nodeToDelete = self._search(key, self.root)
            if nodeToDelete:
                self.remove(nodeToDelete)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree.")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree.")

    def remove(self, currentNode):
        """Removes value from BST in cases where the BST has
        a size > than 1."""
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.val = succ.val

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.payload,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild,
                    )

            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.payload,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild,
                    )

    def traverse(self, order: TraverseOrder):
        """Calls the correct traverse method."""
        result = []
        if order == TraverseOrder.PREORDER:
            self.preorder_traverse(self.root, result)
        elif order == TraverseOrder.INORDER:
            self.inorder_traverse(self.root, result)
        elif order == TraverseOrder.POSTORDER:
            self.postorder_traverse(self.root, result)

        return result

    def postorder_traverse(self, currentNode: TreeNode, result=None):
        """Prints out the postorder traversal of the BST."""
        if currentNode is None:
            return None
        if result is None:
            result = []

        self.postorder_traverse(currentNode.leftChild, result)

        self.postorder_traverse(currentNode.rightChild, result)

        result.append(currentNode.val)

    def inorder_traverse(self, currentNode: TreeNode, result=None):
        """Prints out the inorder traversal of the BST."""
        if currentNode is None:
            return None
        if result is None:
            result = []

        self.inorder_traverse(currentNode.leftChild, result)

        result.append(currentNode.val)

        self.inorder_traverse(currentNode.rightChild, result)

    def preorder_traverse(self, currentNode: TreeNode, result=None):
        """Prints out the preorder traversal of the BST."""
        if currentNode is None:
            return None
        if result is None:
            result = []

        result.append(currentNode.val)

        self.preorder_traverse(currentNode.leftChild, result)

        self.preorder_traverse(currentNode.rightChild, result)

    def get_max(self):
        """Gets the maximum element in the BST using recursion.

        The word 'element' from the instructions isn't very descriptive,
        so I take that to mean the treeNode with the largest value."""
        if self.size < 1:
            return None
        elif self.size == 1:
            return self.root

        return self.root.findMax()

    def get_size(self):
        """Returns the size of the tree."""
        return self.size

    def get_height(self):
        """Returns the height of the tree."""
        if self.root is None:
            return None
        return self.max_depth(self.root)

    def max_depth(self, currentNode):
        """Returns the depth of the bst."""
        if currentNode is None:
            return 0
        else:
            lDepth = self.max_depth(currentNode.leftChild)
            rDepth = self.max_depth(currentNode.rightChild)

            if lDepth > rDepth:
                return lDepth + 1
            else:
                return rDepth + 1
