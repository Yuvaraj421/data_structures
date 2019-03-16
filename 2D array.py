import numpy


def prime_Numbers(start):
    count = 0
    arr = []
    for i in range(0, start):
        count = 0
        if i != 0 and i != 1:
            for j in range(2, i):
                if i % j == 0:
                    count = count + 1
                    break
            if count == 0:
                arr.append(i)
    array = numpy.zeros((10, start))

    for i in range(0, 100):
        if arr[i] < 100:
            array[0][i] = arr[i]
    for i in array[0]:
        if i == 0 and i < 100:
            continue
        print(int(i), end=" ")
    print("\n")

    for i in range(0, len(arr)):
        if 100 < arr[i] < 200:
            array[1][i] = arr[i]
    for i in array[1]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")

    for i in range(0, len(arr)):
        if 200 < arr[i] < 300:
            array[2][i] = arr[i]
    for i in array[2]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")

    for i in range(0, len(arr)):
        if 300 < arr[i] < 400:
            array[3][i] = arr[i]
    for i in array[3]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")

    for i in range(0, len(arr)):
        if 400 < arr[i] < 500:
            array[4][i] = arr[i]
    for i in array[4]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")

    for i in range(0, len(arr)):
        if 500 < arr[i] < 600:
            array[5][i] = arr[i]
    for i in array[5]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")

    for i in range(0, len(arr)):
        if 600 < arr[i] < 700:
            array[6][i] = arr[i]
    for i in array[6]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")

    for i in range(0, len(arr)):
        if 700 < arr[i] < 800:
            array[7][i] = arr[i]
    for i in array[7]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")

    for i in range(0, len(arr)):
        if 800 < arr[i] < 900:
            array[8][i] = arr[i]
    for i in array[8]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")

    for i in range(0, len(arr)):
        if 900 < arr[i] < 1000:
            array[9][i] = arr[i]
    for i in array[9]:
        if i == 0:
            continue
        print(int(i), end=" ")
    print("\n")


if __name__ == '__main__':

    print()
    print("0 to 1000 prime numbers")
    print()

    start = int(input("Enter Range: "))
    if start == 1000:
        prime_Numbers(start)
    else:
        print("Range should be 1000")
