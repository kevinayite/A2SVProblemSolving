class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        answer = 0
        left = 0
        right = len(piles) - 1
        while left < right:
            right -= 1
            answer += piles[right]
            right -= 1
            left +=1
        return answer