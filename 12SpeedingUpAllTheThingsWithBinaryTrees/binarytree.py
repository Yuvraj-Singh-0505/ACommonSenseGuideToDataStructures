class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

index = -1

def build_tree(preorder):
    global index
    index += 1
    if index >= len(preorder) or preorder[index] == -1:
        return None
    root = Node(preorder[index])
    root.left = build_tree(preorder)
    root.right = build_tree(preorder)
    return root

def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=' ')
    inorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=' ')

def level_order_traversal(root):
    if root is None:
        return
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.data, end=' ')
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    print()

preorder_list = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]
root = build_tree(preorder_list)

print("Level Order:")
level_order_traversal(root)

print("Preorder:")
preorder_traversal(root)
print()

print("Inorder:")
inorder_traversal(root)
print()

print("Postorder:")
postorder_traversal(root)
print()
