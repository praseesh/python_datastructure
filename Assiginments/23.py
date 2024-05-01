class TwoDArray:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.array = [[0 for _ in range(cols)] for _ in range(rows)]

    def getArray(self):
        print("Enter the array values:")
        for i in range(self.rows):
            self.array[i] = list(map(int, input().split()))

    def displayArray(self):
        print("Array elements are:")
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.array[i][j], end="\t")
            print()

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    array = TwoDArray(rows, cols)
    array.getArray()
    array.displayArray()

if __name__ == "__main__":
    main()
