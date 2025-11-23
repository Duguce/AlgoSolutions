def quick_sort(lst):
    def partition(lst, left, right):
        pivot = lst[right]
        i = left - 1
        for j in range(left, right):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i+1], lst[right] = lst[right], lst[i+1]

        return i + 1

    def _qs(lst, left, right):
        if left >= right:
            return

        p = partition(lst, left, right)
        _qs(lst, left, p - 1)
        _qs(lst, p+1, right)

    _qs(lst, 0, len(lst)-1)


if __name__ == "__main__":
    sample_list = [3, 6, 8, 10, 1, 2, 1]
    print("Original list:", sample_list)
    quick_sort(sample_list)
    print("Sorted list:", sample_list)
