# Program for BubbleSort


def BubbleSortAlgo(arr):

    for j in range(0, len(arr)-1):
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp


def SelectionSortAlgo(arr):

    for j in range(0, len(arr)-1):

        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
            else:
                temp = arr[i+1]
        print temp


arr2 = []
arr = [2, 6, 1, 3, 7, 9, 4]
#print len(arr)
# BubbleSortAlgo(arr)
SelectionSortAlgo(arr)
print arr2
