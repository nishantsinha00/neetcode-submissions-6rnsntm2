import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[(0-point[0]) ** 2 + (0 - point[1]) ** 2, [point[0], point[1]]] for point in points]
        ksmallest = heapq.nsmallest(k, heap)
        ksmallest[:] = [point[1] for point in ksmallest]
        return ksmallest