class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            
            graph[a].append((b, prob))
            graph[b].append((a, prob))
            
        max_prob = [0.0] * n
        max_prob[start] = 1.0
            
#         def dijkstra(start):
#             q = []
#             heapq.heappush(q, (1, start))
#             p[start] = 1
            
#             while q:
#                 prop, now = heapq.heappop(q)
#                 if p[now] > prop:
#                     continue
#                 for i in graph[now]:
#                     cost = prop * i[1]
#                     if cost > p[i[0]]:
#                         p[i[0]] = cost
#                         heapq.heappush(q, (cost, i[0]))
        
#         dijkstra(start)

        pq = [(-1.0, start)]
        
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                return -cur_prob
            for nxt_node, path_prob in graph[cur_node]:
                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
        
        return 0.0