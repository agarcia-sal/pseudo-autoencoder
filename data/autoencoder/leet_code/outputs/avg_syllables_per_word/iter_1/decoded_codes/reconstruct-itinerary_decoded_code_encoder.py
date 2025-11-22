from collections import defaultdict

def find_itinerary(tickets):
    graph = defaultdict(list)
    for frm, to in tickets:
        graph[frm].append(to)
    for frm in graph:
        graph[frm].sort(reverse=True)

    itinerary = []

    def visit(airport):
        while graph[airport]:
            visit(graph[airport].pop())
        itinerary.append(airport)

    visit("JFK")
    return itinerary[::-1]