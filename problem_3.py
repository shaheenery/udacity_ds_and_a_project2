# Huffman Coding

# A Huffman code is a type of optimal prefix code that is used for compressing
# data. The Huffman encoding and decoding schema is also lossless, meaning that
# when compressing the data to make it smaller, there is no loss of information.

# The Huffman algorithm works by assigning codes that correspond to the relative
# frequency of each character for each character. The Huffman code can be of any
# length and does not require a prefix; therefore, this binary code can be
# visualized on a binary tree with each encoded character being stored on leafs.

import sys

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
