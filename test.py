class LinkedListNode:
    """
    Node to be used in linked list
    === Attributes ===
    @param LinkedListNode next_: successor to this LinkedListNode
    @param object value: data this LinkedListNode represents
    """
    def __init__(self, value, next_=None):
        """
        Create LinkedListNode self with data value and successor next_.
        @param LinkedListNode self: this LinkedListNode
        @param object value: data of this linked list node
        @param LinkedListNode|None next_: successor to this LinkedListNode.
        @rtype: None
        """
        self.value, self.next_ = value, next_

    def __str__(self):
        """
        Return a user-friendly representation of this LinkedListNode.
        @param LinkedListNode self: this LinkedListNode
        @rtype: str
        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        # start with a string s to represent current node.
        s = "{} ->".format(self.value)
        # create a reference to "walk" along the list
        current_node = self.next_
        # for each subsequent node in the list, build s
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s

class LinkedList:
    """
    Collection of LinkedListNodes
    === Attributes ==
    @param: LinkedListNode front: first node of this LinkedList
    @param LinkedListNode back: last node of this LinkedList
    @param int size: number of nodes in this LinkedList
    a non-negative integer
    """
    def __init__(self):
        """
        Create an empty linked list.
        @param LinkedList self: this LinkedList
        @rtype: None
        """
        self.front, self.back = None, None
        self.size = 0

    def append(self, value):
        """
        Insert a new LinkedListNode with value after self.back.
        @param LinkedList self: this LinkedList.
        @param object value: value of new LinkedListNode
        @rtype: None
        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        new_node = LinkedListNode(value)
        if self.front is None:
            # append to an empty LinkedList
            self.front = self.back = new_node
        else:
            # self.back better not be None
            assert self.back, 'Unexpected None node'
            self.back.next_ = new_node
            self.back = new_node
        self.size += 1

    def remove_first_satisfier(self, predicate):
        """
        Remove first node whose value satisfies predicate.
        If there is no such node, leave self as is.

        @param LinkedList self: this linked list
        @param (object)->bool predicate: boolean function
        @rtype: None
        >>> list_ = LinkedList()
        >>> list_.append(5)
        >>> list_.append(3)
        >>> print(list_.front)
        5 -> 3 ->|
        >>> def f(n): return n > 4
        >>> list_.remove_first_satisfier(f)
        >>> print(list_.front)
        3 ->|
        >>> list_.append(5)
        >>> list_.append(7)
        >>> list_.remove_first_satisfier(f)
        >>> print(list_.front)
        3 -> 7 ->|
        """
        curr_node = self.front
        if predicate(curr_node) and curr_node is not self.back:
            self.front = curr_node.next_
        else:
            while not predicate(curr_node.next_) and curr_node.next_ is not self.back:
                curr_node = curr_node.next_
            if curr_node.next_ is not self.back:
                curr_node.next_ = curr_node.next_.next_

if __name__ == "__main__":
    import doctest
    doctest.testmod()
