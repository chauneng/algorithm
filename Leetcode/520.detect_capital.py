# 520. Detect Capital
# Easy

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

import re

word = "usa"

# class Solution:
def detectCapitalUse(word:str):
    # Start_with_capital = re.compile('[A-Z]|[a-z]|^[A-Z](?=.[a-z])')
    # return(Start_with_capital.match(word))
    return word.isupper() or word.islower() or word.istitle()

print(bool(detectCapitalUse("UAa")))