from array import array


def prime_Anagram(str1):
    anagram = []
    non_Anagram = []
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

    flag = True
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if len(str(arr[i])) == len(str(arr[j])):
                var1 = ''.join(sorted(str(arr[i])))
                var2 = ''.join(sorted(str(arr[j])))
                if var1 == var2:
                    anagram.append(arr[i])
                    anagram.append(arr[j])
                    flag = False
        if flag:
            non_Anagram.append(arr[i])
        else:
            flag = True

    print("list of anagram-prime number")

    for j in range(0, len(anagram)):

        print(anagram[j], end=" ")

    print("\n")
    print("list of non-anagram prime number")
    for k in range(0, len(non_Anagram)):

        print(non_Anagram[k], end=" ")



if __name__ == '__main__':
    start = int(input("Enter Range: "))
    prime_Anagram(start)
