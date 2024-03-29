# Union and Intersection of Two Linked Lists

# Your task for this problem is to fill out the union and intersection
# functions.

# The union of two sets A and B is the set of elements which
# are in A, in B, or in both A and B. The intersection of two sets A and B,
# denoted by A ∩ B, is the set of all objects that are members of both the
# sets A and B.

# You will take in two linked lists and return a linked list that is composed
# of either the union or intersection, respectively. Once you have completed the
# problem you will create your own test cases and perform your own run time analysis on the code.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    both = set()
    node = llist_1.head
    while node:
        both.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        both.add(node.value)
        node = node.next

    result = LinkedList()
    for _ in range(len(both)):
        result.append(both.pop())

    return result

def intersection(llist_1, llist_2):
    set_1 = set()
    set_2 = set()

    node = llist_1.head
    while node:
        set_1.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        set_2.add(node.value)
        node = node.next

    inter = LinkedList()
    for value in set_1:
        if value in set_2:
            inter.append(value)

    return inter


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# expect [3,2,4,35,6,65,21,32,9,1,11]
print (intersection(linked_list_1,linked_list_2))
# expect [4,6,21]


# ***************************
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1,3]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# expect [1,2,3,4,6,7,8,9,11,21,23,35,65,]
print (intersection(linked_list_3,linked_list_4))
# expect [3]


# ***************************
# Test case 3


linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1]
element_2 = [1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
# expect [1]
print (intersection(linked_list_5,linked_list_6))
# expect [1]


# ***************************
# Test case 4


linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

print (union(linked_list_7, linked_list_8))
# []
print (intersection(linked_list_7, linked_list_8))
# []
