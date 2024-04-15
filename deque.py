# A deque (double-ended queue) is a data structure that supports adding and
# removing elements from both the front and the back of the sequence
# efficiently.
class Deque:
    def __init__(self, maximum: int) -> None:
        self.dec: list = [None] * maximum
        self.maximum: int = maximum
        # Queue length
        self.length: int = 0
        # Indexes to add
        self.start = self.end = 0
        # Indexes to delete
        self.pop_start = self.pop_end = 0
        # To shift when initially added
        self.flag: bool = True

    # Reset pointers
    def reset(self) -> None:
        if self.length == 0:
            self.start = self.end = 0
            self.pop_start = self.pop_end = 0
            self.flag = True

    # Add an element to the beginning
    def push_front(self, value: str) -> None:
        # If the data structure is full
        if self.length == self.maximum:
            raise IndexError

        # If length = 0, then we reset the pointers
        self.reset()

        # If flag = True, then move the pointer to add to the end by 1
        if self.flag:
            self.end = (self.end + 1) % self.maximum
        self.dec[self.start] = value
        self.pop_start = self.start
        self.start = (self.start - 1) % self.maximum
        self.length += 1
        self.flag = False

    # Add an element to the end
    def push_back(self, value: str) -> None:
        # If the data structure is full
        if self.length == self.maximum:
            raise IndexError

        # If length = 0, then we reset the pointers
        self.reset()

        # If flag = True, then move the pointer to add to the beginning by 1
        if self.flag:
            self.start = (self.start - 1) % self.maximum
        self.dec[self.end] = value
        self.pop_end = self.end
        self.end = (self.end + 1) % self.maximum
        self.length += 1
        self.flag = False

    # Print the first element and delete it
    def pop_front(self) -> str:
        # Length check
        if self.length == 0:
            self.reset()
            raise IndexError

        pop_value: str = self.dec[self.pop_start]
        self.dec[self.pop_start] = None
        self.start = self.pop_start
        self.pop_start = (self.pop_start + 1) % self.maximum
        self.length -= 1
        return pop_value

    # Print the last element and delete it
    def pop_back(self) -> str:
        # Length check
        if self.length == 0:
            self.reset()
            raise IndexError

        pop_value: str = self.dec[self.pop_end]
        self.dec[self.pop_end] = None
        self.end = self.pop_end
        self.pop_end = (self.pop_end - 1) % self.maximum
        self.length -= 1
        return pop_value
