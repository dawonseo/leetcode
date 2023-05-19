from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d = {}
        queue = deque([])
        for idx in range(len(graph)):
            queue.append(idx)
            if idx not in d.keys():
                d[idx] = True
        
            while queue:
                c = queue.popleft()

                for i in graph[c]:
                    if i in d.keys():
                        if d[c] == d[i]:
                            return False
                    else:
                        d[i] = not d[c]
                        queue.append(i)
        
        return True
        
            