# A list is a collection of items where each item holds a relative position with respect to the others.

# Linked lists are made up of data records linked together by pointers.
# This means that the data records that hold the actual “data payload”
# can be stored anywhere in memory—what creates the linear ordering is
# how each data record “points” to the next one.
# Linked lists can have its elements dynamically allocated unlike
# arrays that are contiguous.
# A linked list contains a node, and each node contains a value and pointer
# to another node. The starting node of a linked list is called a header

# As long as we know where to find the first node (containing the first item),
# each item after that can be found by successively following the next links.
# With this in mind, the UnorderedList class must maintain a reference to the
# first node. The following code shows the constructor. Note that each list
# object will maintain a single reference to the head of the list.

# In a doubly-linked list, each element has a reference to both the
# next and the previous element. Why is this useful? Having a reference
# to the previous element can speed up some operations,
# like removing (“unlinking”) an element from a list or traversing the
# list in reverse order.


class ListNode:
    """
    A node in a singly-linked list.
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

        print(f'self.data: {self.data}')
        print(f'self.next: {self.next}')

    def __repr__(self):
        print(f'repr(self.data): {repr(self.data)}')
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head

        print(f'self.head: {self.head}')

        while curr:
            nodes.append(repr(curr))

            print(f'curr.next: {curr.next}')
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node


lst = SinglyLinkedList()
print()
print(lst)

print()
lst.prepend(23)
print(lst)

print()
lst.prepend('a')
print(lst)

print()
lst.prepend('xyz')
print(lst)

print()
lst.append('klm')
print(lst)

print()
lst.append('hmn')
print(lst)

print()
lst.prepend('qoi')
print(lst)