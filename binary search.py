def factor(num):
    res = 1
    for i in range(1, num + 1):
        res = res * i
    return res


if __name__ == "__main__":
    tree_values = []
    tree_count = []
    num = int(input("enter number : "))
    for i in range(1, num + 1):
        print("enter ", i, "value ")
        tree_values.append(int(input()))
    print("Trees :", tree_values)
    for i in tree_values:
        countBST1 = factor(2 * i)
        countBST2 = factor(i + 1) * factor(i)
        tree_count.append(countBST1 // countBST2)
    print("binary tree count: ", tree_count)
