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


# Drop Non Dominance
# Operations can be calculated as: O(n^2) + O(n) OR O(n^2 + n).
# n^2 - is dominante term and n - is not.
# As second n can become large with time and have it stand alone does not make any sense, and
# it can be dropped.
def big_o_nondominance(n: int):
    #O(n^2)
    for x in range(n):
        for y in range(n):
            print(x, y)
    # O(n)
    for a in range(n):
        print(a)


# 0(1) - case when N is increasing but the number of operations stays the same aka constant time.
# It does not matter if we have more sum operations like: n + n + n + etc
# This is the most efficient Big O as N increases but number of operations static.
def big_o_of_one(n: int):
    return n + n


if __name__ == '__main__':
    # O(n) - O(10)
    # big_o(n=10)
    big_osquare(n=10)
    big_osquare(n=10)
    big_o_of_one(n=2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
