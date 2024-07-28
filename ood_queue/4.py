
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
