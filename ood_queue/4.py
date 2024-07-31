
class Queue:
    def __init__(self, list=None):
        if list is None:
            self.items = []
        else:
            self.items = list

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def coffe_order(self, q):
        q1 = []
        timeq1 = 0
        timeq2 = 0
        q2 = []
        total = []
        waiting_times = []

        for idx, each in enumerate(q):
            num1, num2 = each.split(',')
            int1 = int(num1)
            int2 = int(num2)
            if timeq1 <= timeq2:
                if timeq1 >= int1:
                    q1.append(each)
                    waiting_times.append([idx + 1, timeq1 - int1])
                    timeq1 += int2
                    total.append([idx + 1, timeq1])
                else:
                    timeq1 = int1 + int2
                    total.append([idx + 1, timeq1])
                    waiting_times.append([idx + 1, 0])
            else:
                if timeq2 >= int1:
                    q2.append(each)
                    waiting_times.append([idx + 1, timeq2 - int1])
                    timeq2 += int2
                    total.append([idx + 1, timeq2])
                else:
                    timeq2 = int1 + int2
                    total.append([idx + 1, timeq2])
                    waiting_times.append([idx + 1, 0])

        total.sort(key=lambda x: x[1])  # Sort based on the end time

        for t in total:
            print(f"Time {t[1]} customer {t[0]} get coffee")

        max_waiting_time = max(waiting_times, key=lambda x: x[1])

        if max_waiting_time[1] == 0:
            print("No waiting")
        else:
            print(f"The customer who waited the longest is : {max_waiting_time[0]}")
            print(f"The customer waited for {max_waiting_time[1]} minutes")

print(' ***Cafe***')
q1 = [e for e in input('Log : ').split('/')]
q = Queue()
q.coffe_order(q1)
#################
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
4
4


