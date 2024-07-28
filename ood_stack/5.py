
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
    
    def jod_rod(self,data):
        rod_in_soi=data[1].split(',')
        rod_int=[int(i) for i in rod_in_soi] #this part manby not neccessary //// can change this in self.items
        if data[1] == '0':
                self.items=[]
        else:
                self.items=data[1].split(',')

 

        if data[2]=='arrive':

                
            if self.size()==int(data[0]) :
                print(f'car {data[3]} cannot arrive : Soi Full')
                
            elif data[3] in self.items:
                print(f'car {data[3]} already in soi')

            
            else:
                self.push(data[3])
                print(f'car {data[3]} arrive! : Add Car {data[3]}')



        elif data[2]=='depart':
            if  data[3] in self.items:
                print(f'car {data[3]} depart ! : Car {data[3]} was remove')
                self.items.remove(data[3])
            elif data[3] not in self.items and not self.isEmpty() :
                print(f'car {data[3]} cannot depart : Dont Have Car {data[3]}')
            elif self.isEmpty():
                print(f'car {data[3]} cannot depart : Soi Empty')
        self.items=[int(i) for i in self.items]
        print(self.items)

print('******** Parking Lot ********')    
ls = [e for e in input("Enter max of car,car in soi,operation : ").split(' ')]
# print(ls)
s = Stack()  

s.jod_rod(ls)