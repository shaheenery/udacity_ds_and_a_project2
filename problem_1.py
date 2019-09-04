# Least Recently Used Cache

# The lookup operation (i.e., get()) and put() / set() is supposed to be fast
# for a cache memory.

# While doing the get() operation, if the entry is found in the cache, it is
# known as a cache hit. If, however, the entry is not found, it is known as a
# cache miss.

# When designing a cache, we also place an upper bound on the size of the cache.
# If the cache is full and we want to add a new entry to the cache, we use some
# criteria to remove an element. After removing an element, we use the put()
# operation to insert the new element. The remove operation should also be fast.

# For our first problem, the goal will be to design a data structure known as a
# Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we
# remove the least recently used entry when the cache memory reaches its limit.
# For the current problem, consider both get and set operations as an use operation.

# Your job is to use an appropriate data structure(s) to implement the cache.

# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert
# the element. If the cache is full, you must write code that removes the least
# recently used entry first and then insert the element.

# All operations must take O(1) time.

# For the current problem, you can consider the size of cache = 5.

import unittest

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
        if capacity < 1:
            raise ValueError("LRU Cache size cannot be 0 or negative")
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


class LRU_CacheTest(unittest.TestCase):

    def test_normal_usage(self):
        our_cache = LRU_Cache(5)
        our_cache.set(1, 1);

        our_cache.set(2, 2);
        our_cache.set(3, 3);
        our_cache.set(4, 4);

        self.assertEqual(our_cache.get(1), 1)
        print(our_cache.get(1))
        # 1

        self.assertEqual(our_cache.get(2), 2)
        print(our_cache.get(2))
        # 2

        self.assertEqual(our_cache.get(9), -1)
        print(our_cache.get(9))
        # returns -1 because 9 is not present in the cache

        our_cache.set(5, 5)
        our_cache.set(6, 6)

        self.assertEqual(our_cache.get(3), -1)
        print(our_cache.get(3))
        # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    def test_empty(self):
        our_cache = LRU_Cache(5)

        self.assertEqual(our_cache.get(1), -1)
        print(our_cache.get(1))
        # -1 because cache is empty

    def test_only_1(self):
        #Test only holds one value
        our_cache = LRU_Cache(1)
        our_cache.set(1,1)
        our_cache.set(2,2)
        our_cache.set(3,3)
        our_cache.set(4,4)

        self.assertEqual(our_cache.get(1), -1)
        print(our_cache.get(1))
        # -1

        self.assertEqual(our_cache.get(4), 4)
        print(our_cache.get(4))
        # 4

    def test_raises_with_invalid_capacity(self):
        with self.assertRaises(ValueError):
            our_cache = LRU_Cache(0)

if __name__ == '__main__':
    unittest.main()
