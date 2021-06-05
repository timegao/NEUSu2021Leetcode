import heapq


def minAvailableDuration(slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
    # filter for meetings lasting greater than or equal to duration
    # sort by starting time (ending time not needed because no intersection)
    slots1 = sorted(filter(lambda x: x[1] - x[0] >= duration,
                    slots1), key=lambda x: (x[0]))
    slots2 = sorted(filter(lambda y: y[1] - y[0] >= duration,
                    slots2), key=lambda y: (y[0]))
    i, j = 0, 0
    # end of one list means you've checked all intersection
    while i < len(slots1) and j < len(slots2):
        x0, x1 = slots1[i]  # destructure the pair in each list
        y0, y1 = slots2[j]
        if x1 - duration < y0:  # slots1[i] starts too late
            i += 1
        elif y1 - duration < x0:  # slots2[j] starts too late
            j += 1
        else:  # intersection found, walrus operator to initialize start inline
            return [start := max(x0, y0), start + duration]
    return []

# alternative solution using python heap
# takes advantage of the fact that that each of lists do not intersect with itself to join the lists

# def minAvailableDuration(slots1: list[list[int]], slots2: list[list[int]], duration: int) -> list[int]:
#     all_slots = slots1 + slots2
#     pq = list(filter(lambda s: s[1] - s[0] >= duration, all_slots))
#     heapq.heapify(pq)  # sorts by start time followed by end time in min heap
#     # it is guaranteed that no two availability slots of the same person intersect with each other
#     while pq:
#         top = heapq.heappop(pq)
#         # one's end >= another's start + duration
#         if top[1] >= (start := pq[0][0]) + duration:
#             return [start, start + duration]
#     return []


print(minAvailableDuration(
    [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8))
