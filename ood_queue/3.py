
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
##############
# หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  ผิดทั้งหมดกฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

#     โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงลำดับของสีที่เหลือจากขวาไปซ้าย


# Enter Input : G H H H H P
# 3
# PHG



# Enter Input : L C C X X X C D
# 2
# DL
# Combo : 2 ! ! !

# Enter Input : C C C
# 0
# Empty


