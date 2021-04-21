"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import helpers
import json
import math

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            diameter = float(row["diameter"]) if row["diameter"] else math.nan
            hazardous = row["pha"] == "Y"
            name = row["name"] or None
            neos.append(NearEarthObject(row["pdes"], name, diameter, hazardous))

    return neos


def load_approaches(cad_json_path="data/cad.json"):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    required_fields = ("des", "cd", "dist", "v_rel")
    cas = []
    with open(cad_json_path) as f:
        js = json.load(f)
        field_indices = {field_name: js["fields"].index(field_name) for field_name in required_fields}
        for row in js["data"]:
            data = {field_name: row[field_idx] for field_name, field_idx in field_indices.items()}
            approach_time = helpers.cd_to_datetime(data["cd"])
            approach_dist = float(data["dist"])
            approach_velocity = float(data["v_rel"])
            cas.append(CloseApproach(data["des"], approach_time, approach_dist, approach_velocity))
    return cas
