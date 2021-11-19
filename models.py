"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
import math

from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    def __init__(self, designation, name=None, diameter='nan', hazardous=False):
        """
        Create a new `NearEarthObject`
        :param designation: str supplied to the constructor
        :param name: str supplied to the constructor
        :param diameter: int supplied to the constructor
        param hazardous: bool supplied to the constructor
        """
        self.designation = designation
        self.name = name
        self.hazardous = hazardous
        self.diameter = diameter
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # print("Setting name value")
        if value == '':
            self._name = None
        else:
            self._name = value

    @property
    def hazardous(self):
        # print("Getting hazardous value...")
        return self._hazardous

    @hazardous.setter
    def hazardous(self, value):
        # print("Setting hazardous value...")
        # print("value:", value)
        if value == 'Y':
            # print(value)
            self._hazardous = True
        else:
            self._hazardous = False

    @property
    def diameter(self):
        # print("Getting diameter value...")
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        # print("Setting diameter value...")
        if value == '':
            # print(value)
            self._diameter = math.nan
        else:
            # print(value)
            self._diameter = float(value)

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name is not None:
            return f"{self.designation} {self.name}"
        else:
            return f"{self.designation}"

    def __str__(self):
        """Return `str(self)`."""
        return f"A NearEarthObject named {self.fullname} that has a diameter" \
               f" of {self.diameter:.3f} and is {self.hazardous!r} hazardous"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    def __init__(self, designation, time, distance, velocity, neo=None,):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self._designation = designation
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        formatted_time = datetime_to_str(self.time)
        return formatted_time

    @property
    def fullname(self):
        if self.neo is not None:
            fullname = f"{self._designation} {self.neo.name}"
        else:
            fullname = self._designation
        return f"{fullname} approach time {self.time_str}"

    def __str__(self):
        """Return `str(self)`."""
        return f"A close approach... took place at {self.time_str!r}, was at a distance of {self.distance:.2f}, " \
               f"had a velocity of {self.velocity:.2f}, and had the name of {self.neo.name!r})"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
