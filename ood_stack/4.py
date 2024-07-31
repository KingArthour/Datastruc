
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



############################
# กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป

# ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

# อธิบาย Input :   A  <Heights>  แสดงถึงความสูงของต้นไม้  ,   B  คือการหันหลังกลับมามอง

# อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

# โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง

# class Stack:

#     ### Enter Your Code Here ###

# S = Stack()


# inp = input('Enter Input : ').split(',')

# ### Enter Your Code Here ###


# Enter Input : A 4,A 3,B,A 5,A 8,B
# 2
# 1



# Enter Input : A 8,A 3,A 2,A 6,A 2,B,A 10,B
# 3
# 1





# Enter Input : B,B,B,A 10,A 1,A 3,A 2,B,A 1,A 1,B,A 5,A 4,B
# 0
# 0
# 0
# 3
# 4
# 3



# Enter Input : A 1,A 2,A 3,A 4,B,A 3,A 2,B,A 99,A 5,B,A 4,B,A 67
# 1
# 3
# 2
# 3



# Enter Input : A 100,A 50,A 25,A 12,A 6,B,B,B,A 76,B,A 61,B,A 1,B,B,A 6,A 11,B
# 5
# 5
# 5
# 2
# 3
# 4
# 4
# 4
