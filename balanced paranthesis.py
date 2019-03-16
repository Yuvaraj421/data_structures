class Stack:
    def __init__(self):

        self.stack_Array = []

    def push(self, d):

        self.stack_Array.append(d)

    def pop(self):

        try:
            return self.stack_Array.pop()
        except Exception :
            print("")
    def is_Empty(self):
        return self.stack_Array==[]

    def size(self):

        return len(self.stack_Array)

    def print_Stack(self):

        for i in reversed(self.stack_Array):
            print(i)


if __name__ == '__main__':

    s = Stack()
    push_count = 0
    pop_count = 0
    expression = []
    expression = input("enter the arithmetic expression: ")
    for i in range(len(expression)):
        if expression[i] == '(':
            s.push(i)
            push_count += 1
            print(" ( is pushed at index ", i)
        elif expression[i] == ')':
            if s.is_Empty():
                s.pop()
                pop_count += 1
                print("cant pop stack is empty")
                break
            else:
                s.pop()
                pop_count += 1
                print(" )  pop at index ", i)
if push_count == pop_count:
    print("parenthesis is balanced")
else:
    print("parenthesis not balanced")


