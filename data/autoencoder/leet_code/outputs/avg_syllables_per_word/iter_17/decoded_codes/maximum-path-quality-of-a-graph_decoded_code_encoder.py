from collections import defaultdict
from typing import List, Tuple, Set, Dict

def initializeDefaultList() -> Dict[int, List[Tuple[int, int]]]:
    return defaultdict(list)

def initializeGraph(list_of_edges: List[Tuple[int, int, int]]) -> Dict[int, List[Tuple[int, int]]]:
    graph_structure = initializeDefaultList()
    for start_node, end_node, travel_time in list_of_edges:
        graph_structure[start_node].append((end_node, travel_time))
        graph_structure[end_node].append((start_node, travel_time))
    return graph_structure

def initializeEmptySet() -> Set[int]:
    return set()

def addElement(set_structure: Set[int], element: int) -> None:
    set_structure.add(element)

def removeElement(set_structure: Set[int], element: int) -> None:
    set_structure.remove(element)

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[Tuple[int, int, int]], maxTime: int) -> int:
        graph = initializeGraph(edges)

        visited_nodes = initializeEmptySet()
        maximum_quality = 0

        def dfs(node: int, remaining_time: int, current_quality: int) -> None:
            nonlocal maximum_quality

            if node == 0:
                if current_quality > maximum_quality:
                    maximum_quality = current_quality

            for neighbor, travel_time in graph[node]:
                if travel_time <= remaining_time:
                    if neighbor not in visited_nodes:
                        addElement(visited_nodes, neighbor)
                        dfs(neighbor, remaining_time - travel_time, current_quality + values[neighbor])
                        removeElement(visited_nodes, neighbor)
                    else:
                        dfs(neighbor, remaining_time - travel_time, current_quality)

        addElement(visited_nodes, 0)
        dfs(0, maxTime, values[0])

        return maximum_quality