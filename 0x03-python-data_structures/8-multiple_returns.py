#!/usr/bin/python3
def multiple_returns(sentence):
    """
    returns a tuple containing the length of a string and its first character
    """
    if len(sentence) == 0:
        first_char = None
        mini_sentence = (0, first_char)
        return (mini_sentence)
    mini_sentence = (len(sentence), sentence[0])
    return (mini_sentence)
