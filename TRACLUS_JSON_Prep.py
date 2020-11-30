import json
import geopandas as gpd


def create_trajectory_list(trajectory):
    trajectory_list = []
    for x, y in list(trajectory.coords):
        point_dict = {
            'x': x,
            'y': y
        }
        trajectory_list.append(point_dict)

    return trajectory_list


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

    trajectories_list = trajectories.geometry.apply(lambda trajectory: create_trajectory_list(trajectory))

    trajectories_json = trajectories_list.to_json(orient='records')

    trajectories_tmp = json.loads(trajectories_json)

    header.update({'trajectories': trajectories_tmp})

    traclus_json = json.dumps(header, indent=4)

    return traclus_json


def write_to_file(traclus_json, filename="traclus_trajectories.json"):
    with open("Data/" + filename, 'w+') as f:
        f.write(traclus_json)