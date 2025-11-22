from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        # Sort tickets lex order ascending, then reverse for efficient pop from end
        for dep, arr in sorted(tickets)[::-1]:
            graph[dep].append(arr)

        itinerary = []

        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]