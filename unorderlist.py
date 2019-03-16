import array


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def insert(self, data):

        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def print(self):

        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

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

    def poll_first(self):



        self.last_node = self.head
        self.head = self.head.next
        return self.last_node.data

    def size_of_node(self):

        # it will return size of the node

        current = self.head
        size = 0
        while current:
            size = size+1
            current = current.next
        return size


if __name__ == '__main__':
    arr = []
    ll = LinkedList()
    fo = open("UnOrdered.txt", "r")
    arr = fo.read()
    words = arr.strip().split(' ')
    fo.close()
    print("File Output: ")
    # inserting_into_list
    for i in words:
        ll.insert(i)
    ll.print()
    print()
    print("enter element to search in linked list")
    element = input()
    var = ll.search(element)
    if var:
        print("element found and removed from list")
        ll.delete(element)
    else:
        print("element not found")
        print(element, " is added to list")
        ll.insert(element)
    ll.print()
    node_size = ll.size_of_node()
    array = []
    for i in range(node_size):
        array.append(ll.poll_first())
    print()
    print(array)
    fo = open("UnOrdered.txt", "w")
    for i in array:
        fo.write(i+" ")
    fo.close()
