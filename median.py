nums = lst(input("enter a number:")
nums.sort()
length = len(nums)
if (length % 2 == 0):
    median = (nums[(length)//2] + nums[(length)//2-1]) / 2
else:
    median = nums[(length-1)//2]
 

print(median)
