
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.include=[]

    def __str__(self):
        return str(self.root)
    def get_include(self):
        return self.include

    def insert(self, data):
        
        if self.root is None:
            self.root = Node(data)
            
            return self.root
            
        else:
            return self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)
        return node
    
    def search_Tree(self, node, value):
        if node==None:
            return None  
        if node.data ==value:
            return self.include_node(node)
        elif value<node.data:
            return self.search_Tree(node.left,value)
        else:
            return self.search_Tree(node.right,value)
    def include_node(self, node,):
        if node is not None:
            self.include.append(node.data)
            self.include_node(node.left)
            self.include_node(node.right)
        return self.include
            
T = BST()
inp_first,inp_second=[i for i in input('Enter the BST values and search value: ').split(', ')]

inp_first_cop=[int(i)  for i in inp_first.split()]
inp_second_cop=int(inp_second)

print(f'Input: root = {inp_first_cop}, val = {inp_second_cop}')
for i in inp_first_cop:
    root = T.insert(i)

result=T.search_Tree(root,inp_second_cop)
if result:
    print(f'Output: {T.get_include()}')
    
else:
    print('Output: []')


####################
# Chapter : 7 - item : 3 - ลูกจ๋าอยู่ไหน




