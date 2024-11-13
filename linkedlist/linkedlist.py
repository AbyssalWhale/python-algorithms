from imghdr import tests


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
        # 1. 0 nodes
        # 2. 1 node
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

    def pop_first_2(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp





