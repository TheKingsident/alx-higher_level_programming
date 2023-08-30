class Node:
    """
    Represents a node of a singly linked list.

    This class defines a node with data and next_node private attributes.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of Node.

        Args:
            data (int): The data for the node.
            next_node (Node): The next node in the linked list
            (default is None).

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not None or a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node of the node.

        Args:
            value (Node or None): The new next node value.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be None or a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    This class defines a linked list with a head attribute.
    """

    def __init__(self):
        """
        Initializes a new instance of SinglyLinkedList.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return '\n'.join(elements)  # Changed separator to '\n'
