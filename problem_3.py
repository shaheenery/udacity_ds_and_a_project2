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
            elif other.char is None:
                return False
            return self.char > other.char
        return self.priority < other.priority
    def __eq__(self, other):
        return self.priority == other.priority
    def __repr__(self):
        return f"<Node {self.priority} {self.char}>"


def huffman_encoding(data):
    if data is None or data is "":
        return "Please enter a valid string"

    frequency = defaultdict(int)
    pq = []
    for char in data:
        frequency[char] += 1

    for char, freq in frequency.items():
        heappush(pq, Node(freq, char))

    while len(pq) > 1:
        node1 = heappop(pq)
        node2 = heappop(pq)

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

def huffman_decoding(data,tree):
    new_tree = dict([(value, key) for key, value in tree.items()])

    string = ""

    current = ""
    for char in data:
        current += char

        if current in new_tree:
            string += new_tree[current]
            current = ""

    return string, tree


# Test 1 - Normal sentence
a_great_sentence = "Huffman coding is a data compression algorithm."

pre_size = getsizeof(a_great_sentence)
print ("The size of the data is: {}\n".format(pre_size))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

post_size = getsizeof(int(encoded_data, base=2))
print ("The size of the encoded data is: {}\n".format(post_size))
print ("The content of the encoded data is: {}\n".format(encoded_data))


print ("The compression ratio is {}\n".format(post_size/pre_size * 100))

decoded_data, tree = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}".format(getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))

# Test 2 - null input
print (huffman_encoding(None))
# "Please enter a valid string"

# Test 3 - empty input
print (huffman_encoding(""))
# "Please enter a valid string"

# Test 4 - Large Input 10 paragraphs

#normally I would put this in another file
# and probably make it larger, but due to our 1 file per problem limitation,
# I'm stuck.  If there is a way to be able to stick this at the very bottom and
# still be accessible as a variable I would love to know how

bacon_ipsum = '''\
Spicy jalapeno bacon ipsum dolor amet dolor ut sausage ex lorem strip steak incididunt porchetta cow leberkas chuck quis bresaola. Fugiat deserunt ut pariatur officia porchetta sed nulla irure nostrud eu bacon id. Chuck ribeye adipisicing porchetta laborum turducken tempor enim kielbasa pork chop tenderloin sed burgdoggen strip steak. Swine in shank quis kevin elit officia ex aute cow, nostrud ullamco turducken. Buffalo excepteur tenderloin, eu tri-tip drumstick pancetta laboris aliqua ut. Sirloin ut ad commodo, ex officia aute excepteur short loin aliqua pork belly labore buffalo ea.

Consectetur est tenderloin, shank turducken dolore ground round ham buffalo rump voluptate short ribs mollit irure. Bacon salami laborum nostrud esse ex. Filet mignon drumstick burgdoggen turkey ea pork chop in aute short ribs pork loin chuck buffalo. Landjaeger minim eiusmod hamburger t-bone, swine beef ribs sausage fugiat andouille turducken sed shank. Aliqua jerky shank beef, ipsum biltong ea short loin in corned beef.

Sed fugiat excepteur deserunt nostrud leberkas ipsum ut elit beef ribs. Non in quis, pastrami flank kevin tempor fatback. Reprehenderit pastrami fatback porchetta labore ham hock doner shankle meatloaf ground round. Sint cillum drumstick nisi tri-tip, cupidatat nulla. Enim laboris bacon short ribs, t-bone jowl ut pariatur ut eiusmod sed turducken ullamco duis. Adipisicing boudin landjaeger, exercitation ipsum turkey shankle porchetta venison short loin buffalo aliquip veniam ribeye biltong. Duis mollit minim veniam, picanha et labore.

Pork chop do duis minim magna tongue short ribs filet mignon consequat occaecat velit labore laborum aliqua. Eiusmod ham fatback, beef ribs jerky pancetta t-bone doner. Sint filet mignon qui fatback pariatur. Irure flank porchetta laborum.

Pariatur in et short ribs sunt quis consequat. Ut ex kielbasa, bresaola cow burgdoggen minim pastrami consequat qui turducken strip steak shank fugiat tail. Fugiat qui in swine, short loin eu aliquip deserunt velit pig. Laborum corned beef quis pork belly tail ut pastrami tri-tip brisket rump. Elit ullamco anim ham hock fatback dolore proident rump sint dolor et est picanha excepteur.

Picanha et hamburger esse pig sunt. Non et spare ribs, irure bresaola sunt buffalo rump eu tenderloin ipsum shoulder hamburger shankle. Jowl non brisket, occaecat corned beef est strip steak cow tri-tip meatloaf prosciutto. Voluptate tri-tip laborum in dolor anim minim dolore pork loin. Ad in shank shankle exercitation laboris, pork proident et.

In porchetta enim filet mignon qui. Ham pork shankle est. Irure beef ribs drumstick, consequat adipisicing pariatur chuck brisket. Tail aute shankle enim fatback chicken short ribs meatball t-bone sed. Ipsum hamburger pancetta biltong t-bone ut irure mollit turducken occaecat shank landjaeger. Dolore venison elit quis.

Qui filet mignon sed, rump tail jowl duis ad porchetta. Enim aute pariatur kielbasa ut alcatra labore sunt prosciutto buffalo corned beef. Jerky cupim ullamco mollit meatball irure. Pork esse magna corned beef. Pork loin ad landjaeger ut. Et in commodo pariatur lorem beef veniam duis magna ribeye anim kielbasa landjaeger.

Eu kielbasa dolore culpa biltong excepteur burgdoggen anim pig esse andouille doner in ut. Sint minim voluptate, short loin incididunt anim burgdoggen ullamco filet mignon chuck lorem. Ground round id tenderloin ut boudin adipisicing tongue sirloin incididunt fugiat et pork loin dolore hamburger. Beef ribs meatloaf est hamburger brisket boudin, pork chop eu ullamco. Pariatur andouille jerky pancetta beef ribs ut spare ribs ham chicken do nulla dolore shank velit ea. Et tenderloin salami corned beef veniam bresaola dolor shank in. Boudin tenderloin minim picanha shankle filet mignon est spare ribs andouille officia pig reprehenderit chicken.

Exercitation swine buffalo, short loin ut consequat nulla laborum ribeye shankle. Anim beef beef ribs voluptate. Pork belly pork loin pastrami fatback. Sed cupim aute consequat. Nisi cillum jowl tongue pig enim picanha chicken bacon dolor. Sint incididunt pastrami biltong bacon bresaola in pork dolore et ea spare ribs pariatur chicken mollit.\
'''
# baconipsum.com if you're curious

pre_size = getsizeof(bacon_ipsum)
print ("The size of the data is: {}\n".format(pre_size))
print ("The content of the data is: {}\n".format(bacon_ipsum))

encoded_data, tree = huffman_encoding(bacon_ipsum)

post_size = getsizeof(int(encoded_data, base=2))
print ("The size of the encoded data is: {}\n".format(post_size))
print ("The content of the encoded data is: {}\n".format(encoded_data))


print ("The compression ratio is {}\n".format(post_size/pre_size * 100))

decoded_data, tree = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}".format(getsizeof(decoded_data)))
print ("The content of the decoded data is: {}\n".format(decoded_data))
