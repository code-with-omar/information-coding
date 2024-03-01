import heapq
from collections import Counter


def calculate_frequency(my_text):
    my_text = my_text.upper().replace(" ", "")
    frequency = dict(Counter(my_text))
    # print(frequency)
    return frequency


def build_heap(freq):
    heap = []
    for char, weight in freq.items():
        heap_element = [weight, [char, ""]]
        heap.append(heap_element)
    heapq.heapify(heap)
    return heap
    # print(heap)


def build_tree(heap):
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        # print(lo[0])
        # print(hi[0])
        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
            # print(pair[1])
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]
            # print(pair[1])
        # print(heap)
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        # print(heap)
    return heap[0]


freq = calculate_frequency("aaaaabccccccddd")
# print(freq)
heap = build_heap(freq)
# print(heap)
tree = build_tree(heap)
for pair in tree[1:]:
    print(pair[0], "->", pair[1])
