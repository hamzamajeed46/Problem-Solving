class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n==1: return 1
        candies = [1] * n
        if ratings[0] > ratings[1]: candies[0] = 2
        for i in range(1,n-1):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
            elif ratings[i] > ratings[i+1]:
                candies[i] += 1
        if ratings[-1] > ratings[-2]: candies[-1] = candies[-2] + 1
        for i in range(n-1,0,-1):
            if ratings[i] < ratings[i-1] and candies[i] >= candies[i-1]:
                candies[i-1] = candies[i] + 1
        return sum(candies)
        
"""
Problem Link: https://leetcode.com/problems/candy/
"""