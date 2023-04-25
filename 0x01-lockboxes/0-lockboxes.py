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
    num_boxes = len(boxes)
    visited = set()
    stack = [0]  # start with box 0
    
    while stack:
        box = stack.pop()
        visited.add(box)
        for key in boxes[box]:
            if key < num_boxes and key not in visited:
                stack.append(key)
    
    return len(visited) == num_boxes
