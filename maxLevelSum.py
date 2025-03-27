# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:    return 0
        max_sum = float('-inf')
        curr_q = [root]
        
        level = 1
        max_level = 1
        while curr_q:
            lvl_sum = 0
            next_q = []
            for x in curr_q:
                lvl_sum += x.val
                if x.left:  next_q.append(x.left)
                if x.right:  next_q.append(x.right)
            curr_q = next_q
            
            if max_sum < lvl_sum:
                max_level = level
                max_sum = lvl_sum
            level += 1
        return max_level





# Problem Link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
