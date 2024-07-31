
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



###################################
# จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

# A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

# P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

# D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

# LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

# MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

# การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

# *** Hint ***

# ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ





# Enter Input : P,P,MD 7,LD 7,D 7
# -1
# -1
# -1
# -1
# -1
# Value in Stack = []




# Enter Input : A 1,A 2,A 3,A 2,MD 2
# Add = 1
# Add = 2
# Add = 3
# Add = 2
# Delete = 3 Because 3 is more than 2
# Value in Stack = [1, 2, 2]



# Enter Input : A 3,A 3,A 3,P,A 2,A 10,A 5,A 7,A 8,D 3,LD 5
# Add = 3
# Add = 3
# Add = 3
# Pop = 3
# Add = 2
# Add = 10
# Add = 5
# Add = 7
# Add = 8
# Delete = 3
# Delete = 3
# Delete = 2 Because 2 is less than 5
# Value in Stack = [10, 5, 7, 8]



# Enter Input : A 0,A 0,A 1,A 6,A 5,P,P,P,D 6,LD 0,D 0
# Add = 0
# Add = 0
# Add = 1
# Add = 6
# Add = 5
# Pop = 5
# Pop = 6
# Pop = 1
# Delete = 0
# Delete = 0
# Value in Stack = []



# Enter Input : D 10,A -1,A -3,A 1,A 4,A 8,D 1,LD 0
# -1
# Add = -1
# Add = -3
# Add = 1
# Add = 4
# Add = 8
# Delete = 1
# Delete = -3 Because -3 is less than 0
# Delete = -1 Because -1 is less than 0
# Value in Stack = [4, 8]

