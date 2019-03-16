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

    def search(self,element):

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
            print(n.data, end=" ")
            n = n.next

    def returnvalue(self):

        values = []
        n = self.head
        while n is not None:
            values.append(n.data)
            n = n.next
        return values

    def size_of_node(self):

        current = self.head
        size = 0
        while current:
            size = size + 1
            current = current.next
        return size

    def poll_first(self):

        self.last_node = self.head
        self.head = self.head.next
        return self.last_node.data


if __name__ == '__main__':
    arr = []
    ll = []
    l1 = LinkedList()
    for i in range(11):
        l1 = LinkedList()
        ll.append(l1)
    fo = open("Hashing.txt", "r")
    arr = fo.read()
    words = arr.strip().split(' ')
    fo.close()
    print("File Output: ")
    print(words)
    for i in range(len(words)):
        ll[int(words[i]) % 11].insert_with_sorting(int(words[i]))
    for i in range(len(ll)):
        print(ll[i].display1())

    print("enter element to search in linked list")
    element = int(input())
    element_hash = element % 11
    var = ll[element_hash].search(element)
    print(var)
    if var:
        print("element found and removed from list")
        ll[element_hash].delete(element)
    else:
        print("element not found")
        print(element, " is added to list")
        ll[element_hash].insert_with_sorting(element)

    for i in range(len(ll)):
        print(ll[i].display1())
    file = open("Hashing.txt", 'w')
    file.write("")
    file.close()
    file1 = open("Hashing.txt", 'a')
    for i in range(11):
        if ll[i] == None:
            continue
        size = ll[i].size_of_node()
        for j in range(size):
            file1.write(str(ll[i].poll_first())+"   ")


