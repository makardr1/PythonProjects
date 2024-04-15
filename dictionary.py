# A hash table is a data structure for storing key pairs and their values.
# In fact, it is an array where the location of the element depends on the
# value of the element itself. The relationship between the value of an
# element and its position in the hash table is set by the hash function.
from typing import Union


class Node:
    def __init__(self, value) -> None:
        self.value: Union[int, str] = value
        self.next: Union[None, Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Union[None, Node] = None

    # Adding a key-value pair
    def put(self, key: int, value: int) -> None:
        new_node = Node([key, value])
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current is not None:
                if current.value[0] == key:
                    current.value[1] = value
                    return
                current = current.next
            # Add to the top of the list
            new_node.next = self.head
            self.head = new_node

    # Getting the value by key
    def get(self, key: int) -> Union[int, str]:
        if self.head is None:
            raise IndexError
        else:
            current = self.head
            while current is not None:
                if current.value[0] == key:
                    print(current.value[1])
                    return
                current = current.next
            raise IndexError

    # Delete an item
    def delete(self, key: int) -> Union[int, str]:
        if self.head is None:
            raise IndexError
        else:
            if self.head.value[0] == key:
                result = self.head.value[1]
                self.head = self.head.next
                print(result)
                return
            left = self.head
            right = self.head.next
            while right:
                if right.value[0] == key:
                    result = right.value[1]
                    left.next = right.next
                    print(result)
                    return
                left = left.next
                right = right.next
            raise IndexError

    # Outputs all values of the linked list
    def conclusion(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')


class HashMap:
    def __init__(self):
        # Module
        self.module: int = 133571
        # Hash table
        self.hash_table: list = [None] * self.module

    # Hash calculation
    def hash_function(self, key: int) -> int:
        return key % self.module

    # Adding a key-value pair
    def put(self, key: int, value: int) -> None:
        index: int = self.hash_function(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = LinkedList()
        self.hash_table[index].put(key, value)

    # Getting the value by key
    def get(self, key: int) -> None:
        index: int = self.hash_function(key)
        if self.hash_table[index] is None:
            raise IndexError
        self.hash_table[index].get(key)

    # Deleting a key from a table
    def delete(self, key: int) -> None:
        index: int = self.hash_function(key)
        if self.hash_table[index] is None:
            raise IndexError
        self.hash_table[index].delete(key)

    # Outputs all values of the linked list
    def conclusion(self, key: int) -> None:
        index: int = self.hash_function(key)
        self.hash_table[index].conclusion()
