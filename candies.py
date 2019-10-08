#Leet code: 575. Distribute Candies: https://leetcode.com/problems/distribute-candies/

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """

        return min(len(set(candies)), (len(candies) / 2))
