
class Queue:

    def __init__(self):
        self.list1 = []

    def is_empty(self):
        return self.list1 == []

    def enqueue(self, list1):
        self.list1.insert(0, list1)

    def de_queue(self):
        return self.list1.pop()

    def size(self):
        return len(self.list1)


def cash_counter():

    queue = Queue()  # creating queue object

    bank_cash = 1000

    try:

        no_of_people = int(input('Enter Number of People in the Queue:\n'))

    except ValueError:

        print("enter data in number")

    for i in range(0, no_of_people):
        queue.enqueue(i)
    try:
        for i in range(0, queue.size()):

            print("1. Deposit the amount\n2. Withdraw cash\n")

            choose = int(input("Enter the your choice\n"))

            if choose == 1:
                deposit_amount = float(input("Enter the amount to deposit \n"))

                bank_cash = bank_cash + deposit_amount

                queue.de_queue()

            if choose == 2:

                withdraw_cash = int(input("Enter the amount to withdraw\n"))

                if withdraw_cash <= bank_cash:
                    bank_cash = bank_cash - withdraw_cash

                    print("Total cash in bank counter = ", bank_cash)
                    queue.de_queue()
                    continue

                if withdraw_cash > bank_cash:

                    print("Insufficient bank balance \n")

                    print("1. Reenter the amount\n2. cancel the transaction\n")

                    choice = int(input("Enter your choice\n"))

                    if choice == 1:

                        if withdraw_cash <= bank_cash:
                            withdraw_cash = float(input("Enter the amount to withdraw\n"))

                            bank_cash = bank_cash - withdraw_cash

                            print("Withdraw cash = ", withdraw_cash, "\n")

                            queue.de_queue()

                    if choice == 2:

                        print("Your transaction is cancelled\n")

                        print("Thank you\n")

                        queue.de_queue()

            if i < queue.size():
                print("Next person \n")

            print("Total cash in bank counter = ", bank_cash)

    except ValueError:
        print("enter valid data")


if __name__ == '__main__':
    cash_counter()



