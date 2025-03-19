class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        if len(word2) != len(word1):
            return False
        for i in range(len(word1)):
            if word1[i] not in dict1: dict1[word1[i]] = 1
            else: dict1[word1[i]] += 1
            if word2[i] not in dict2: dict2[word2[i]] = 1
            else: dict2[word2[i]] += 1
        if dict1.keys() != dict2.keys(): return False
        list1 = sorted(list(dict1.values()))
        list2 = sorted(list(dict2.values()))
        return list1 == list2

"""
Problem Link:
https://leetcode.com/problems/determine-if-two-strings-are-close/

"""