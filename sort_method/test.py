import unittest
import randata
import copy
from sort_methods import * 

class methodsTestCase(unittest.TestCase):

    def testSortMethods(self):
        for count in range(-1, 100):

            arr = randata.get_randata(count)

            rs = [
                bubble_sort(copy.copy(arr)),
                insert_sort_0(copy.copy(arr)),
                insert_sort_1(copy.copy(arr)),
                shell_sort_0(copy.copy(arr)),
                shell_sort_1(copy.copy(arr)),
            ]

            for a in rs:
                for x in range(0, count-1):
                    self.failUnless(a[x] <= a[x+1])


if __name__ == '__main__':
    unittest.main()
