
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self):
        self.root = None

    def build_tree(self, postfix):
        stack = []
        operators = set(['+', '-', '*', '/'])
        
        for char in postfix:
            if char not in operators:
                node = Node(char)
                stack.append(node)
            else:
                node = Node(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        
        self.root = stack[-1]

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node.data)
            self.print_tree(node.left, level + 1)
    
    def to_infix(self, node):
        if node is None:
            return ''
        if node.left is None and node.right is None:
            return node.data
        left_expr = self.to_infix(node.left)
        right_expr = self.to_infix(node.right)
        return f'({left_expr}{node.data}{right_expr})'
    
    def to_prefix(self, node):
        if node is None:
            return ''
        left_expr = self.to_prefix(node.left)
        right_expr = self.to_prefix(node.right)
        return f'{node.data}{left_expr}{right_expr}'


postfix_input = input("Enter Postfix : ")

expr_tree = ExpressionTree()
expr_tree.build_tree(postfix_input)


print("Tree :")
expr_tree.print_tree(expr_tree.root)


infix_expression = expr_tree.to_infix(expr_tree.root)
prefix_expression = expr_tree.to_prefix(expr_tree.root)

print("--------------------------------------------------")
print(f'Infix : {infix_expression}')
print(f'Prefix : {prefix_expression}')


##############
# Chapter : 7 - item : 5 - Expression Tree
