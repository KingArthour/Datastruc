
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
    

    def check_order(self,value):
        EN=[]
        ES=[]

        for i in value:
           

           if i[:2]=='EN':
               EN.append(i[2:])
               self.enQueue(i[2:])
               

           elif i[:2] =='ES':
               ES.append(i[2:])
               if  self.isEmpty():
                   self.enQueue(i[2:])
               elif  not self.isEmpty() and self.items[0] in ES and self.size()>1:
                   for each in self.items:
                       if each not in ES:
                           self.items.insert(self.items.index(each),i[2:])
                           break
               elif  not self.isEmpty() and self.items[0] in ES and self.size()==1 :
                    self.enQueue(i[2:])
               elif not self.isEmpty() and self.items[0] in EN :
                   self.items.insert(0,i[2:])
                   
           
           
           elif i[0]=='D':
               
               if self.size()==0:

                 print('Empty')
               else:

                dq=self.deQueue().strip()
                print(dq)
            
        # print(ES)
        # print(EN)
        # print(self.items)
                
               

                

    

q1=[e for e in input('Enter Input : ').split(',')]
q=Queue()

q.check_order(q1)