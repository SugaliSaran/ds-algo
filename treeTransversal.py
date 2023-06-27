
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorderTransveral(root):
    if root == None:
        return
    inorderTransveral(root.left)
    print(root.data)
    inorderTransveral(root.right)


def preorderTransveral(root):
    if root == None:
        return
    print(root.data)
    preorderTransveral(root.left)
    preorderTransveral(root.right)


def postorderTransveral(root):
    if root == None:
        return
    preorderTransveral(root.left)
    preorderTransveral(root.right)
    print(root.data)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.right = Node(10)
root.right.right.left = Node(11)
root.left.left.right.left = Node(12)
root.left.left.right.right = Node(13)
root.right.right.left.left = Node(14)

postorderTransveral(root)
#
#                  1      -> root
#           /             \
#          2               3    ->left, rigt
#        /   \           /   \
#       4     5        6      7   -> left left, left right, right left, right right
#     /  \     \             /
#    8    9     10         11            ->-> left left left, left left right, left right right, right right left
#       /   \            /
#     12   13           14

# inorder left->root->right
# preorder root->left->right
# postorder left->right->node
