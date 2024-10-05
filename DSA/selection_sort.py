def selection_sort(arr):
    for i in range(len(arr)):
        min_value = i
        for j in range(i,len(arr)):
            if arr[j] < min_value:
                min_value = j
                arr[i], arr[j] = arr[j], arr[i]
    print("Sort Completed\n\n", arr)
    return

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]

selection_sort(arr)