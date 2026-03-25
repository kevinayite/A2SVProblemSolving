nums = [5,8,3,2,6]
prefix_sum = [0]*(len(nums) + 1)

accumulator = 0 
for i in range(len(nums)):
   prefix_sum[i] = accumulator
   accumulator += nums[i]
prefix_sum[-1] = accumulator
print(prefix_sum)