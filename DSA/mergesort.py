def merge_sort(array):
   if len(array) <= 1:
       return array
   mid = len(array) // 2
   lefthalf = array[mid:]
   righthalf = array[:mid]
   
   sorted_left = merge_sort(lefthalf)
   sorted_right = merge_sort(righthalf)
   
   return merge(sorted_left,sorted_right)
    
def merge(left,right):
   result = []
   i = 0
   j = 0
   while i < len(left) and j < len(right):
      if left[i] < right[j]:
         result.append(left[i])
         i += 1
      else:
         result.append(right[j])
         j += 1
   result.extend(left[i:])
   result.extend(right[j:])
      
   return result


unsortedArr = [5,4,3,2,1,4]
sorted_array = merge_sort(unsortedArr)
print("Sorted Array: ",sorted_array)
         
          
      