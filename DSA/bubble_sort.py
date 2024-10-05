class BubbleSort:
    def bubble(self,array):
        for i in range(len(array)):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        print("Sort completed\n",array)
        return
    
a = [4,5,2,5,2,7,8,4,1,3,6]

bubblesort = BubbleSort()
bubblesort.bubble(a)