"""Module docstring for import rand"""
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

locs_list = [
    {
        "loc_name": "A",
        "desc": "Spawn",
        "items": "None",
        "next_loc": ["B", "C", "D"]
    },
    {
        "loc_name": "B",
        "desc": "Fields",
        "items": random.choice(["Sword", "Stick", "Knife", "Dagger"]),
        "next_loc": ["E", "F", "G"]
    },
    {
        "loc_name": "E",
        "desc": "Cave",
        "items": random.choice(["Sword", "Stick", "Knife", "Dagger"]),
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
        print(location_split[0])
        dest = input(str("Where would you like to go?")).upper()

        for loc in locs_list:
            # if player's dest in next_loc
            if dest in loc["next_loc"]:
                self._location = dest
                print("You have moved.")
                print(f"Next locations are: {locs_list[0].values()}")
                return dest

            return False

    def __repr__(self):
        """Prints out player name, health, dmg and current location."""
        return f"{self.name} {self.health} {self.dmg} {self._location}"

player = Player("aeirone", 10, 10, "Spawn Point")
# print(player)

# check_loc = player.move()

# player = Player("aeirone", 100, 1, check_loc)
# # error()
# print(player)

# create tkinter window
root = tk.Tk()

# title change
root.title('TOR')

# window geometry
root.geometry('800x700')
root.resizable('False','False')

# title
title = Label(root, text = "Tower of Resuscitation")
title.config(font =("Courier", 25))
title.pack()

# text box for input
txt_box = Text(root, height=4, width=20)
txt_box.pack()

# next button
b1 = Button(root, text = "Next", )
b1.pack()

# exit button.
b2 = Button(root, text = "Exit",
            command = Widget.destroy) 
b2.pack()

root.mainloop()