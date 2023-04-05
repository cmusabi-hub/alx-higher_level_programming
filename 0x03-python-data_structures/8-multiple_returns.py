#!/usr/bin/python3


def multiple_returns(sentence):
    string = ()
    if sentence == None:
        return (0, None)
    else:
        string = len(sentence), sentence[0]
    return string
