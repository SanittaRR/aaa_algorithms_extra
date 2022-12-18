import heapq


def merge_k_sorted(arrs: list) -> list:
    total = []
    heap = []

    for i in range(len(arrs)):
        heapq.heappush(heap, (arrs[i][0], i, 0))

    while heap:
        val, rows, columns = heapq.heappop(heap)
        total.append(val)
        if columns + 1 < len(arrs[rows]):
            heapq.heappush(heap, (arrs[rows][columns + 1], rows, columns + 1))
    return total
