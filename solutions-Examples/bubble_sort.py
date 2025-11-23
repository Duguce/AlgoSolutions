def bubble_sort(lst):
    n = len(lst)
    flag = False
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                flag = True
        if not flag:
            break
        flag = False


if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", sample_list)
    bubble_sort(sample_list)
    print("Sorted list:", sample_list)
