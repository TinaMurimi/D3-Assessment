# A deque, also known as a double-ended queue, is an ordered collection
# of items similar to the queue. It has two ends, a front and a rear,
# and the items remain positioned in the collection. What makes a deque
# different is the unrestrictive nature of adding and removing items.
# New items can be added at either the front or the rear.
# Likewise, existing items can be removed from either end. In a sense,
# this hybrid linear structure provides all the capabilities of
# stacks and queues in a single data structure.

# It is important to note that even though the deque can assume many
# of the characteristics of stacks and queues, it does not require the
# LIFO and FIFO orderings that are enforced by those data structures. It is up
# to you to make consistent use of the addition and removal operations.

# # Performance of Deque
# 1. Inserting and removing elements at the front and back of a deque is a
#   fast O(1) operation. However, inserting or removing in the middle
#   takes O(n) time because we don’t have access to the previous-element
#   or next-element linked list pointers. That’s abstracted away by the deque interface.
# 2. Storage is O(n)—but not every element gets its own list node.
#   The deque class uses blocks that hold multiple elements at once and then
#   these blocks are linked together as a doubly-linked list. As of
#   CPython 3.6 the block size is 64 elements. This incurs some space overhead
#   but retains the general performance characteristics given a large
#   enough number of elements.
# 3. In-place reversal: In Python 3.2+ the elements in a deque instance
#   can be reversed in-place with the reverse() method. This takes O(n)
#   time and no extra space.


class Deque():
    """
    Creates a new deque that is empty.
    It needs no parameters and returns an empty deque.
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        """
        Tests to see whether the deque is empty.
        It needs no parameters and returns a boolean value.
        """
        return len(self.items) == 0

    def add_rear(self, item):
        """
        Adds a new item to the rear of the deque.
        It needs the item and returns nothing.
        Note: append is 𝑂(1) and insert(i,item) is 𝑂(𝑛)
        """
        self.items.append(item)

    def add_front(self, item):
        """
        Adds a new item to the front of the deque.
        It needs the item and returns nothing.
        Note: append is 𝑂(1) and insert(i,item) is 𝑂(𝑛)
        """
        self.items.insert(0, item)

    def remove_rear(self):
        """
        Removes the rear item from the deque.
        It needs no parameters and returns the item.
        The deque is modified.
        pop() is 𝑂(1) but pop(i) is 𝑂(𝑛)
        """
        return self.items.pop()

    def remove_front(self):
        """
        Removes the front item from the deque.
        It needs no parameters and returns the item.
        The deque is modified.
        pop() is 𝑂(1) but pop(i) is 𝑂(𝑛)
        """
        return self.items.pop(0)

    def size(self):
        """
        Returns the number of items on the deque.
        It needs no parameters and returns an integer.
        """
        return len(self.items)
