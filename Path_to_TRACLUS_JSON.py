import json
from pathlib import Path


def create_header(epsilon=0.00016, min_neighbors=2, min_num_trajectories_in_cluster=3, min_vertical_lines=2, min_prev_dist=0.0002):
    header = {
        "epsilon": epsilon,
        "min_neighbors": min_neighbors,
        "min_num_trajectories_in_cluster": min_num_trajectories_in_cluster,
        "min_vertical_lines": min_vertical_lines,
        "min_prev_dist": min_prev_dist
    }

    json_header = json.dumps(header, indent=4)

    return json_header


def create_trajectories(paths):
    list_trajectories = []
    for path in paths:
        trajectory = []
        for point in path.points:
            dict_point = {
                "x": point.x,
                "y": point.y
            }
            trajectory.append(dict_point)
        list_trajectories.append(trajectory)

    trajectories = {
        "trajectories": list_trajectories
    }

    json_trajectories = json.dumps(trajectories, indent=4)

    return json_trajectories


def create_traclus_json(json_header, json_trajectories):
    header = json.loads(json_header)
    trajectories = json.loads(json_trajectories)
    header.update(trajectories)

    traclus_json = json.dumps(header, indent=4)

    return traclus_json


def write_traclus_json_file(traclus_json, filename="traclus_trajectories.json"):
    with open("Data/" + filename, 'w+') as f:
        json.dump(traclus_json, f, indent=4)
