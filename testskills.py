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
        if word in pirate_translations:
            translated_words.append(pirate_translations[word])
        else:
            translated_words.append(word)

    print " ".join(translated_words)





pirate_talk("my student is not a man")