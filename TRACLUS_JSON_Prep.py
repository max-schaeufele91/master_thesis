import json
import geopandas as gpd
import pandas as pd


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
    geo_trajectory = gpd.GeoSeries(trajectory.coords)

    #print('trajectory TYPE | ', type(trajectory))
    #print('trajectory | ', trajectory)

    #print('geo_trajectory TYPE | ', type(geo_trajectory))
    #print('geo_trajectory | ', geo_trajectory)

    trajectory_list = geo_trajectory.apply(lambda point: create_point(point))

    #print('trajectory_list TYPE | ', type(trajectory_list))
    #print('trajectory_list | ', trajectory_list)
    return trajectory_list.to_list()


def create_json(trajectories: gpd.GeoDataFrame, epsilon=0.00016, min_neighbors=2,
                min_num_trajectories_in_cluster=3, min_vertical_lines=2,
                min_prev_dist=0.0002):
    header = {
        "epsilon": epsilon,
        "min_neighbors": min_neighbors,
        "min_num_trajectories_in_cluster": min_num_trajectories_in_cluster,
        "min_vertical_lines": min_vertical_lines,
        "min_prev_dist": min_prev_dist
    }

    '''
    import dask.dataframe as dd
    trajectories_dd = dd.from_pandas(pd.Series(trajectories.geometry), npartitions=8)
    print('trajectories_dd | ', trajectories_dd.head())

    trajectories_list = trajectories_dd.apply(lambda trajectory: create_trajectory_list(trajectory))
    '''

    trajectories_list = trajectories.geometry.progress_apply(lambda trajectory: create_trajectory_list(trajectory))

    print('trajectories_list TYPE| ', type(trajectories_list))
    print('trajectories_list SHAPE| ', trajectories_list.shape)
    print('trajectories_list | ', trajectories_list.head())

    trajectories_json = trajectories_list.to_json(orient='records')

    trajectories_tmp = json.loads(trajectories_json)

    header.update({'trajectories': trajectories_tmp})

    traclus_json = json.dumps(header, indent=4)

    return traclus_json


def write_to_file(traclus_json, filename="traclus_trajectories.json"):
    with open("Data/" + filename, 'w+') as f:
        f.write(traclus_json)