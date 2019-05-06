"""
- A comparison sort algorithm that builds a sorted list one entry at a time.
- Adaptive: Efficient for datasets that are subtantially sorted.
- Stable: Maintains the relative order of items with equal keys.
- In-place: Requires only a constant amount O(1) of additional memory space.
- On-time: Can sort a list as it receives it

Maintains a sorted sublist in the lower positions of the list.
Each new list is inserted back into the previous list such that the
sorted sublist is one item larger.

Performance: Worst Case O(n2), Best Case O(n)
Space Complexity: O(n)
"""


def insertion_sort(elements):
    iterations = 0

    l = len(elements)

    # We begin by assuming that a list with one item (position 0)
    # is already sorted
    for i in range(1, l):
        print(f'\ni: {i}')
        print('----')

        curr = elements[i]
        pos = i

        # print(f'pos: {pos}')
        # print(f'1, elements[pos]: {elements[pos]}')
        
        # print(f'{elements[pos-1]} > {curr}')

        # print(f'pos: {pos}')

        # print(elements)

        print(f'curr: {curr}')

        while pos > 0 and elements[pos-1] > curr:
            # print(f'1, elements[pos]: {elements[pos]}')
            print(f'pos: {pos}')
            print(f'{elements[pos-1]} > {curr}')
            elements[pos] = elements[pos-1]
            pos -= 1

        print(f'insert at: {pos}')
        elements[pos] = curr

        # print(f'2, elements[pos]: {elements[pos]}')

        # print(elements)

        iterations += 1

    print(f'\nTotal comparisons: {iterations}\n')
    return elements


# elements = [20, 545, 26, 26, 76, 54, 31, 44]
# elements = [20, 3, 545, 26, 26, 76, 54, 31, 44]
elements = [54, 26, 93, 17, 77, 31, 44]
insertion_sort(elements)

print('\nSorted list')
print(insertion_sort(elements))