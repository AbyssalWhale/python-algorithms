#O(n) - propoprtional
def big_o(n: int):
    for x in range(n):
        print(x)


#O(n^2) - loop withing loop - n in square
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


# 0(1) - constant - case when N is increasing but the number of operations stays the same aka constant time.
# It does not matter if we have more sum operations like: n + n + n + etc
# This is the most efficient Big O as N increases but number of operations static.
def big_o_of_one(n: int):
    return n + n


# Different terms for input when func has 2 params - it cannot be marked as O(n) because 2 params
# and not clear which param is n - a or b?
# This func is marked as O(a + b)
def big_o_different_term_sum(a: int, b: int):
    # O(n)
    for x in range(a):
        print(a)
    # O(n)
    for y in range(b):
        print(a)


# This func is marked as O(a + b) - because 1 loop is nested
def big_o_different_term_multiply(a: int, b: int):
    # O(n)
    for x in range(a):
        print(a)
        for y in range(b):
            print(a)


# Big O list - O(n) is number of items in list/array O(1) - operation can be marked when we add/remove item to end of
# list. O(n) - operation can be marked when we add/remove item to beginning/middle of list as we are changing sequence -
# indexes needs to be updated as well. So more operations
def big_0_list(number: int):
    my_list = [1, 2, 3, 4]
    my_list.append(number)


if __name__ == '__main__':
    # O(n) - O(10)
    # big_o(n=10)
    big_osquare(n=10)
    big_osquare(n=10)
    big_o_of_one(n=2)
    big_o_different_term_sum(a=1, b=3)
    big_o_different_term_multiply(a=1, b=3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
