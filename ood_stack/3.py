
class Stack:
    def __init__(self, list=None):
        if list is None:
            self.items = []
        else:
            self.items = list  

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def color_crush(self):
        temp_stack = []
        count = 0

        while self.items:
            current = self.pop()
            if len(temp_stack) >= 2 and temp_stack[-1] == temp_stack[-2] == current:
                temp_stack.pop()
                temp_stack.pop()
                count += 1
            else:
                temp_stack.append(current)

        # Restore items back to self.items in correct order
        while temp_stack:
            self.push(temp_stack.pop())

        # if count >= 2:
        #     self.items.reverse()

        if len(self.items) == 0:
            str_line2 = 'Empty'
        else:
            str_line2 = "".join(self.items[::-1])  # Reverse the order here

        return f'{len(self.items)}\n{str_line2}\n{"Combo : " + str(count) + " ! ! !" if count >= 2 else ""}'


ls = [e for e in input("Enter Input : ").split()]

s = Stack(ls)  

print(s.color_crush())
