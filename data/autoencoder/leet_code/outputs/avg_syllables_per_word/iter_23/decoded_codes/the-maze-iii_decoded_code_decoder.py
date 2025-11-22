import heapq

class Solution:
    def findShortestWay(self, maze, ball, hole):
        # directions: (dx, dy, direction_char)
        directions = [
            (0, 1, 'r'),
            (1, 0, 'd'),
            (0, -1, 'l'),
            (-1, 0, 'u')
        ]
        m = len(maze)
        n = len(maze[0]) if m > 0 else 0
        start = (ball[0], ball[1])
        hole = (hole[0], hole[1])

        # priority queue stores tuples: (distance, path string, (x, y))
        pq = [(0, "", start)]
        visited = set()

        while pq:
            dist, path, position = heapq.heappop(pq)
            x, y = position
            if position == hole:
                return path
            if position in visited:
                continue
            visited.add(position)

            for dx, dy, direction in directions:
                new_x, new_y = x, y
                count = 0
                while (0 <= new_x + dx < m and 0 <= new_y + dy < n and
                       maze[new_x + dx][new_y + dy] == 0):
                    new_x += dx
                    new_y += dy
                    count += 1
                    if (new_x, new_y) == hole:
                        break
                if (new_x, new_y) not in visited:
                    heapq.heappush(pq, (dist + count, path + direction, (new_x, new_y)))

        return "impossible"