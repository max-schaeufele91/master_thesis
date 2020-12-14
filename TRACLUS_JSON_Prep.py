import json
import pandas as pd
import dask.dataframe as dd
from shapely.geometry import LineString

'''
def create_trajectory_list(trajectory):
    trajectory_list = []
    for x, y in list(trajectory.coords):
        point_dict = {
            'x': x,
            'y': y
        }
        trajectory_list.append(point_dict)

    return trajectory_list
'''


def create_point(point: tuple) -> dict:
    return {'x': point[0], 'y': point[1]}


def create_trajectory_list(trajectory):
    trajectory = pd.Series(LineString(trajectory).coords)

    # print('trajectory TYPE | ', type(trajectory))
    # print('trajectory | ', trajectory)

    # print('geo_trajectory TYPE | ', type(geo_trajectory))
    # print('geo_trajectory | ', geo_trajectory)

    trajectory = trajectory.apply(lambda point: create_point(point))

    # print('trajectory_list TYPE | ', type(trajectory_list))
    # print('trajectory_list | ', trajectory_list)
    return trajectory.to_list()


def create_json(trajectories: dd.DataFrame, epsilon=0.00016, min_neighbors=2,
                min_num_trajectories_in_cluster=3, min_vertical_lines=2,
                min_prev_dist=0.0002):

    header = create_head(epsilon, min_neighbors, min_num_trajectories_in_cluster, min_prev_dist, min_vertical_lines)

    '''
    import dask.dataframe as dd
    trajectories_dd = dd.from_pandas(pd.Series(trajectories.geometry), npartitions=8)
    print('trajectories_dd | ', trajectories_dd.head())

    trajectories_list = trajectories_dd.apply(lambda trajectory: create_trajectory_list(trajectory))
    '''

    # print('trajectories.geometry TYPE| ', type(trajectories.geometry))

    trajectories_temp = trajectories.map_partitions(
        lambda trajectory: create_trajectory_list(trajectory))

    import sys
    print('Size trajectories_temp | ', sys.getsizeof(trajectories_temp))
    print('trajectories_temp | ', trajectories_temp.head())

    '''
    trajectories_json = []
    for t in trajectories['geometry_json']:
        trajectories_tmp = json.loads(t)
        trajectories_json.append(trajectories_tmp)
    '''

    trajectories_json = trajectories_temp.to_json(orient='records')
    print('trajectories_json | ', trajectories_json)
    print('Size trajectories_json | ', sys.getsizeof(trajectories_json))

    header.update({'trajectories': trajectories_json})
    print('header.update() complete')

    traclus_json = json.dumps(header, indent=4)
    print('traclus_json complete | ', type(traclus_json))
    
    traclus_json = traclus_json.replace('\\', '')

    return traclus_json

    '''
    trajectories_json = trajectories['geometry'].to_json(orient='records')
    print('trajectories_json complete')

    trajectories_tmp = json.loads(trajectories_json)
    print('trajectories_tmp complete')

    header.update({'trajectories': trajectories_tmp})
    print('header.update() complete')

    traclus_json = json.dumps(header, indent=4)
    print('traclus_json complete')

    return traclus_json
    '''


def create_head(epsilon, min_neighbors, min_num_trajectories_in_cluster, min_prev_dist, min_vertical_lines):
    header = {
        "epsilon": epsilon,
        "min_neighbors": min_neighbors,
        "min_num_trajectories_in_cluster": min_num_trajectories_in_cluster,
        "min_vertical_lines": min_vertical_lines,
        "min_prev_dist": min_prev_dist
    }
    return header


def write_to_file(traclus_json, filename="traclus_trajectories.json"):
    with open("Data/" + filename, 'w+') as f:
        f.write(traclus_json)
