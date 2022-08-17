from LinkedLists.linkedQueue import LinkedQueue


def merge(s1, s2, s):
    """Merge two sorted queue instances s1 and s2 into empty queue s"""
    while not s1.is_empty() and s2.is_empty():
        if s1.first() < s2.first():
            s.enqueue(s1.dequeue())
        else:
            s.enqueue(s2.dequeue())

    while not s1.is_empty():        # move remaining elements of s1 to S
        s.enqueue(s1.dequeue())

    while not s2.is_empty():        # move remaining elements of s2 to S
        s.enqueue(s2.dequeue())


def merge_sort(S):
    """Sort elements of queue S using the merge sort algorithm"""
    n = len(S)
    if n < 2:
        return      # lis is already sorted
    # divide
    s1 = LinkedQueue()      # or any other queue implementation
    s2 = LinkedQueue()

    while len(s1) < n//2:       # move the first n//2 elements of s1
        s1.enqueue(S.dequeue())

    # conquer
    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, S)
