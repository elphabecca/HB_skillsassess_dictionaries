"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # SOLUTION 1:
    phrase = phrase.split()
    word_count_dict = {}

    for word in phrase:
        word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict 


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_dict = {"Watermelon" : 2.95,
                  "Cantaloupe" : 2.50,
                  "Musk" : 3.25,
                  "Christmas" : 14.25}


    # The title() method will ensure the user doesn't create a new key if they 
    # spell the name of the melon correctly but don't use proper capitalization.
    return melon_dict.get(melon_name.title(), "No price found")


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    # Create the dictionary:
    len_dict = {}

    # Fill the dictionary:
    for word in words:
        len_dict[len(word)] = len_dict.get(len(word), [])
        len_dict[len(word)].append(word)

    # Sort the word lists (values)
    for value in len_dict.values():
        value.sort()

    # Return a list of tuples ordered by word-length
    return sorted(len_dict.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_to_pirate_dictionary = {"sir" : "matey",
                                    "hotel" : "fleabag inn",
                                    "student" : "swabbie",
                                    "man" : "matey",
                                    "professor" : "foul blaggart",
                                    "restaurant" : "galley",
                                    "your" : "yer",
                                    "excuse" : "arr",
                                    "students" : "swabbies",
                                    "are" : "be",
                                    "restroom" : "head",
                                    "my" : "me",
                                    "is" : "be"}

    words = phrase.split()
    pirate_text = ""

    # A loop which replaces the english word with the pirate word, if one exists.
    for word in words:
        pirate_text += english_to_pirate_dictionary.get(word, word) + " "

    return pirate_text.rstrip()


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    names_back = [names[0]]
    del names[0]

    kid_dict = {name : name[0] for name in names}

    for i in range(len(names)):
        letter_up = names_back[-1][-1]
        next_words = [name for name in names if kid_dict[name] == letter_up]
        if next_words == []:
            return names_back
        names_back.append(next_words[0])
        names.remove(next_words[0])


    return names_back

    # DICT SOLUTION:
    """This was my first solution -- overcomplicated."""

    # kid_dict = {}
    # return_text = [names[0]]

    # # Fill a kid_dict based on the names being played with
    # for name in names[1:]:
    #     kid_dict[name] = kid_dict.get(
    #         name, {"start_letter" : name[0], "last_letter" : name[-1]})
    
    # # Find the next word & remove it once used
    # for i in range(len(names)):
    #     letter_up = return_text[i][-1]
    #     options = [key for key, mini_dict in kid_dict.items()
    #         if kid_dict[key]["start_letter"] == letter_up]
    #     if options == []:
    #         return return_text
    #     new_word = options.pop()
    #     return_text.append(new_word)
    #     del kid_dict[new_word]

    # return return_text

    

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
