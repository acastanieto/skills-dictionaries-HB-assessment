# To work on the advanced problems, set to True
ADVANCED = False

from collections import Counter

def count_unique(string1):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    return Counter(string1.split(" ")) # Split string into list, create a Counter from list.




def common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    dict = {}
    new_list = []

    for num in list1:            # iterates through the list1
        dict.setdefault(num, []) # add nums to dictionary (dict) as key and set value to [] (empty list); if 
                                 # key already in dictionary, then no changes made (value returned)
        dict[num].append(num)    # append num to list that is the value of the num key
    for num in list2:                # iterates through list2   
        dict.setdefault(num, [])     # if num not a key in the dictionary, adds num and sets value to [] 
        new_list.extend(dict[num])   # for each time num is in list2, if it is already in the dictionary, extends new_list by the value
    return new_list


def unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `common_items`, this should find [1, 2]:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    set1 = set(list1)
    set2 = set(list2)

    return list(set1 & set2) # created sets from list1 and list2 and used set math operator & to find unique common numbers


def sum_zero(list1):
    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    all_sums = set()

    for index, num in enumerate(list1):     # for each num in list1:
        for next_num in list1[index + 1:]:  # the sum of the num and each number after it (next_num) is found (on next line)
            sum = num + next_num            # here the sum of num and next_num is found
            if sum == 0:                    # then each sum is checked to see if == 0, and if so...
                all_sums.add(tuple(sorted([num, next_num])))  # num and next_num are made into a list.  A tuple of the sorted version 
                                                              # of this list is then added to the all_sums set to get rid of duplicate
                                                              # tuples.  (Note:  the number pairs are 1st sorted so that, for example,
                                                              # (1, -1) and (-1, 1) aren't treated as two unique pairs)

    return list(all_sums) # to return a list, a list is made of the all_sums set and that is what is returned







def find_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(find_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(find_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    return set(words) # a set is made of the input list of words.  This gets rid of any duplicate words.


def word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    word_length_dict = {}
    word_length_list = []

    for word in words:
        word_length_dict.setdefault(len(word), []) # for each word in list of words, adds its length to word_length_dict dictionary with empty list
                                                   # as value; if already in dictionary, no changes made (returns value)
        word_length_dict[len(word)].append(word)   # for each word in list of words, appends the word to the value list belonging to the key
                                                    # that is the length of the word

    for length in word_length_dict.keys(): # iterates through a list of word lengths, the word_length_dict keys (word_length_dict.keys())
        word_tuple = (length, word_length_dict[length])  # for each length, Python finds it in word_length_dict and makes a tuple of two things:
                                                         # the length, and a list of the words of that length
        word_length_list.append(word_tuple)              # appends the tuple to word_length_list 

    return sorted(word_length_list)                      # returns a sorted copy of word_length_list


def pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    # Approach:  first make a dictionary of English:Pirate key:value pairs.  Then make a list of the words of the input string, then iterate through the list.  For each word in the list, find it in the dictionary and add its value to a new_list.  Be sure to add condition statement if word not in dictionary. Lastly, join the words in the new_list.

def pirate_talk(phrase):
    # Approach:  first make a dictionary of English:Pirate key:value pairs.  Then make a list of the words of the input string, then iterate through the list.  For each word in the list, find it in the dictionary and add its value to a new_list.  Be sure to add condition statement if word not in dictionary. Lastly, join the words in the new_list.

    pirate_translations = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "boy": "matey",
        "madam": "proud beauty",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "lawyer": "foul blaggart",
        "the": "th'",
        "restroom": "head",
        "my": "me",
        "hello": "avast",
        "is": "be",
        "man": "matey"
    } # dictionary of english:pirate translations as key:value pairs

    translated_words = [] # initialize empty list for the translated words to go into
    english_words = phrase.split(" ") # make list of the words of the english input string

    for word in english_words: 
       
        if word in pirate_translations: # first checks if word is in the pirate dictionary
            translated_words.append(pirate_translations[word]) # if it is, the value of that word, which is the translated pirate word, is 
                                                               # appended to the translated_words list
        else:
            translated_words.append(word)                      # if it isn't in the pirate dictionary, the (untranslated) word is added to the
                                                               # translated_words list

    return " ".join(translated_words)                           # a string of the joined words of translated_words list is returned

# def adv_word_length_sorted_words(words):
#     """Given list of words, return list of ascending [(len, [sorted-words])].
#
#     Given a list of words, return a list of tuples, ordered by word-length.
#     Each tuple should have two items--the length of the words for that
#     word-length, and the list of words of that word length. The list of words
#     for that length should be sorted alphabetically.
#
#     For example:
#
#         >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
#         [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
#
#     """
#
#     return []


# ##############################################################################
# You can ignore everything after here

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
