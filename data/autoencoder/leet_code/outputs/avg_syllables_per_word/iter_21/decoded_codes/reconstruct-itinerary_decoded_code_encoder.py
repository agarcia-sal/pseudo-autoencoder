from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        # Sort tickets ascending, then reverse for efficient pop from the end
        for dep, dest in sorted(tickets)[::-1]:
            graph[dep].append(dest)

        itinerary = []
        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]