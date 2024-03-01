import heapq
from collections import Counter
import math


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
        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]


def compute_huffman_avg_length(freq, tree, length):
    huffman_avg_length = 0
    for pair in tree[1:]:
        # print(pair[0])
        # print(len(pair[1]) * (freq[pair[0]] / length))
        huffman_avg_length += len(pair[1]) * (freq[pair[0]] / length)
        # print(huffman_avg_length)
    return huffman_avg_length


def entropy(freq, length):
    H = 0  # entropy
    p = []
    for value in freq.items():
        # print(value[1])
        prob = value[1] / length
        p.append(prob)
    print(p)
    for x in p:
        H += -(x * math.log2(x))
    return H


message = "aaabbbbbccccccddddee"
# print(len(message))
freq = calculate_frequency(message)
heap = build_heap(freq)
tree = build_tree(heap)

huffman_avg_length = compute_huffman_avg_length(freq, tree, len(message))
H = entropy(freq, len(message))
print("Huffman : %.2f bits" % huffman_avg_length)
print("Entropy : %.2f bits" % H)
if huffman_avg_length >= H:
    print("Huffman code is optimal")
else:
    print("Code is not optimal")
