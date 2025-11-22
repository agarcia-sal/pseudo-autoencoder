from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for from_airport, to_airport in sorted(tickets, reverse=True):
            graph[from_airport].append(to_airport)

        itinerary = []

        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]