#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",")

    i = 0
    num_col = None
    mark_col = None

    for head in headings:
        if head == "Student Number":
            num_col = i
        elif head == "Mark":
            mark_col = i
        i += 1
        
    return (num_col, mark_col)

def findTop(f, num_col, mark_col):
    ''' finds the top student in the class '''
    best = -1
    best_idx = None

    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])  
        if mark > best: 
            best = mark  
            best_idx = data[num_col]  
    
    return best_idx, best  

# Make sure this block is indented
if __name__ == "__main__":
    f = open(sys.argv[1])
    num_col, mark_col = getCols(f)
    best_idx, best = findTop(f, num_col, mark_col)
    print("The top student was student %s with %d" % (best_idx, best))

