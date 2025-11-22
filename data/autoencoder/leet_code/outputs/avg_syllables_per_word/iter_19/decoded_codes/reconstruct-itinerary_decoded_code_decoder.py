from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        # Build graph with destinations sorted in reverse lexical order
        for departure_airport, arrival_airport in sorted(tickets, reverse=True):
            graph[departure_airport].append(arrival_airport)

        itinerary = []

        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit('JFK')
        return itinerary[::-1]