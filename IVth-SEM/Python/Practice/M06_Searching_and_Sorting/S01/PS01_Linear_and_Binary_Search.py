def Linear_Search(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1  
print(Linear_Search([13,15,45,67,89,20],15))
print(Linear_Search([13,15,45,67,89,20],100))

def Binary_Search(nums):
    pass
