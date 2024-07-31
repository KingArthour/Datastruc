
class Queue :
    def __init__(self, start, end, width, height) :
        
        if start == None : 
            print("Invalid map input.")
            self.queue = []
        else : self.queue = [start]
        self.end = end
        self.width = width
        self.height = height
        self.record_part = []

    def enQ(self, i) :
        self.queue.append(i)

    def deQ(self, room) :
        print(f"Queue: {self.queue}")
        position = self.queue.pop(0)
        state = self.search_portal(position, room)
        if state == "end" : 
            print("Found the exit portal.")
            q.queue = []
        elif self.isEmpty() : print("Cannot reach the exit portal.")

    def isEmpty(self) :
        return len(self.queue) == 0

    def search_portal(self, current_position, room) :
        if current_position[1] - 1 >= 0 and (current_position[0], current_position[1] - 1) not in self.record_part :
            if room[current_position[1] - 1][current_position[0]] == '_' :
                self.enQ((current_position[0], current_position[1] - 1))
                self.record_part.append((current_position[0], current_position[1] - 1))
            elif room[current_position[1] - 1][current_position[0]] == 'O' :
                return "end"
        if current_position[0] + 1 <= width - 1 and (current_position[0] + 1, current_position[1]) not in self.record_part :
            if room[current_position[1]][current_position[0] + 1] == '_' :
                self.enQ((current_position[0] + 1, current_position[1]))
                self.record_part.append((current_position[0] + 1, current_position[1]))
            elif room[current_position[1]][current_position[0] + 1] == 'O' :
                return "end"
        if current_position[1] + 1 <= hight - 1 and (current_position[0], current_position[1] + 1) not in self.record_part :
            if room[current_position[1] + 1][current_position[0]] == '_' :
                self.enQ((current_position[0], current_position[1] + 1))
                self.record_part.append((current_position[0], current_position[1] + 1))
            elif room[current_position[1] + 1][current_position[0]] == 'O' :
                return "end"
        if current_position[0] - 1 >= 0 and (current_position[0] - 1, current_position[1]) not in self.record_part :
            if room[current_position[1]][current_position[0] - 1] == '_' :
                self.enQ((current_position[0] - 1, current_position[1]))
                self.record_part.append((current_position[0] - 1, current_position[1]))
            elif room[current_position[1]][current_position[0] - 1] == 'O' :
                return "end"
    
room = input("Enter width, height, and room: ").split(" ")
width = int(room[0])
hight = int(room[1])
room = room[2].split(",")
check = True

if len(room) != hight : 
    print("Invalid map input.")
    check=False
for i in room :
    if len(i) != width : 
        print("Invalid map input.")
        check=False
        break
if check  :
    def search(room) :
        position = {'start': None, 'end': None}
        for a in range(width) :
            for b in range(hight) :
                if room[b][a] == 'F' :
                    position["start"] = (a, b)
                elif room[b][a] == 'O' :
                    position["end"] = (a, b)
        return position

    position_set = search(room)

    q = Queue(position_set["start"], position_set["end"], width, hight)

    while not q.isEmpty() :
        q.deQ(room)



