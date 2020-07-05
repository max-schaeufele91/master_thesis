import unittest
import numpy as np
import Path_to_TRACLUS_JSON as pj
import CSV_Path_Functions as pf


class MyTestCase(unittest.TestCase):
    def test_create_header(self):
        json_header = pj.create_header()

        self.assertTrue("\"epsilon\": 0.00016" in json_header, "epsilon incorrect")
        self.assertTrue("\"min_neighbors\": 2" in json_header, "min_neighbors incorrect")
        self.assertTrue("\"min_num_trajectories_in_cluster\": 3" in json_header,
                        "min_num_trajectories_in_cluster incorrect")
        self.assertTrue("\"min_vertical_lines\": 2" in json_header, "min_vertical_lines incorrect")
        self.assertTrue("\"min_prev_dist\": 0.0002" in json_header, "min_prev_dist incorrect")

    def test_create_trajectories(self):
        paths = self.create_paths()

        json_trajectories = pj.create_trajectories(paths)

        self.assertTrue("\"trajectories\":" in json_trajectories, "Not init as trajectories")
        self.assertTrue("\"x\": 107096" in json_trajectories, "First X incorrect")
        self.assertTrue("\"y\": 18237" in json_trajectories, "First Y incorrect")

    def test_create_traclus_json(self):
        traclus_json = pj.create_traclus_json(pj.create_header(), pj.create_trajectories(self.create_paths()))

        self.assertTrue("\"epsilon\": 0.00016" in traclus_json, "epsilon incorrect")
        self.assertTrue("\"min_neighbors\": 2" in traclus_json, "min_neighbors incorrect")
        self.assertTrue("\"min_num_trajectories_in_cluster\": 3" in traclus_json,
                        "min_num_trajectories_in_cluster incorrect")
        self.assertTrue("\"min_vertical_lines\": 2" in traclus_json, "min_vertical_lines incorrect")
        self.assertTrue("\"min_prev_dist\": 0.0002" in traclus_json, "min_prev_dist incorrect")

        self.assertTrue("\"trajectories\":" in traclus_json, "Not init as trajectories")
        self.assertTrue("\"x\": 107096" in traclus_json, "First X incorrect")
        self.assertTrue("\"y\": 18237" in traclus_json, "First Y incorrect")

    @staticmethod
    def create_paths():
        paths_array = np.array(
            ["{\"(107096,18237)\",\"(16127,19080)\",\"(105253,2054)\",\"(10136,2318)\",\"(10362,2448)\"}",
             "{\"(207096,1837)\",\"(10617,1980)\",\"(10253,20554)\",\"(10516,23198)\",\"(103262,2448)\"}",
             "{\"(307096,1237)\",\"(10612,1908)\",\"(15253,2554)\",\"(10513,2398)\",\"(10262,2448)\"}"])
        paths = pf.create_paths(paths_array)
        return paths


if __name__ == '__main__':
    unittest.main()
