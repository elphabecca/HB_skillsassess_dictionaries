"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # SOLUTION 1: This made the test work, but technically returned a set, not a list.
    # Sets are a unique collection
    # return set(words)

    #SOLUTION 2:
    return [word for word in set(words)]


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    # Use sets to find the intersection of the items, 
    # then return a list of that intersection
    return list(set(items1) & set(items2))

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    # SOLUTION DICT:
    # pair_dict = {}

    # for num in numbers:
    #     if -num in numbers:
    #         # The following line makes sure I don't end up with duplicate keys (ie 2 and -2)
    #         num = max(num, -num)
    #         pair_dict[-num] = num

    # return [pair for pair in pair_dict.items()]

    # SOLUTION DICT2:
    pair_dict = {-x:x for x in numbers if -x in numbers and x >= -x}

    return [[key, value] for key, value in pair_dict.items()]

    # SOLITION 1: 
    # pair_list = []

    # for num in numbers:
    #     if -num in numbers:
    #         # you have to make the pairs tuples so they're hashable for when you put them into a set
    #         pair = tuple(sorted([num, -num]))
    #         pair_list.append(pair)

    # return [list(pair) for pair in set(pair_list)]

    # SOLUTION 2:
    # tuple_list = []

    # # Same idea as above, but with a nested for loop!
    # for num in numbers:
    #     for numnum in numbers:
    #         if num + numnum == 0:
    #             tuple_list.append(tuple(sorted((num, numnum))))

    # return [list(pair) for pair in set(tuple_list)]

    # SOLUTION 3:
    # tuple_list = [tuple(sorted((x, y))) for x in numbers for y in numbers if x+y==0]

    # return [list(pair) for pair in set(tuple_list)]   

    # Not going to lie, I was REALLY surprised when the double for loop worked in the comprehension.
    # It was around this time I had the brilliant idea to start with an empty dictionary intead of an empty list.


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    # This will take out spaces but also make sure all characters are lowercase (for equal counting)
    phrase = "".join(phrase.lower().split())

    letter_count = {}

    for letter in phrase:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    # This variable identifies the maximum letter occurences
    num_of_max_occurences = max(letter_count.values())
    
    return sorted([letter for letter in letter_count
        if letter_count[letter] == num_of_max_occurences])

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
