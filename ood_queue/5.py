
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