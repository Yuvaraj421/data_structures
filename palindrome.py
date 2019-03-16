class Deque:
    def __init__(self, capacity):

        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.deque = [] * capacity

    def insert_at_rear(self, lower_case1):

        if self.capacity == self.rear:
            print("Deque is full")
        else:

            for i in lower_case1:
                self.deque.append(i)
                self.rear += 1

    def display(self):

        if self.front == self.rear:
            print("empty deque")
        else:
            for i in range(self.rear):
                print(self.deque[i], end=" ")
                self.rear -= 1

    def remove_from_front(self):

        if self.front == self.rear:
            print("empty deque")
        else:
            # print("deque from front ", self.deque[self.front])
            self.front += 1
            return self.deque[self.front - 1]

    def remove_from_rear(self):

        if self.rear == self.front:
            print("empty deque")
        else:
            # print("deque from rear ", self.deque[self.rear-1])
            self.rear -= 1
            return self.deque[self.rear]


if __name__ == '__main__':
    element = input("enter a string to check palindrome or not: ")
    lower_case = element.lower()
    d = Deque(len(lower_case))
    d.insert_at_rear(lower_case)
    for i in range(len(lower_case) // 2):
        if d.remove_from_front() == d.remove_from_rear():
            if i == (len(lower_case) // 2) - 1:
                print("palindrome")
        else:
            print("not palindrome")
            break
