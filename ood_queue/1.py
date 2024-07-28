
class Queue:
    def __init__(self,list=None):
        if list == None:
            self.items =[]
        else:
            self.items=list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def basic(self,q1):
        new_list=[]
        for each in q1:
            integ=each[2:].strip()
            if each[0]=='E':
                new_list+=[integ]
                self.enQueue(integ)

                print(f'Add {integ} index is {self.items.index(integ)}')
            elif each[0]=='D':
                
                if not self.isEmpty()  :
                 remove=self.deQueue()                
                 print(f'Pop {remove} size in queue is {self.size()}')
                else:
                    print(-1)
        if not self.isEmpty(): 
         print(f'Number in Queue is :  {self.items}')
        else:
            print('Empty')
q1=[e for e in input('Enter Input : ').split(',')]
q=Queue()

q.basic(q1)