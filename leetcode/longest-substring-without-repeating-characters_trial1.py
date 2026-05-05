from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        my_dict = defaultdict(int) # here we initiate an array with each count is aurtomatically 0
        max_len = 0
        for right in range(len(s)):
            my_dict[s[right]] += 1
            while left < len(s) and len(my_dict) != (right - left + 1):
                my_dict[s[left]] -=1
                if my_dict[s[left]] == 0:
                    del my_dict[s[left]]
                left +=1
            max_len = max(max_len, right - left + 1)
        return max_len
        