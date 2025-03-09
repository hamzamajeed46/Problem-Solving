class Solution:
    def maxArea(self, height: List[int]) -> int:
        k = len(height) - 1
        i = 0
        max_area = 0
        while i < k:
            lower = min(height[i],height[k])
            diff = k - i
            area = lower * diff
            max_area = max(max_area,area)
            if height[i] < height[k]:
                i += 1
            else:
                k -= 1
        return max_area


"""
Problem link:
https://leetcode.com/problems/container-with-most-water
"""