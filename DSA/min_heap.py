# arr: The array representing the heap.
# n: The total number of elements in the heap.
# i: The index of the root of the subtree you want to "heapify."


def min_heap(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
        
    if smallest != i:
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        min_heap(arr, n, smallest)
        
        
def build_min_heap(arr):
    n = len(arr)
    
    for i in range(n//2-1, -1, -1 ):
        min_heap(arr,n,i)
        
arr = [4, 10, 3, 5, 1]
build_min_heap(arr)
print("Min Heap", arr)