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
import json

from models import NearEarthObject, CloseApproach

import pathlib

here = pathlib.Path('.')
here = here.resolve()
TEST_CAD_FILE = here / 'tests' / 'test-cad-2020.json'
TEST_NEO_FILE = here / 'tests' / 'test-neos-2020.csv'

def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.

    neos = []
    # print("####################START##########################")
    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for elem in reader:
            # print(elem)
            neo = NearEarthObject(elem['pdes'], elem['name'], elem['diameter'], elem['pha'])
            # print(neo.__repr__())
            neos.append(neo)
    # print(neos)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.

    approaches = []
    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)
        for elem in contents['data']:
            designation = elem[0]
            time = elem[3]
            distance = elem[4]
            velocity = elem[7]

            # print(designation, time, distance, velocity)
            ca = CloseApproach(designation, time, distance, velocity)
            approaches.append(ca)
            # print(approaches)

    return approaches

# if __name__ == '__main__':
    # load_approaches(TEST_CAD_FILE)