def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    lefthalf = array[mid:]
    righthalf = array[:mid]
    
    sorted_left = merge_sort(lefthalf)
    sorted_right = merge_sort(righthalf)
   
   return merge(sorted_left,sorted_right)
    