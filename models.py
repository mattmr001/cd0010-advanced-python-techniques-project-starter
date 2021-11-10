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
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
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
    def diameter(self):
        print("Getting diameter value...")
        return self._diameter

    @diameter.setter
    def diameter(self, val):
        print("Setting diameter value...")
        if val == '':
            print(val)
            self._diameter = 'nan'
        else:
            print(val)
            self._diameter = float(val)

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
        # TODO round diamter if passed to string ex: self.diameter:.3f but allow the string 'NAN'
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter}, hazardous={self.hazardous!r})"


class CloseApproach():
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
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, neo=None, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self._designation = ''
        self.time = cd_to_datetime(info["time"])  # TODO: Use the cd_to_datetime function for this attribute.
        self.distance = 0.0
        self.velocity = 0.0

        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo

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
        # TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        formatted_time = datetime_to_str(self.neo.time)
        # TODO: Use self.designation and self.name to build a fullname for this object.
        fullname = f"{self.neo.designation} {self.neo.name}"
        return f"{fullname} approach time {formatted_time}"

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f"A close approach... took place at {self.time_str!r}, was at a distance of {self.distance:.2f}, " \
               f"had a velocity of {self.velocity:.2f}, and had the name of {self.neo.name!r})"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
