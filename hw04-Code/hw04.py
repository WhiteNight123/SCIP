""" Homework 4: Data Abstraction and Trees"""

from math import sqrt
from ADT import make_city, get_name, get_lat, get_lon, tree, label, branches, is_leaf, print_tree

#####################
# Required Problems #
#####################


def couple(lst1, lst2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 5, 6]
    >>> couple(lst1, lst2)
    [[1, 4], [2, 5], [3, 6]]
    >>> lst3 = ['c', 6]
    >>> lst4 = ['s', '1']
    >>> couple(lst3, lst4)
    [['c', 's'], [6, '1']]
    """
    assert len(lst1) == len(lst2)
    "*** YOUR CODE HERE ***"
    return [[lst1[i], lst2[i]] for i in range(len(lst1))]


def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    "*** YOUR CODE HERE ***"
    return sqrt((get_lat(city1) - get_lat(city2)) ** 2 + (get_lon(city1) - get_lon(city2)) ** 2)


def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    tmp_city = make_city('tmp', lat, lon)
    return get_name(city1) if distance(city1, tmp_city) < distance(city2, tmp_city) else get_name(city2)


def nut_finder(t):
    """Returns True if t contains a node with the value 'nut' and
    False otherwise.

    >>> scrat = tree('nut')
    >>> nut_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('nut')]), tree('branch2')])
    >>> nut_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> nut_finder(numbers)
    False
    >>> t = tree(1, [tree('nut',[tree('not nut')])])
    >>> nut_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    if label(t) == 'nut':
        return True
    for b in branches(t):
        if nut_finder(b):
            return True
    return False


def sprout_leaves(t, values):
    """Sprout new leaves containing the data in values at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if not branches(t):
        return tree(label(t), [tree(i) for i in values])
    return tree(label(t), [sprout_leaves(s, values) for s in branches(t)])


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    # 当t1和t2至少有一个为子节点
    if is_leaf(t1) or is_leaf(t2):
        return tree(label(t1) + label(t2), branches(t2) + branches(t1))
    else:
        new_branches = []
        # 当t1和t2都有分支时，递归调用
        for i in range(min(len(branches(t1)), len(branches(t2)))):
            new_branches += [add_trees(branches(t1)[i], branches(t2)[i])]
        # 多余的分支补充在后面
        for i in range(min(len(branches(t1)), len(branches(t2))), max(len(branches(t1)), len(branches(t2)))):
            if len(branches(t1)) > len(branches(t2)):
                new_branches += [branches(t1)[i]]
            else:
                new_branches += [branches(t2)[i]]
    return tree(label(t1) + label(t2), new_branches)


def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    return (1 if label(t) >= n else 0) + sum([bigpath(b, n - label(t)) for b in branches(t)])


def bigger_path(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    return bigpath(t, n) + sum([bigger_path(b, n) for b in branches(t)])

##########################
# Just for fun Questions #
##########################


def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return base_func(label(t))
    return merge_func(label(t), [fold_tree(b, base_func, merge_func) for b in branches(t)])


def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, lambda _: 1, lambda _, vs: sum(vs))


def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, lambda v: v, lambda v, vs: v + sum(vs))


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, lambda v: [v], lambda v, vs: sum(vs, [v]))


def has_int(tree, i):
    """Return if an integer is contained in a tree

    >>> has_int(tree(1, [tree(2, tree(3)), tree(4)]), 1)
    True
    >>> has_int(tree(1, [tree(2, tree(3)), tree(4)]), 5)
    False
    """
    return label(tree) == i or any([has_int(b) for b in branches(tree)])


def has_int(tree, i):
    """Return if an integer is contained in a tree

    >>> has_int(tree(1, [tree(2, [tree(3)]), tree(4)]), 1)
    True
    >>> has_int(tree(1, [tree(2, [tree(3)]), tree(4)]), 5)
    False
    """

    def base_func(l):
        return lambda i: l == i

    def merge_func(l, bs):
        return lambda i: l == i or any([b(i) for b in bs])

    return fold_tree(tree, base_func, merge_func)(i)


def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'

    def base_func(l):
        return lambda word: len(word) == 1 and l == word[0]

    def merge_func(l, bs):
        return lambda word: len(word) == 1 and l == word[0] or l == word[0] and any([b(word[1:]) for b in bs])

    return fold_tree(t, base_func, merge_func)(word)
