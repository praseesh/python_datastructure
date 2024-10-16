def heightChecker(heights):
    expected = sorted(heights)
    count = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            count += 1
    return count
heights = [1,1,4,2,1,3]
print(heightChecker(heights))