## -*- coding: utf-8 -*-
import re

def maintest(scheme, arr):
    for i in range(1, len(arr)):
        if re.search('([А-Яа-я]*)( \d){3}$', re.sub("^\s+|\n|\r|\s+$", '', arr[i])):
            v = re.search('([А-Яа-я]*)( \d){3}$', re.sub("^\s+|\n|\r|\s+$", '', arr[i])).group(0)
        else:
            return([0, 'Not all lines match the pattern, stop the program!'])
        b = re.sub("^\s+|\n|\r|\s+$", '', arr[i])
        if v != b:
            return([0, 'Not all lines match the pattern, stop the program!'])
    return([1, 'Check input data successfully finished!'])
