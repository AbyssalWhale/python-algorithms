#O(n)
def big_o(n: int):
    for x in range(n):
        print(x)

#O(n^2) - n in square
# Less efficient in comparison to big_o in terms of time complexity
def big_osquare(n: int):
    for x in range(n):
        for y in range(n):
            print(x, y)


if __name__ == '__main__':
    # O(n) - O(10)
    # big_o(n=10)
    big_osquare(n=10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

