import unittest
import CSV_Path_Functions as pf
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_create_point(self):
        str_point = "(123,456)"
        point = pf.create_point(str_point)

        self.assertEqual(point.x, 123, "X isn't correct")
        self.assertEqual(point.y, 456, "Y isn't correct")

    def test_create_path(self):
        str_path = "'{\"(107096,18237)\",\"(106127,19080)\",\"(105253,20554)\",\"(105136,23198)\",\"(103262,24448)\"}'"
        path = pf.create_path(str_path)

        self.assertEqual(path.points[0].x, 107096, "X isn't correct")
        self.assertEqual(path.points[0].y, 18237, "Y isn't correct")

    def test_create_paths(self):
        paths_array = np.array(["{\"(107096,18237)\",\"(16127,19080)\",\"(105253,2054)\",\"(10136,2318)\",\"(10362,2448)\"}",
                                "{\"(207096,1837)\",\"(10617,1980)\",\"(10253,20554)\",\"(10516,23198)\",\"(103262,2448)\"}",
                                "{\"(307096,1237)\",\"(10612,1908)\",\"(15253,2554)\",\"(10513,2398)\",\"(10262,2448)\"}"])

        paths = pf.create_paths(paths_array)

        self.assertEqual(paths[0].points[0].x, 107096, "X isn't correct")
        self.assertEqual(paths[0].points[0].y, 18237, "Y isn't correct")

if __name__ == '__main__':
    unittest.main()
