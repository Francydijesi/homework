# To work on the advanced problems, set to True
ADVANCED = True
from operator import itemgetter


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


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
    word_dict = {}
    words = input_string.strip().split()

    for word in words:
        if word in word_dict:
           word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in at least one list and is present
    in both lists, return it each time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    common_items = []

    for item1 in list1:
        for item2 in list2:
            if item2 == item1:
               common_items.append(item2)

    return common_items


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """
    # return list(set(find_common_items(list1,list2)))
    return [x for x in list1 if x in list2]



def get_sum_zero_pairs(input_list):
    """Given a list of numbers, return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
######################
# Solution n.1
######################
    dic = {}
    words_couple = []

    for num in input_list:

        # Searchs for the opposite number of num in the input_list
        opposites = filter(lambda x: x + num == 0, input_list)
        if opposites:
            words_couple.append(tuple(sorted([num, opposites[0]])))

    # It returns a list of unique tuples
    return dic.fromkeys(words_couple).keys()

########################
# Solution n.2
########################
    # dic = {}
    # couple_list = []

    # couple_words = [(x, y) for x in input_list for y in input_list if x + y == 0]
    # for couple in couple_words:
    #     couple_list.append(tuple(sorted(couple)))
    # return dic.fromkeys(couple_list).keys()

########################
# Solution n.3
########################

    # dic = {}
    # couple_words = []
    # input_list.sort()
    # for num in input_list:
    #     for x in input_list:
    #         if x + num == 0:
    #             if (num, x) not in couple_words:
    #                couple_words.append(tuple(sorted([num, x])))
    # return dic.fromkeys(couple_words).keys()

def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    Do this without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """
    return dict.fromkeys(words).keys()



def encode(phrase):
    """Given a phrase, return the encoded string.

    Replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u".

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    return phrase.replace('e', 'p').replace('a', 'd').replace('t', 'o').replace('i', 'u')

def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    dic = {}
    sorted_len_word = []

    # Generates a dictionary {1:['a'], 2:['ok','an'] ...} from list of words
    for word in words:
        if len(word) not in dic.keys():
           dic[len(word)] = [word]
        if word not in dic[len(word)]:
           dic[len(word)].append(word)

    # Generates a list of tuple [(1,['a']),(2,['ok','an']) ...] from dictionary
    for num, word in dic.items():
        sorted_len_word.append((num,word))

    # Returns list of tuple sorted by key = length of words
    return sorted(sorted_len_word, key=itemgetter(0))



def get_pirate_talk(phrase):
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

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
   # Create a dictionary from two lists
    keys = ['sir', 'hotel', 'student', 'boy', 'madam', 'professor', 'restaurant',
            'your', 'excuse', 'students', 'are', 'lawyer', 'the', 'restroom',
            'my', 'hello', 'is', 'man']
    values = ['matey', 'fleabag', 'swabbie', 'matey', 'proud beauty',
              'foul blaggart', 'galley', 'yer', 'arr', 'swabbies', 'be',
              'foul blaggart', 'th\'', 'head', 'me', 'avast', 'be', 'matey']
    pirate_dict = dict(zip(keys, values))

   # Replaces english words in phrase with pirate words from the dictionary
    words = phrase.split()
    for i in range(len(words)):
        if words[i] in pirate_dict:
            words[i] = pirate_dict[words[i]]

    return " ".join(words)

# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    For example:
        >>> adv_get_top_letter("La pecora nel bosco.")
        ['o']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    # ####################
    # Solution n.1
    ######################

    # max_count = 0
    # letter = []

    # input_string = input_string.lower().replace(" ", "")

    # for l in input_string:
    #     num_letter = input_string.count(l)
    #     if max_count < num_letter:
    #         max_count = num_letter
    #         letter = [l]
    #     elif max_count == num_letter and l not in letter:
    #         letter.append(l)

    # return letter
    
    ########################
    # Solution n.2
    #######################

    dic = {}

    # Lower the case in the string
    input_string = input_string.lower().replace(" ", "")

    # Get a set of the unique letters
    uniques = set(input_string)

    # Creates a list of tuples (count, letter): [(1, l),(3, a),...]
    let_count_tuples = map(lambda x: (input_string.count(x), x), uniques)

    # Creates a dictionary with the list of tuples: {1:['l'], 3: ['e','a'], ...}
    for let_count_tuple in let_count_tuples:

        # Check if key is already in the dictionary
        if let_count_tuple[0] not in dic.keys():
            # If key not in the dictionary, it creates a new key-value key
            dic[let_count_tuple[0]] = [let_count_tuple[1]]
        else:
            dic[let_count_tuple[0]].append(let_count_tuple[1])
    # First sort the dictionary by key (=count) in descending order
    # Then returns the value of the first key, which represent the max count
    return dic[sorted(dic.keys(), reverse=True)[0]]


def adv_alpha_sort_by_word_length(words):
    """Given a list of words, return a list of tuples, ordered by word-length.

    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """
    dic = {}
    sorted_list = []

    for word in sorted(words):
        if len(word) not in dic:
            dic[len(word)] = [word]
        if word not in dic[len(word)]:
            dic[len(word)].append(word)

    for key, value in dic.items():
        sorted_list.append((key, value))

    # return sorted(sorted_list, itemgetter(1))
    return sorted_list

##############################################################################
# You can ignore everything below this.

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
