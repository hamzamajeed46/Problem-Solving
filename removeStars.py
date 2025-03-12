class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if i != "*":
                st.append(i)
            else:
                st.pop()
        result = ""
        for s in st:
            result += s
        return result



"""
Problem Link:
https://leetcode.com/problems/removing-stars-from-a-string/
"""