#!/usr/bin/python3
'''Module to return n number of locked boxes'''

def canUnlockAll(boxes):
     '''
    Locked boxes
    Args:
      boxes is a list of lists
    Returns:
      True if all boxes can be opened, else return False
    '''
    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
     if len(keys) == len(boxes):
        return True
    return False
