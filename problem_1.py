import time
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def set_value(self, value):
        self.value = value

    def set_prev(self, node):
        self.prev = node

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        if self.prev:
            prev = self.prev.value
        else:
            prev = None
        if self.next:
            _next = self.next.value
        else:
            _next = None

        return f"<node val={str(self.value)} prev={prev} next={_next}>"

class DLL:
    def __init__(self, node = None):
        self.head = node
        self.tail = node

    def move_to_tail(self, node):
        if node == self.tail:
            return # no-op

        prev_node = node.prev
        next_node = node.next

        next_node.set_prev(prev_node)
        if prev_node:
            prev_node.set_next(next_node)
        else:
            self.head = next_node

        node.set_next(None)
        node.set_prev(self.tail)
        self.tail.set_next(node)
        self.tail = node
        return

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return node

        self.tail.set_next(node)
        node.set_prev(self.tail)

        self.tail = node

        return node

    def pop_left(self):
        old_head = self.head
        self.head = old_head.next
        return old_head

    def __repr__(self):
        node = self.head
        s = "DLL: "
        while node:
            s += str(node.value) + ","
            node = node.next

        return s

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.count = 0
        self.list = DLL()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        lookup = self.dict.get(key)

        if lookup:
            self.list.move_to_tail(lookup)
            _key, value = lookup.value
            return value

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        lookup = self.dict.get(key)
        if lookup:
            lookup.set_value((key,value))
            self.list.move_to_tail(lookup)
            return

        if self.count < self.capacity:
            node = self.list.add((key,value))
            self.dict[key] = node
            self.count += 1
        else:
            old_key, _val = self.list.pop_left().value
            node = self.list.add((key,value))
            self.dict[key] = node
            del self.dict[old_key]

    def __repr__(self):
        return self.list.__repr__() + "\nDict: " + self.dict.__repr__() + "\n"

our_cache = LRU_Cache(5)
our_cache.set(1, 1);

our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.get(1))     # returns 1
print(our_cache.get(2))     # returns 2

print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
