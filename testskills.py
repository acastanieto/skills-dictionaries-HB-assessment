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
        word_length_dict.setdefault(len(word), []) # for each word in list of words, adds its lenght to word_length_dict dictionary with empty list
                                                   # as value; if already in dictionary, no changes made (returns value)
        word_length_dict[len(word)].append(word)   # for each word in list of words, appends the word to the value list belonging to the key
                                                    # that is the length of the word

    for length in word_length_dict.keys(): # iterates through a list of word lengths, the word_length_dict keys (word_length_dict.keys())
        word_tuple = (length, word_length_dict[length])  # for each length, Python finds it in word_length_dict and makes a tuple of
                                                         # the length and a list of the words of that length
        word_length_list.append(word_tuple)              # appends the tuple to word_length_list 

    return sorted(word_length_list)                      # returns a sorted copy of word_length_list

word_length(["ok", "an", "apple", "a", "day"])