def Binary_Search(nums,target):
    low,high=0,len(nums)-1
    while low < high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

li=list(map(int,input("Enter the elements of the list separated by space: ").split()))
target=int(input("Enter the target element: "))
print(Binary_Search(li,target))