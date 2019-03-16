class Node:
    try:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    except Exception as e:
        print(e)
