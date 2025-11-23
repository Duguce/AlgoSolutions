def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]


if __name__ == "__main__":
    sample_list = [64, 25, 12, 22, 11]
    print("Original list:", sample_list)
    selection_sort(sample_list)
    print("Sorted list:", sample_list)
