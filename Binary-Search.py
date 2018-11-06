def IteratoryBinarySearch(arr, x):
    low = 0
    high = len(arr)-1

    while(low <= high):
        mid = (low+high)//2
        if x == arr[mid]:
            return True
        elif x > arr[mid]:
            low = mid+1
        elif x < arr[mid]:
            high = mid-1


arr = [1, 2, 3, 4, 5, 6, 7, 8]
x = 9
print IteratoryBinarySearch(arr, x)

# def Binarysearch(arr, l, r, x):
#     if r >= l:
#         mid = l + (r-1)/2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             Binarysearch(arr, l, mid-1, x)
#         else:
#             Binarysearch(arr, mid+1, r, x)
#     else:
#         return -1
#
#
# arr = [10, 20, 30, 40, 50, 55, 60, 62, 76, 89]
# print Binarysearch(arr, 0, len(arr)-1, 55)
