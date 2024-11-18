from imghdr import tests
from logging import fatal


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        print out entire list
        """
        if self.length == 0:
            print("list is empty")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Adds node to the end
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Removes node from end
        """
        temp = None
        if self.length == 0:
            return temp
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, number: int):
        """
        Adds node to the beginning
        """
        temp = Node(number)
        if self.length == 0:
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
            self.length += 1
        return True

    def pop_first(self):
        """
        Removes node from the beginning
        """
        if self.length == 0 or self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return None
        else:
            removed_item = self.head
            self.head = removed_item.next
            removed_item.next = None
            self.length -= 1
            return removed_item

    def get(self, index):
        """
        get Node
        """
        if index < 0 or index > self.length:
            return None
        else:
            item = self.head
            for _ in range(index):
                item = item.next
            return item

    def set_index_value(self, index, value):
        """
        set Node value
        """
        temp = self.get(index=index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """
        Insert new Node at specified index
        """
        if self.length == 0 or self.length == 1:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        previous = self.get(index=index - 1)
        if previous:
            new_next = previous.next
            previous.next = Node(value=value)
            previous.next.next = new_next
            return True
        return False

    def remove(self, index):
        """
        remove Node at specified index
        """
        if self.length == 0 or index >= self.length:
            return None
        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        parent = self.get(index=index - 1)
        node_to_remove = parent.next
        parent.next = node_to_remove.next
        self.length -= 1
        return node_to_remove

    def reverse(self):
        """
        reverse list in opposite order
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle(self):
        """
        returns middle node. If the linked list has an even number of nodes, return the first node of the second half of the list.
        """
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_loop(self):
        """
        returns True if there is a cycle or loop present in the linked list.
        """
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
