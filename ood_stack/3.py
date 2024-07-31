
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

    def color_crush(self):
        temp_stack = []
        count = 0

        while self.items:
            current = self.pop()
            if len(temp_stack) >= 2 and temp_stack[-1] == temp_stack[-2] == current:
                temp_stack.pop()
                temp_stack.pop()
                count += 1
            else:
                temp_stack.append(current)

        # Restore items back to self.items in correct order
        while temp_stack:
            self.push(temp_stack.pop())

        # if count >= 2:
        #     self.items.reverse()

        if len(self.items) == 0:
            str_line2 = 'Empty'
        else:
            str_line2 = "".join(self.items[::-1])  # Reverse the order here

        return f'{len(self.items)}\n{str_line2}\n{"Combo : " + str(count) + " ! ! !" if count >= 2 else ""}'


ls = [e for e in input("Enter Input : ").split()]

s = Stack(ls)  

print(s.color_crush())



###########
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

