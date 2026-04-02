nums = [5,8,3,2,6]
n = len(nums)
sumRight = [0] * n   # initialize with zeros
running_sum = 0
for i in range(n - 1, -1, -1):  # go from right to left
   sumRight[i] = running_sum
   running_sum += nums[i]
   print(running_sum)
print(sumRight)