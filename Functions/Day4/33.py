def has_33(nums):
    for i in range(0,len(nums)-1):
       if nums[i]==3 and nums[i+1]==3:
           return True
    return False
    
print(has_33([3,6,3]))