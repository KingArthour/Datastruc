

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
    

    def below(self,value):
        below_value= [i for i in self.include if i < value]
        return below_value

    
    def get_include(self):
        return self.include

    def insert(self, data):
        self.include.append(data)
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

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def search_number(self, node):
        if node != None:
            self.printTree(node.right,)
            print(node)
            self.printTree(node.left,)
        


T = BST()
inp_first,inp_second=[i for i in input('Enter Input : ').split('|')]

inp_first_cop=[int(i)  for i in inp_first.split()]
inp_second_cop=int(inp_second)


for i in inp_first_cop:
    root = T.insert(i)
    

T.printTree(root)

print('--------------------------------------------------')



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

below_values = T.below(inp_second_cop)


sorted_below_values = bubble_sort(below_values)

if sorted_below_values:
    print(f'Below {inp_second_cop} : ', end='')
    for i in sorted_below_values:
        print(f'{i} ', end='')
else:
    print(f'Below {inp_second_cop} : Not have')


#################
# Chapter : 7 - item : 2 - หาค่า Below
















