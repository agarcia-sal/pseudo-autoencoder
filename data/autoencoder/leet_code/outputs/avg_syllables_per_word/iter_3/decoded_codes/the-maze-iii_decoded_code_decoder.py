import heapq

class Solution:
    def findShortestWay(self, maze, ball, hole):
        directions = [(0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l'), (-1, 0, 'u')]
        m, n = len(maze), len(maze[0])
        start = tuple(ball)
        hole = tuple(hole)
        pq = [(0, "", start)]
        visited = {}

        while pq:
            dist, path, (x, y) = heapq.heappop(pq)
            if (x, y) == hole:
                return path
            if (x, y) in visited and (visited[(x, y)][0] < dist or (visited[(x, y)][0] == dist and visited[(x, y)][1] <= path)):
                continue
            visited[(x, y)] = (dist, path)
            for dx, dy, direction in directions:
                new_x, new_y, count = x, y, 0
                while 0 <= new_x + dx < m and 0 <= new_y + dy < n and maze[new_x + dx][new_y + dy] == 0:
                    new_x += dx
                    new_y += dy
                    count += 1
                    if (new_x, new_y) == hole:
                        break
                if (new_x, new_y) not in visited or dist + count < visited[(new_x, new_y)][0] or (dist + count == visited[(new_x, new_y)][0] and path + direction < visited[(new_x, new_y)][1]):
                    heapq.heappush(pq, (dist + count, path + direction, (new_x, new_y)))

        return "impossible"