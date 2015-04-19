
    # For example:

    #     >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
    #     [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

def adv_word_length_sorted_words(words):


    word_length_dict = {}
    word_length_list = []

    for word in words:
        word_length_dict.setdefault(len(word), []) # for each word in list of words, adds its length to word_length_dict dictionary with empty list
                                                   # as value; if already in dictionary, no changes made (returns value)
        word_length_dict[len(word)].append(word)   # for each word in list of words, appends the word to the value list belonging to the key
                                                    # that is the length of the word

    for length in word_length_dict.keys(): # iterates through a list of word lengths, the word_length_dict keys (word_length_dict.keys())
        word_tuple = (length, sorted(word_length_dict[length]))  # for each length, Python finds it in word_length_dict and makes a tuple of two things:
                                                         # the length, and a SORTED copy of the list of the words of that length
        word_length_list.append(word_tuple)              # appends the tuple to word_length_list 

    print sorted(word_length_list)           

adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])