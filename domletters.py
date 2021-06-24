#!/usr/bin/python3
import sys
import re


def get_dom_count(word):
    """
    :param word: one single word from given input text file.
    :type word: str
    :return: This function returns the maximum count of a letter in a given ASCII word.
    :rtype: int
    """
    letterCountDict = {}
    for w in range(len(word)):
        letterCountDict[word[w]] = (letterCountDict[word[w]] + 1) if letterCountDict.keys().__contains__(word[w]) else 1
    return max(letterCountDict.values())


if __name__ == "__main__":
    for line in sys.stdin:
        stringWords = open(line.rstrip('\n'), 'r').read().lower()
        words = re.split('[\n\\s]', stringWords)
        count = 0
        for i in range(len(words)):
            if len(words[i]) > 0:
                if words[i].isalpha():  # https://www.geeksforgeeks.org/python-string-isalpha-application/
                    count = count + get_dom_count(words[i])

        print("Total dominant letters Count: ", count)
        break
