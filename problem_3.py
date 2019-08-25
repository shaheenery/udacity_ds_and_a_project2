# Huffman Coding

# A Huffman code is a type of optimal prefix code that is used for compressing
# data. The Huffman encoding and decoding schema is also lossless, meaning that
# when compressing the data to make it smaller, there is no loss of information.

# The Huffman algorithm works by assigning codes that correspond to the relative
# frequency of each character for each character. The Huffman code can be of any
# length and does not require a prefix; therefore, this binary code can be
# visualized on a binary tree with each encoded character being stored on leafs.

from collections import defaultdict
from functools import total_ordering
from heapq import heappush, heappop
from sys import getsizeof

@total_ordering
class Node(object):
    """docstring for Node"""
    def __init__(self, priority=None, char=None ):
        self.priority = priority
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        if self.priority == other.priority:
            if self.char is None:
                return True
            if other.char is None:
                return False
            return self.char > other.char
        return self.priority < other.priority
    def __eq__(self, other):
        return self.priority == other.priority
    def __repr__(self):
        return f"<Node {self.priority} {self.char}>"


def huffman_encoding(data):
    frequency = defaultdict(int)
    pq = []
    for char in data:
        frequency[char] += 1

    for char, freq in frequency.items():
        heappush(pq, Node(freq, char))

    while len(pq) > 1:
        node1 = heappop(pq)
        node2 = heappop(pq)
        print(node2, node1)
        combined = node1.priority + node2.priority
        internal_node = Node(combined)
        internal_node.left = node1
        internal_node.right = node2
        heappush(pq, internal_node)

    node = heappop(pq)

    def _encode(node, encodings={}, encoding=""):

        if node.char is not None:
            encodings[node.char] = encoding

        if node.left:
            _encode(node.left, encodings, encoding + "0")


        if node.right:
            _encode(node.right, encodings, encoding + "1")

        return encodings

    encodings = _encode(node)

    string = ""

    for char in data:
        string += encodings[char]

    return string, encodings

# def huffman_decoding(data,tree):
#     pass

# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"
a_great_sentence = "Huffman coding is a data compression algorithm."
# a_great_sentence = "aaaaaaaaaaaaaaabbbbbbbccccccddddddeeeee"

pre_size = getsizeof(a_great_sentence)
print ("The size of the data is: {}\n".format(pre_size))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)
print(tree)
post_size = getsizeof(int(encoded_data, base=2))
print ("The size of the encoded data is: {}\n".format(post_size))
print ("The content of the encoded data is: {}\n".format(encoded_data))


print ("The compression ratio is {}".format(post_size/pre_size * 100))
#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))
