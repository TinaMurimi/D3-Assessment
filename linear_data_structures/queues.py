# A queue is ordered collection of items where the addition of new items
# happens at one end, called the “rear,” and the removal of existing items
# occurs at the other end, commonly called the “front.” As an element enters
# the queue it starts at the rear and makes its way toward the front, waiting
# until that time when it is the next element to be removed.
# The most recently added item in the queue must wait at the end
# of the collection. The item that has been in the collection the
# longest is at the front.
# This ordering principle is sometimes called FIFO, first-in first-out.
# It is also known as “first-come first-served.”
# Queues can assist in the construction of timing simulations.


class Queue():
    """
    Creates a new queue that is empty.
    It needs no parameters and returns an empty queue.
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        """
        Tests to see whether the queue is empty.
        It needs no parameters and returns a boolean value.
        """
        return len(self.items) == 0

    def enqueue(self, item):
        """
        Adds a new item to the rear of the queue.
        It needs the item and returns nothing.
        Note: append is 𝑂(1) and insert(i,item) is 𝑂(𝑛)
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes the front item from the queue.
        It needs no parameters and returns the item. The queue is modified.
        pop() is 𝑂(1) but pop(i) is 𝑂(𝑛)
        """
        return self.items.pop(0)

    def size(self):
        """
        Returns the number of items on the queue.
        It needs no parameters and returns an integer.
        """
        return len(self.items)


q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print(q.items)
q.dequeue()
print(q.items)
