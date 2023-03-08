class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            val = points[i]
            next_val = points[i + 1]
            time += max(abs(val[0]- next_val[0]), abs(val[1] - next_val[1]))
            
        return time
            