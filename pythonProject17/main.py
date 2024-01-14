### Program

''' Bertha Wright: Program 2-3
Date: 7-Dec-2022
Assignment: Week 14
Pseudocode: None Needed
'''


### Main Program

from binarytree import tree, Node

twelve_tree = tree(height=4, is_perfect=False)

print(twelve_tree)

assert twelve_tree.height == 4
assert twelve_tree.is_perfect is False
assert twelve_tree.is_symmetric is False
assert twelve_tree.is_balanced is False
assert twelve_tree.is_perfect is False

built = Node(7)
built.left = Node(4)
built.left.right = Node(5)
built.right = Node(9)
built.right.right = Node(12)
built.right.left = Node(11)
built.left.left = Node(2)
built.left.left.right = Node(6)

print(built)

print(built.inorder)
print(built.postorder)
print(built.preorder)

