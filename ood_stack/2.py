
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
    
    def ManageStack(self,value):
        
        for each in value:

            if each[0] == 'A':
                print('Add = '+f'{int(each[2:])}')
                
                self.push(str(each[2:]))
                
            elif each[0] == 'P' and len(self.items)>0:
                print('Pop = '+ self.pop())
            elif each[0] == 'P' and len(self.items)==0:
                print(-1)

            elif each[0] == 'D' :
                check=each[2:].strip()
                if check in self.items:
                    for step in range(self.items.count(check)):
                     self.items.remove(check)
                     print(f'Delete = {int(check)}')
                elif self.size() ==0:
                    print(-1)

            elif each[0:2] == 'LD' :
                removal=[int(i) for i in self.items if int(i)<int(each[2:])]
                if removal:
                    removal.sort()
                    for x in removal:
                        print(f'Delete = {x} Because {x} is less than {int(each[2:])}')
                    self.items=[i for i in self.items if int(i)>=int(each[2:])]
                elif self.size() ==0:
                    print(-1)

            elif each[0:2] == 'MD' :
                removal=[int(i) for i in self.items if int(i)>int(each[2:])]
                if removal:
                    
                    removal.sort()
                    
                    for x in removal:
                        print(f'Delete = {x} Because {x} is more than {int(each[2:])}')
                    self.items=[i for i in self.items if int(i)<=int(each[2:])]

                
                elif self.size() ==0:
                    print(-1)

            
            output=[int(e) for e in self.items]

                        
        print(f'Value in Stack = {output}')
  


ls = [e for e in input("Enter Input : ").split(',')]

s = Stack()  
s.ManageStack(ls)


