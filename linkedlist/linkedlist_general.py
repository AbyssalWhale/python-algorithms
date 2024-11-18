from tabulate import tabulate

from linkedlist import LinkedList

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def list_vs_linkedlist():
    print("-" * 10, "LIST VS LINKED LIST", "-" * 10)
    data = [
        ["append", f"{GREEN}O(1){RESET}", f"{GREEN}O(1){RESET}"],
        ["pop", f"{RED}O(n){RESET}", f"{GREEN}O(1){RESET}"],
        ["prepend", f"{GREEN}O(1){RESET}", f"{RED}O(n){RESET}"],
        ["pop first", f"{GREEN}O(1){RESET}", f"{RED}O(n){RESET}"],
        ["insert", f"{RED}O(n){RESET}", f"{RED}O(n){RESET}"],
        ["remove", f"{RED}O(n){RESET}", f"{RED}O(n){RESET}"],
        ["lookup by index", f"{RED}O(n){RESET}", f"{GREEN}O(1){RESET}"],
        ["lookup by value", f"{RED}O(n){RESET}", f"{RED}O(n){RESET}"]
    ]

    headers = ["Big O", "Linked List", "List"]
    print(tabulate(data, headers))
    print("-" * 15)
    print("Linked List does not have indexes")
    print("Linked List items are not located next to each other in memory. Each item is referencing to next item")
    print("Linked List. Head - first item, tail - last item")


def what_is_node():
    print("-" * 10, "Node", "-" * 10)
    print("- each item in linked list is node")
    print("- node - its value and reference to next item (arrays)")
    print("- linked list - is a collection of nodes/arrays")
    example = {
        "value": 1,
        "next": {
            "value": 2,
            "next": {
                "value": 3,
                "next": None
            }
        }
    }
    print(f"example {example}")

def pop_test():
    print("-" * 10, "MY LINKED LIST LIST - POP TEST", "-" * 10)
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(1)
    my_linked_list.append(5)
    my_linked_list.pop()
    my_linked_list.print_list()

def prepend_test():
    print("-" * 10, "MY LINKED LIST LIST - PREPEND TEST", "-" * 10)
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(1)
    my_linked_list.append(5)
    my_linked_list.prepend(number=0)
    my_linked_list.print_list()

def pop_first_test():
    print("-" * 10, "MY LINKED LIST LIST - POP FIRST TEST", "-" * 10)
    my_linked_list_2 = LinkedList(1)
    my_linked_list_2.append(2)
    print(my_linked_list_2.pop_first())
    print(my_linked_list_2.pop_first())
    my_linked_list_2.print_list()

def get_test():
    print("-" * 10, "MY LINKED LIST LIST - GET TEST", "-" * 10)
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    print(my_linked_list.get(0))

def set_test():
    print("-" * 10, "MY LINKED LIST LIST - SET TEST", "-" * 10)
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.set_index_value(index=1, value=5)
    my_linked_list.print_list()
def insert_test():
    print("-" * 10, "MY LINKED LIST LIST - INSERT TEST", "-" * 10)
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.insert(index=2, value=2)
    my_linked_list.print_list()

def remove_test():
    print("-" * 10, "MY LINKED LIST LIST - REMOVE TEST", "-" * 10)
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.remove(index=2)
    my_linked_list.print_list()

def reverse_test():
    print("-" * 10, "MY LINKED LIST LIST - REVERSE TEST", "-" * 10)
    my_linked_list_reverse = LinkedList(0)
    my_linked_list_reverse.append(1)
    my_linked_list_reverse.append(3)
    my_linked_list_reverse.append(4)
    my_linked_list_reverse.reverse()
    my_linked_list_reverse.print_list()

def find_middle_test():
    print("-" * 10, "MY LINKED LIST LIST - FIND MIDDLE TEST", "-" * 10)
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(3)
    my_linked_list.append(4)
    print(f"middle value: {my_linked_list.find_middle().value}")


def has_loop_test():
    print("-" * 10, "MY LINKED LIST LIST - HAS LOOP TEST", "-" * 10)
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(3)
    my_linked_list.append(4)
    print(f"has loop?: {my_linked_list.has_loop()}")
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.tail.next = my_linked_list.head
    print(f"has loop?: {my_linked_list.has_loop()}")

def find_from_end():
    print("-" * 10, "MY LINKED LIST LIST - FIND FROM END TEST", "-" * 10)
    my_linked_list = LinkedList(0)
    my_linked_list.append(1)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)
    print(find_kth_from_end(my_linked_list, 2).value)


def find_kth_from_end(ll, k):
    """
    return node from the end by specified index
    :param ll: - your linked list
    :param k: - index from end to return
    :return:
    """
    slow = fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == '__main__':
    list_vs_linkedlist()
    what_is_node()

    # My linked list
    pop_test()
    prepend_test()
    pop_first_test()
    get_test()
    set_test()
    insert_test()
    remove_test()
    reverse_test()
    find_middle_test()
    has_loop_test()
    find_from_end()