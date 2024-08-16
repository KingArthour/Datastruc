
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)
    
    def preorder(self, node, result):
        if node:
            result.append(str(node.data))
            self.preorder(node.left, result)
            self.preorder(node.right, result)
    
    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(str(node.data))
            self.inorder(node.right, result)
    
    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(str(node.data))
    
    def breadth_first_search(self, result):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(str(node.data))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


bst = BST()
inputs = list(map(int, input("Enter Input : ").split()))

for value in inputs:
    bst.insert(value)


preorder_result = []
inorder_result = []
postorder_result = []
breadth_result = []

bst.preorder(bst.root, preorder_result)
bst.inorder(bst.root, inorder_result)
bst.postorder(bst.root, postorder_result)
bst.breadth_first_search(breadth_result)


print("Preorder : " + " ".join(preorder_result))
print("Inorder : " + " ".join(inorder_result))
print("Postorder : " + " ".join(postorder_result))
print("Breadth : " + " ".join(breadth_result))


##############
# Chapter : 7 - item : 4 - สนุกไปกับ Binary Search Tree
