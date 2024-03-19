# from tkinter import Tk
"""Docstring for tkinter module"""

locs_list = [
    {
        "loc_name": "Spawn point",
        "desc": "Spawn point of the player",
        "items": "None",
        "next_loc": ["B", "C", "D"] # <-- does the method go through every "next_loc"?
    },
    {
        "loc_name": "Point B",
        "desc": "Area lies a hidden chest.",
        "items": "a sword",
        "next_loc": ["E", "F", "G"]
    }
]


class Map:
    """
        Map for the game.
    """

    def __init__(self):
        self.map = []


class Location:
    """Location for player.

    Returns:
        str: location, description, items and next locations
    """

    # next_loc is the node and is set to 'None' by default
    def __init__(self, loc_name, desc, items, next_loc):
        self.loc_name = loc_name
        self.desc = desc
        self.items = items
        self.next_loc = next_loc

    def __repr__(self):
        """
            Prints out location name, description and the next locations
        """
        return f"{self.loc_name} {self.desc} {self.items} {self.next_loc}"


location_split = [Location(**locations) for locations in locs_list]


class Player:
    """ 
    Player's attributes. 
    """

    def __init__(self, name, health, dmg, location):
        self._name = name
        self._health = health
        self._dmg = dmg
        self._location = location  # current

    @property
    def location(self):
        """

        Returns:
            _type_: _description_
        """
        return self._location

    @location.setter
    def location(self, new_loc):
        self._location = new_loc

    def __repr__(self):
        """
            Prints out player name, health, dmg and current location.
        """
        return f"{self._name} {self._health} {self._dmg} {self._location}"

    def move(self):
        """move method for player.

        Returns:
            str: new location of player
        """
        for loc in locs_list:
            dest = input(str("Where would you like to go?")).upper()

            # if player's dest in next_loc
            if dest in loc["next_loc"]:
                dest = self._location
                return dest

    def __str__ (self):
        return f'{self._name}, {self._health}, {self._dmg}, Spawn Point'


player = Player("aeirone", 10, 10, "Spawn Point")
print(player)
player.move()

# TODO how to change current location to dest
player = Player("aeirone", 10, 10, player.move)
print(player)
