from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        int_set = set()
        ans = []
        for a, b in edges:
            d[b].append(a)
            int_set.add(a)
            int_set.add(b)
        
        for i in int_set:
            if i not in d.keys():
                ans.append(i)
        
        return ans