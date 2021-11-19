"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""
import pathlib

here = pathlib.Path('.')
here = here.resolve()
TEST_CAD_FILE = here / 'tests' / 'test-cad-2020.json'
TEST_NEO_FILE = here / 'tests' / 'test-neos-2020.csv'
from extract import load_neos, load_approaches


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        self._neo_by_designation = {neo.designation: neo for neo in neos}
        self._neo_by_name = {neo.name: neo for neo in neos if neo.name}

        self.link_neos_with_approaches(self._neo_by_designation,
                                       self._neo_by_name)

    def link_neos_with_approaches(self, neo_by_designation, neo_by_name):
        """ Link together the NEOs and their close approaches.
            :param neo_by_designation: dict of neo designations and associtated neo.
            :param neo_by_names: dict of neo names and associated neos.
        """
        for approach in self._approaches:
            neo = self._neo_by_designation[approach._designation]
            approach.neo = neo
            neo.approaches.append(approach)

    def test(self):
        print("NEO : ", self._neos[0].__repr__)
        print("APPROACH : ", self._approaches[0].__repr__)

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """
        for neo in self._neos:
            if designation != neo.designation:
                continue
            else:
                print("Designation input : ", designation)
                print("Neo Designation : ", neo.designation)
                return neo

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        for neo in self._neos:
            if name != neo.name:
                continue
            else:
                print("Found neo name : ", neo.name)
                return neo

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaningfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        for approach in self._approaches:
            if all(f(approach) for f in filters):
                yield approach

if __name__ == '__main__':
    neos = load_neos(TEST_NEO_FILE)
    approaches = load_approaches(TEST_CAD_FILE)
    db = NEODatabase(neos, approaches)
    print(db.test())
    print(db.get_neo_by_designation("1865"))
    # print(db.get_neo_by_name('Toro'))
    print("query : ", list(db.query()))
