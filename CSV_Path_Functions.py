from Point import Point
from Path import Path
import numpy as np
import re


def create_point(str_point):
    str_point = str_point.replace("(", "").replace(")", "")

    coordinates = list(map(int, str_point.split(",")))

    point = np.array(coordinates)

    return point


def create_path(str_path):
    str_path = str_path.replace("{", "").replace("}", "")

    str_points = re.findall("\([^\)]*\)", str_path)

    points = np.array([np.array([])])

    for str_point in str_points:
        point = create_point(str_point)
        print("Point " + str(point))
        points[0] = np.append(points, point, axis=0)
        print("Points " + str(points))
        #points = np.vstack((points, point))

    print(points)
    return points


def create_paths(path_array):
    paths = np.array([])

    for path in path_array:
        tmp_path = create_path(path)
        paths = np.append(paths, tmp_path)

    return paths

'''
def create_paths(path_array):
    paths = np.array([])

    for path in path_array:
        tmp_path = create_path(path)
        paths = np.append(paths, tmp_path)

    return paths


def create_path(str_path):
    str_path = str_path.replace("{", "").replace("}", "")

    str_points = re.findall("\([^\)]*\)", str_path)

    points = np.array([])

    for str_point in str_points:
        point = create_point(str_point)
        points = np.append(points, point)

    path = Path(points)

    return path


def create_point(str_point):
    str_point = str_point.replace("(", "").replace(")", "")

    str_coordinates = str_point.split(",")

    point = Point(int(str_coordinates[0]), int(str_coordinates[1]))

    return point
'''