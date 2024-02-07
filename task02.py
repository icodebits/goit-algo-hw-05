def binary_search(arr, target):
    iterations = 0
    low = 0
    high = len(arr) - 1
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        iterations += 1

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
            if upper_bound is None or arr[mid] < upper_bound:
                upper_bound = arr[mid]
        else:
            return iterations, arr[mid]

    if upper_bound is None:
        upper_bound = arr[low] if low < len(arr) else None

    return iterations, upper_bound


if __name__ == "__main__":
    arr = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5]
    target = 1.0
    iterations, upper_bound = binary_search(arr, target)
    print("Кількість ітерацій:", iterations)
    print("Верхня межа:", upper_bound)
