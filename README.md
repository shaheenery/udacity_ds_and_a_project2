# Data Structures and Algorithms
## Project 2

### Problem 1 - LRU Cache

#### Complexity

Time: O(1)
Space: O(n)

#### Analysis

For this problem *n* is the capacity of the cache i.e. the maximum number of items we are willing to store at once.  In order to achieve constant `get` and `set` performance I chose the combination of a map and a doubly-linked-list (DLL).  The map gives us a datastore capable of getting and setting in O(1) time.  The DLL, with nodes referenced by the map, allow us to add or move any item to the back of the list in O(1) time.  The DLL must maintain a reference to the current head and tail nodes for this to be possible.

The space complexity is O(n) because there must be key stored and node created in the DLL for each item in the cache.  The space requirements will grow linearly with the capacity of the cache that we set when we initialize it.

------



### Problem 2 - Finding Files

#### Complexity

Time: O(n)
Space: O(n)

#### Analysis

Recursion fits well into the hierarchy used by a file system.  The main work can be done on files in a folder and then the function called recursively on each child folder with the results being appended and returned to the top level call.  The time complexity is O(n) where n is the total number of files and folders contained in the folder at the file path specified as an argument.

The space complexity is O(n) where n is the `max()` of "the number of children in the folder or subfolder containing the most children" and "the number of files found that match the supplied type."  The reason I describe it in this was is that the results of `os.scandir()` must be stored in memory while being iterated through.  So, even if no match is ever found and a subfolder has 100 files a list of size 100 would be held in memory at some point.  If the list is somehow streamed and not held in memory, that would make n the number of matches.

------



### Problem 3 - Huffman Encoding  / Decoding

#### Complexity

Time: O(n log(n))
Space: O(n)

##### Calculate Frequency

To calculate the freqency of each letter in the string I use a `defaultdict(int)` and increment the value of the letter's key at each occurrence which is a O(1) operation.

##### Sort and build tree

The tree structure built using the Huffman technique behaves much like a max heap.  I use the frequency of each letter's occurrence as its priority for determining its place in the heap, with the most frequently occuring letter at the top.  I use the `heapq` module of the Python standard library to implement heap behavior on a Python `list()`.   Sorting using a heap takes O(n log(n)) in the best, worst, and average cases.  **This is the highest complexity contained in the function**

##### Generate Encoding

Then, I traverse the entirely built tree (of 2n-1 nodes) to build a mapping between the Huffman code and a character.

##### Convert

Finally, I generate a string of the encoded original string to return. O(n)

##### Space

The number of nodes that comprise a Huffman tree is 2n - 1 in the worst case of encoding a string filled with all unique characters.  This number is composed of the letter nodes and frequency nodes needed to build out the tree.  The number of entries in our `dict` is the number of unique characters in our string O(n).  Since the two main sets of stored data both have a space complexity of O(n) we can say that the overall method is O(n).

------



### Problem 4 - Active Directory

#### Complexity

Time: O(n)
Space: O(n)

#### Analysis

This is essentially the same problem as [number 2](#problem-4-active-directory). In this case *n* is how many groups are nested in the searched group and how many users are in each of those groups.  The space complexity is O(n) where *n* is the number of nested groups and users in the group to be searched

You could see performance gains by using a dictionary instead of an array for group membership.  That would eliminate spending time iterating through an array of group members, but it would not help in the worst case of the user being located at the lowest decendent leaf of the tree (depending on search used, of course)

### Problem 5 - Blockchain

#### Complexity

Time: O(1)
Space: O(n)

#### Analysis

Since the only operation that we perform is the `append` feature of the blockchain and we use a linked list, the complexity is O(1) since we can simply set the new node as the new tail and link to the old tail from the new node.  The space complexity is O(n) since we will add a new element to the linked list for every single block in the block chain.

------



### Problem 6 - Union and Intersection of Two Linked Lists

#### Complexity

##### Union

Time: O(n)
Space: O(n)

##### Intersection

Time: O(n)
Space: O(n)

#### Analysis

For `LinkedList.union()` the time complexity is O(n) since each element in both lists must be iterated over, O(n + m).  I chose to use the Python `set()` as an intermediary data structure to remove duplicate values.  For a set, `add` and `pop` are O(1) operations as the internal implementation is typically a dictionary.  The worst case for the space complexity of `union()` is O(n) because both lists could have different values from each other requiring us to store a new linked list of size O(n + m).

For `LinkedLinked.intersection()` the time and space complexity are also O(n) for the same reasons.  Both lists must be iterated over.  And even though an additional check is made for a value's inclusion in both intermediary sets, the O(1) nature of the check only ups the complexity to 2n which simplifies to O(n).  The worst case for space for `intersection` is if list n contained all of list m (or vice versa) giving us a complexity of O(m).

Without the use of an intermediary data structure with O(1) lookups e.g. iterating through list B for each item in list A, the time complexity would then be O(n * n)