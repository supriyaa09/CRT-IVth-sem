'''def Array_sum(nums):
    s=0
    for i in range(len(nums)):
        s+=nums[i]
    return s
print(Array_sum([1,2,3,4,5])) #15

def Array_sum_recursion(nums):
    s=0
    for i in range(len(nums)-1,-1,-1):
        s+=nums[i]
    return s
print(Array_sum_recursion([1,2,3,4,5])) #15'''
#Recurssive approach
'''def Array_sum1(nums,index):
    if index==-1:
        return 0
    return nums[index]+Array_sum1(nums,index-1)
print(Array_sum1([1,2,3,4,5],4)) 
'''
'''#Recursive approach-2
def Array_sum2(nums):
    if len(nums)==0:
        return 0
    return nums[-1]+Array_sum2(nums[:-1])
print(Array_sum2([1,2,3,4,5]))
'''

