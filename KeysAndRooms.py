class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [False]*len(rooms)
        queue = [0]
        while queue:
            k = queue.pop(0)
            if keys[k] == False:
                for key in rooms[k]:
                    queue.append(key)
                keys[k] = True
        return (all(keys)==True)


"""
Problem Link: https://leetcode.com/problems/keys-and-rooms/
"""








        