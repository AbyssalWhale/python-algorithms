from tabulate import tabulate

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



if __name__ == '__main__':
    list_vs_linkedlist()
    what_is_node()
