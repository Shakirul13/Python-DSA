nums1 = [1,4,3,2]
nums2 = [6,2,6,5,1,2]
def partition(arr):
    arr.sort()
    total = 0
    for i in range(0, len(arr), 2):
        total += arr[i]
    return total
print(partition(nums1))
print(partition(nums2))