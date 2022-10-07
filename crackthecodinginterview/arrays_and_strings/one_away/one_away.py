#!/usr/bin/python3

def check_replacement(ch_1, ch_2):
    """ check if a replacement will make the strings same """
    if (len(ch_1) != len(ch_2)):
        return None
    for i in range(0, len(ch_1)):
        if ch_1[i] != ch_2[i]:
          # difference found
          x = [c for c in ch_2]
          x[i] = ch_1[i]
          s = ''.join(x)
          if ch_1 != s:
            return False
          else: 
            return True 

def one_away(ch_1, ch_2):
    """ one away """
    # there is more than one edit away
    if (len(ch_1) - len(ch_2) > 1):
        return False
    if (len(ch_1) == len(ch_2)):
        r = check_replacement(ch_1, ch_2)
        return r
    if (len(ch_1) - len(ch_2) == 1):
        r = check_replacement(ch_1, ch_2)
        if (r != None):
            return False
    return True
