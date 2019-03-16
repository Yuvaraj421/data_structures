from array import array


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.pre_node = None

    def enqueue(self, data):

        if self.pre_node is None:
            self.head = Node(data)
            self.pre_node = self.head
        else:
            self.pre_node.next = Node(data)
            self.pre_node = self.pre_node.next

    def deque(self):

        if self.head is None:
            return None
        else:
            deque_value = self.head.data
            self.head = self.head.next
            return deque_value


def prime_Anagram(str1):

    anagram = []
    arr = array('i', [])
    for i in range(0, str1):
        count = 0
        if i != 0 and i != 1:
            for j in range(2, i):
                if i % j == 0:
                    count = count + 1
                    break
            if count == 0:
                arr.append(i)

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if len(str(arr[i])) == len(str(arr[j])):
                var1 = ''.join(sorted(str(arr[i])))
                var2 = ''.join(sorted(str(arr[j])))
                if var1 == var2:
                    anagram.append(arr[i])
                    anagram.append(arr[j])

    print("anagram numbers range between 0 and given number is: ")
    q = Queue()
    for i in anagram:
        q.enqueue(i)

    for i in range(0, len(anagram)):
        print(q.deque(), end=" ")




if __name__ == '__main__':

    start = int(input("Enter Range: "))

    prime_Anagram(start)
