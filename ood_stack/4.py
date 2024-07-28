
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
    
    def watch_back(self,tree):
        count=1
        include=[]
        for each in tree:
            if each[0] == "A" :
                self.push(int(each[2:]))
                
            elif each[0] == "B":
                if self.size() == 0:
                    print(0)
                elif self.size() == 1:
                    print(1)
                else:
                    count = 1
                    max_height = self.items[-1]
                    for i in range(self.size() - 2, -1, -1):
                        if self.items[i] > max_height:
                            count += 1
                            max_height = self.items[i]
                    print(count)
ls = [e for e in input("Enter Input : ").split(',')]

s = Stack()  
s.watch_back(ls)


