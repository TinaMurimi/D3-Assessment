# A stack is an ordered collection of items where the
# addition of new items and the removal of existing items
# always takes place at the same end.
# Ordering Principle: LIFO
# Stacks are very useful for designing algorithms to evaluate and translate expressions.
# Stacks can provide a reversal characteristic.


class Stack():
    """
    Creates a new stack that is empty.
    It needs no parameters and returns an empty stack.
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        """
        Tests to see whether the stack is empty.
        It needs no parameters and returns a boolean value.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Adds a new item to the top of the stack.
        It needs the item and returns nothing.
        Note: append is 𝑂(1) and insert(i,item) is 𝑂(𝑛)
        """
        self.items.append(item)

    def peek(self):
        """
        Returns the top item from the stack but does not remove it.
        It needs no parameters. The stack is not modified.
        𝑂(1)
        """
        return self.items[-1]

    def size(self):
        """
        Returns the number of items on the stack.
        It needs no parameters and returns an integer.
        𝑂(𝑛)
        """
        return len(self.items)

    def pop(self):
        """
        Removes the top item from the stack.
        It needs no parameters and returns the item.
        The stack is modified.
        pop() is 𝑂(1) but pop(i) is 𝑂(𝑛)
        """
        return self.items.pop()


# m = Stack()
# m.push('x')
# m.push('y')
# m.push('z')
# while not m.isEmpty():
#     m.pop()
#     m.pop()
# print(m.peek())

def rev_string(my_str):
    """
    Uses a stack to reverse the characters in a string.
    """
    s_old = Stack()
    s_new = Stack()

    s_old.items = list(my_str)
    print(s_old.items)
    while not s_old.isEmpty():
        s_new.push(s_old.pop())

    return "".join(s_new.items)


print(rev_string("lip"))