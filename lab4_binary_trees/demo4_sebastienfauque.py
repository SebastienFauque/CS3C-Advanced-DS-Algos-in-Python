"""
3C Lab4 Student Driver
Topic: Binary Trees
Applicaiton: Finding Max in binary tree
Description: Test driver and demo code for implementation of BST. Contains
             tests using Pytest and demo output.
Development environment: Ubuntu 20.04
Version: Python 3.12.1
Solution File: demo4_sebastienfauque.py
Date: 06/04/2024
"""

from sebastienfauqueLab4 import BinarySearchTree, TreeNode, TraverseOrder
import pytest


# Put the test cases
def test_tree_node():
    node = TreeNode("key", 10)
    assert node.key == "key"
    assert node.val == 10
    assert node.parent is None
    assert node.leftChild is None
    assert node.rightChild is None


@pytest.fixture
def sample_tree():
    bt = BinarySearchTree()
    bt.insert(10, 10)
    bt.insert(5, 5)
    bt.insert(20, 20)
    bt.insert(3, 3)
    bt.insert(7, 7)
    bt.insert(15, 15)
    bt.insert(30, 30)
    return bt


def test_insert(sample_tree):
    assert sample_tree.root.val == 10
    assert sample_tree.root.leftChild.val == 5
    assert sample_tree.root.rightChild.val == 20
    assert sample_tree.root.leftChild.leftChild.val == 3
    assert sample_tree.root.leftChild.rightChild.val == 7
    assert sample_tree.root.rightChild.leftChild.val == 15
    assert sample_tree.root.rightChild.rightChild.val == 30


def test_search(sample_tree):
    assert sample_tree.search(15) is not None
    assert sample_tree.search(100) is None


def test_delete(sample_tree):
    sample_tree.delete(20)
    assert sample_tree.root.rightChild.val == 30
    assert sample_tree.search(20) is None


def test_inorder(sample_tree):
    assert sample_tree.traverse(TraverseOrder.INORDER) == [3, 5, 7, 10, 15, 20, 30]


def test_preorder(sample_tree):
    assert sample_tree.traverse(TraverseOrder.PREORDER) == [10, 5, 3, 7, 20, 15, 30]


def test_postorder(sample_tree):
    assert sample_tree.traverse(TraverseOrder.POSTORDER) == [3, 7, 5, 15, 30, 20, 10]


def test_size(sample_tree):
    assert sample_tree.get_size() == 7
    sample_tree.insert(25, 25)
    assert sample_tree.get_size() == 8


def test_height(sample_tree):
    assert sample_tree.get_height() == 3


def test_get_max(sample_tree):
    assert sample_tree.get_max() == 30
    sample_tree.insert(35, 35)
    assert sample_tree.get_max() == 35


# Put the run output here
def main():
    bt = BinarySearchTree()
    bt.insert(10, 10)
    bt.insert(5, 5)
    bt.insert(20, 20)
    bt.insert(3, 3)
    bt.insert(7, 7)
    bt.insert(15, 15)
    bt.insert(30, 30)

    print("Inorder traversal:", bt.traverse(TraverseOrder.INORDER))
    print("Preorder traversal:", bt.traverse(TraverseOrder.PREORDER))
    print("Postorder traversal:", bt.traverse(TraverseOrder.POSTORDER))

    print("Search for 15:", bt.search(15) is not None)
    print("Size of the tree:", bt.get_size())
    print("Height of the tree:", bt.get_height())
    print("Maximum element:", bt.get_max())

    bt.delete(20)
    print("Inorder traversal after deleting 20:", bt.traverse(TraverseOrder.INORDER))


if __name__ == "__main__":
    main()


"""
Inorder traversal: [3, 5, 7, 10, 15, 20, 30]
Preorder traversal: [10, 5, 3, 7, 20, 15, 30]
Postorder traversal: [3, 7, 5, 15, 30, 20, 10]
Search for 15: True
Size of the tree: 7
Height of the tree: 3
Maximum element: 30
Inorder traversal after deleting 20: [3, 5, 7, 10, 15, 30]

Time complexity: O(log n)
Space complexity: O(1)
"""
