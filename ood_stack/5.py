
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



##################
ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***



******** Parking Lot ********
Enter max of car,car in soi,operation : 5 1,2,3,4 arrive 5
car 5 arrive! : Add Car 5
[1, 2, 3, 4, 5]


******** Parking Lot ********
Enter max of car,car in soi,operation : 4 1,2,3,4 arrive 5
car 5 cannot arrive : Soi Full
[1, 2, 3, 4]


******** Parking Lot ********
Enter max of car,car in soi,operation : 8 1,4,6,2,3,5,8 arrive 7
car 7 arrive! : Add Car 7
[1, 4, 6, 2, 3, 5, 8, 7]


******** Parking Lot ********
Enter max of car,car in soi,operation : 5 0 depart 3
car 3 cannot depart : Soi Empty
[]


******** Parking Lot ********
Enter max of car,car in soi,operation : 4 1,3,2 depart 1
car 1 depart ! : Car 1 was remove
[3, 2]

******** Parking Lot ********
Enter max of car,car in soi,operation : 6 2,3,5,7,8 depart 1
car 1 cannot depart : Dont Have Car 1
[2, 3, 5, 7, 8]




