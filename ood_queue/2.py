
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


#############
PSD48 (P-Saderd 48 Group) เป็นวงไอดอลวงหนึ่งที่กระแสกำลังมาแรง ณ ตอนนี้โดยเพลงที่ได้รับความนิยมอย่างมากคือเพลงจี่หอย โดยวง PSD48 กำลังจะจัดงานจับมือขึ้น โดยมีกฎอยู่ว่าถ้าหากคนที่กำลังต่อแถวอยู่เป็นคนจาก กองกำลังสำรวจ จะได้สิทธิพิเศษในการแทรกแถวไปข้างหน้าสุดทันที (แต่ถ้าหากคนหน้าสุดก็เป็นคนของกองกำลังสำรวจก็ต้องต่อหลังเขาอยู่ดี)  PSD48 อยากให้คุณช่วยเขียนโปรแกรมสำหรับหาว่าจะมีโอตะ id ใดบ้างที่ได้จับมือ

เพลงประกอบ : https://youtu.be/Jd4Hd-HFgls

Input :
EN <value>  เป็นโอตะธรรมดา  id = value
ES <value>  เป็นโอตะของกองกำลังสำรวจ  id = value
D                  เป็นคำสั่งแสดงผล value ของหัวแถว ถ้าหากในแถวไม่มีคนจะแสดงคำว่า Empty




Enter Input : EN 1,EN 2,D,D,D,EN 3,D
1
2
Empty
3








Enter Input : EN 1,ES 2,D,D,D,EN 3,D
2
1
Empty
3






Enter Input : EN 1,ES 2,ES 99,D,D,D,EN 3,D
2
99
1
3
