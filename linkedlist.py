from tabulate import tabulate

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def list_vs_linkedlist():
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
    print("-" * 10)
    print("Linked List does not have indexes")
    print("Linked List items are not located next to each other in memory. Each item is referencing to next item")
    print("Linked List. Head - first item, tail - last item")


if __name__ == '__main__':
    # O(n) - O(10)
    # big_o(n=10)
    list_vs_linkedlist()
