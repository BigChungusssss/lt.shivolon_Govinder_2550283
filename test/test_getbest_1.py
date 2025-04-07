#!/usr/bin/env python3code

import unittest
import getbest 
from io import StringIO


class TestStudentTopMark(unittest.TestCase):

    def test_getCols(self):
        file = StringIO("Course,Student Number,Mark,Comment\
ELEN3020,160001,72,OK\
ELEN3020,167381,90,Check\
ELEN3020,143211,83,-\
ELEN3020,17171,48,Redo\
ELEN3020,191919,73,-\n")
        num_col, mark_col = getbest.getCols(file)
        self.assertEqual(num_col, 1)
        self.assertEqual(mark_col, 3)

    def test_findTop(self):
        
        file = StringIO("Course,Student Number,Mark,Comment\
ELEN3020,160001,72,OK\
ELEN3020,167381,90,Check\
ELEN3020,143211,83,-\
ELEN3020,17171,48,Redo\
ELEN3020,191919,73,-\n")
        num_col, mark_col = getbest.getCols(file)
        best_idx, best = getbest.findTop(file, num_col, mark_col)
        self.assertEqual(best_idx, "1002")
        self.assertEqual(best, 92)

if __name__ == '__main__':
    unittest.main()
