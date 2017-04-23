""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import re


def get_word_list(file_name, n):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    text = f.read()
    words = re.compile('\w+').findall(text)
    return get_top_n_words(words, n)


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    words = []

    # Change all words to lowercase
    for word in word_list:
        word = str.lower(word)
        if word not in words:
            words.append(word)

    # Calculate frequency of each word
    frequency = []
    for word in words:
        word_count = 0
        for test in word_list:
            if word == test:
                word_count += 1
        frequency.append(word_count)

    dic = dict()
    for i, word in enumerate(words):
        dic[frequency[i]] = word

    # Sort dictionary to return ranks
    keys = dic.keys()
    keys = sorted(keys)
    words_ranked = []
    for key in keys:
        words_ranked.append(dic.get(key))
    words_ranked = words_ranked[::-1]
    words_ranked = words_ranked[:n]
    return words_ranked


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(get_word_list('huckfin.txt', 5))
    # print(string.punctuation)
