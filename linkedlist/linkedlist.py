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
        if index < 0 or index > self.length:
            return None
        else:
            item = self.head
            for _ in range(index):
                item = item.next
            return item

    def set_index_value(self, index, value):
        temp = self.get(index=index)
        if temp:
            temp.value = value
            return True
        return False