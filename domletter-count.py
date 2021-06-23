#!/usr/bin/python3
import re
import sys


def get_dom_count(word):
    letterCountDict = {}
    for i in range(len(word)):
        letterCountDict[word[i]] = (letterCountDict[word[i]] + 1) if letterCountDict.keys().__contains__(word[i]) else 1
    return max(letterCountDict.values())


file_name = sys.argv[1]
stringWords = open(file_name, 'r').read().lower()
words = re.split('[\n\s]', stringWords)
count = 0
for i in range(len(words)):
    if len(words[i]) > 0:
        if words[i].isalpha():
            count = count + get_dom_count(words[i])

print("Total Count: ", count)
