class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = []
        my_dict = Counter(nums)
        for key, value in my_dict.items():
            new_nums.append(key)
        nums.clear()
        nums += new_nums
        for i in range(len(new_nums), n):
            nums.append("_")
        return len(new_nums)
        
        