from tkinter import Tk

locs_list = [
    {
        "loc_name": "Spawn point",
        "desc": "Spawn point of the player",
        "items": " ",
        "next_loc": ["B", "C", "D"]
    },
    {
        "loc_name": "B",
        "desc": "Area lies a hidden chest.",
        "items": " ",
        "next_loc": ["E", "F", "G"]
    },
    {
        "loc_name": "E",
        "desc": "Area lies a hidden chest.",
        "items": " ",
        "next_loc": ["H", "I", "J"]
    }
]


class Map:
    """Map for the game."""

    def __init__(self):
        """Docstring for map."""
        self.map = []


class Location:
    """Location for player.

    Returns:
        str: location, description, items and next locations.
    """

    # next_loc is the node and is set to 'None' by default
    def __init__(self, loc_name, desc, items, next_loc):
        """Docstring for location."""
        self.loc_name = loc_name
        self.desc = desc
        self.items = items
        self.next_loc = next_loc

    def __repr__(self):
        """Prints out location name, description and the next locations."""
        return f"{self.loc_name} {self.desc} {self.items} {self.next_loc}"

# static method makes the method belong to class itself,
# not a specific instance of the class.
    @staticmethod
    def rand_ite():
        """Items for each location."""
        # TODO randomise the items and assign it to a location.
        common = ["Sword", "Stick", "Knife", "Dagger"]
        rare = ["Machete", "Katana", "Flail", "Mace", "Shield"]
        legendary = ["Excalibur"]


location_split = [Location(**locations) for locations in locs_list]


class Player:
    """Player's attributes."""

    def __init__(self, name, health, dmg, location):
        """Docstring for Player."""
        self.name = name
        self.health = health
        self.max_health = health
        self.dmg = dmg
        self._location = location  # current

    @property
    def location(self):
        """ Gets the location.

        Returns:
            str: location of the player.
        """
        return self._location

    @location.setter
    def location(self, new_loc):
        self._location = new_loc

    def move(self):
        """Move method for player.

        Returns:
            str: new location of player
        """
        dest = input(str("Where would you like to go?")).upper()

        for loc in locs_list:
            # if player's dest in next_loc
            if dest in loc["next_loc"]:
                self._location = dest
                return dest

            return False

    def __repr__(self):
        """Prints out player name, health, dmg and current location."""
        return f"{self.name} {self.health} {self.dmg} {self._location}"


def error():
    """If check loc is False."""

    while check_loc is False:
        print("Sorry but this is an invalid location. Try again: ")
        player.move()
        if check_loc: # fix to break the loop.
            print(player)


player = Player("aeirone", 10, 10, "Spawn Point")
print(player)

check_loc = player.move()

player = Player("aeirone", 10, 10, check_loc)
# error()
print(player)
