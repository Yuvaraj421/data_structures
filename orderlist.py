class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):

        self.head = None
        self.pre_node = None

    def insert_with_sorting(self, data):

        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        elif self.head.data > newNode.data:
            newNode.next = self.head
            self.head = newNode
        else:
            n = self.head
            while n is not None:
                if n.data > newNode.data:
                    newNode.next = n
                    self.pre_node.next = newNode
                    break
                self.pre_node = n
                n = n.next
            self.pre_node.next = newNode

    def search(self, element):

        current = self.head
        while current != None:
            if current.data == element:
                return True
            current = current.next
        return False

    def delete(self, element):

        current = self.head
        while current != None:
            if self.head.data == element:
                self.head = self.head.next
                break
            if current.data == element:
                self.last_node.next = current.next
                break
            self.last_node = current
            current = current.next

    def display1(self):

        n = self.head
        while n is not None:
            print(n.data,end=" ")
            n = n.next

    def dis2(self):

        n = self.head
        while n is not None:
            return n.data
            # print(n.data,end=" ")
            n = n.next

    def poll_first(self):

        self.last_node = self.head
        self.head = self.head.next
        return self.last_node.data

    def size_of_node(self):

        current = self.head
        size = 0
        while current:
            size = size + 1
            current = current.next
        return size


if __name__ == '__main__':
    arr = []
    l1 = LinkedList()
    fo = open("Ordered.txt", "r")
    arr = fo.read()
    words = arr.strip().split(' ')
    fo.close()
    print("File Output: ")
    print(words)
    for i in words:
        l1.insert_with_sorting(int(i))
    print("sorted array is:")
    l1.display1()
    print()
    print("enter element to search in linked list")
    element = int(input())
    var = l1.search(element)
    if var:
        print("element found and removed from list")
        l1.delete(element)
    else:
        print("element not found")
        print(element, " is added to list")
        l1.insert_with_sorting(element)
    l1.display1()

    node_size = l1.size_of_node()
    array = []
    for i in range(node_size):
        array.append(l1.poll_first())
    print()
    print(array)
    fo = open("Ordered.txt", "w")
    for i in array:
        fo.write(str(i) + " ")
    fo.close()

