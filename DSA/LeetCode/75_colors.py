def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) -1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    print(nums)

arr = [2, 0, 1, 2, 0, 1, 2, 1, 0]
sort_colors(arr)