import unittest
import randata
import copy
from multi_sort import * 

class SortTestCase(unittest.TestCase):

    def testMultiMethods(self):
        for x in range(-1, 100):

            arr = randata.get_randata(x)

            arr1 = copy.copy(arr)
            arr2 = copy.copy(arr)
            arr3 = copy.copy(arr)

            t1 = bubble_sort(arr1)
            t2 = insert_sort1(arr2)
            t3 = insert_sort2(arr3)

            for y in range(0, x-1):
                self.failUnless(t1[y] <= t1[y+1])
                self.failUnless(t2[y] <= t2[y+1])
                self.failUnless(t3[y] <= t3[y+1])


if __name__ == '__main__':
    unittest.main()
