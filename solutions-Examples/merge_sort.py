def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst[:]

    mid = n // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    i = j = 0
    out = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1

    out.extend(left[i:])
    out.extend(right[j:])

    return out


if __name__ == "__main__":
    sample_list = [3, 6, 8, 10, 1, 2, 1]
    print("Original list:", sample_list)
    sorted_list = merge_sort(sample_list)
    print("Sorted list:", sorted_list)