######################
# พี่ซันฟงได้รับคำสั่งจากอาจารย์ให้ออกโจทย์เขียนโปรแกรมให้แก่น้องๆ พี่จึงกลับไปนอนคิดที่บ้าน รู้สึกตัวอีกทีก็อยู่ในห้องมืดๆ พี่สามารถมองเห็นและเดินไปยังพื้นที่ที่อยู่ติดกันได้ (4 ทิศ เหนือ ใต้ ออก ตก) พี่จะต้องหาประตูทางออกจากฝันเพื่อไปส่งโจทย์ให้กับอาจารย์ ต่อมาพี่ก็คิดวิธีในการเดินหาประตูทางออกได้โดยใช้วิธีหาแบบ Breadth First Search โดยพี่จะเริ่มยืนในจุดเริ่มต้นแล้วมองหาและจำทางเริ่มจากทิศเหนือ ทิศตะวันออก ทิศใต้ ทิศตะวันตก ตามลำดับ แล้วเดินไปยังช่องถัดไปแล้วหาใหม่ ในเมื่อคิดวิธีออกแล้วพี่จึงต้องการโปรแกรมที่จะบอกพี่ว่าสามารถไปถึงทางออกได้หรือพี่จะต้องติดอยู่ในฝันไปตลอดกาล ปัญหาคือพี่ขี้เกียจเขียนโค้ด พี่เลยอยากให้น้องๆเขียนโค้ดให้พี่หน่อย เขียนสวยๆกะทัดรัด ไม่งั้นจะส่งกลับไปเขียนใหม่
# โดยรายละเอียดโปรแกรมจะมีดังนี้
# Input
# รับความกว้าง ความสูง และแผนที่ โดยแผนที่แต่ละบรรทัดจะขั้นด้วย ','
# ตัวอย่าง input: 3 3 F__,##_,O__
# จะมีความหมายว่าแผนที่กว้าง 3 สูง 3 และแผนที่จะเป็นแบบนี้
# F__
# ##_
# O__
# ภายในแผนที่
# 'F' แทนตำแหน่งเริ่มต้นของพี่
# 'O' แทนประตูทางออก
# '_' แทนพื้นที่ที่สามารถเดินได้
# ตัวอักษรอื่นๆทั้งหมดแทนกำแพง ไม่สามารถเดินไปที่ช่องนั้นได้
# Output
# หากไม่มีพี่ (F) อยู่ในห้องหรือแผนที่ที่ใส่เข้ามาไม่ตรงกับขนาดของ width ให้แสดงว่า "Invalid map input."
# แสดง queue ระหว่างหาทางออก
# ถ้าหาทางออกเจอให้แสดงว่า "Found the exit portal."
# ถ้าหาไม่เจอให้แสดงว่า "Cannot reach the exit portal."



# Enter width, height, and room: 6 4 F__###,##_###,##__##,###__O
# Queue: [(0, 0)]
# Queue: [(1, 0)]
# Queue: [(2, 0)]
# Queue: [(2, 1)]
# Queue: [(2, 2)]
# Queue: [(3, 2)]
# Queue: [(3, 3)]
# Queue: [(4, 3)]
# Found the exit portal.



# Enter width, height, and room: 8 6 ########,##___###,##_F_###,##____##,##_##_O_,##______
# Queue: [(3, 2)]
# Queue: [(3, 1), (4, 2), (3, 3), (2, 2)]
# Queue: [(4, 2), (3, 3), (2, 2), (4, 1), (2, 1)]
# Queue: [(3, 3), (2, 2), (4, 1), (2, 1), (4, 3)]
# Queue: [(2, 2), (4, 1), (2, 1), (4, 3), (2, 3)]
# Queue: [(4, 1), (2, 1), (4, 3), (2, 3)]
# Queue: [(2, 1), (4, 3), (2, 3)]
# Queue: [(4, 3), (2, 3)]
# Queue: [(2, 3), (5, 3)]
# Queue: [(5, 3), (2, 4)]
# Queue: [(2, 4), (5, 4)]
# Queue: [(5, 4), (2, 5)]
# Found the exit portal.


# Enter width, height, and room: 3 3 ###,######F,###
# Invalid map input.



# Enter width, height, and room: 3 3 F__,##_,O_
# Invalid map input.


# Enter width, height, and room: 1 1 F
# Queue: [(0, 0)]
# Cannot reach the exit portal.


# Enter width, height, and room: 5 3 __|__,F_|_O,__|__
# Queue: [(0, 1)]
# Queue: [(0, 0), (1, 1), (0, 2)]
# Queue: [(1, 1), (0, 2), (1, 0)]
# Queue: [(0, 2), (1, 0), (1, 2)]
# Queue: [(1, 0), (1, 2)]
# Queue: [(1, 2)]
# Cannot reach the exit portal.
