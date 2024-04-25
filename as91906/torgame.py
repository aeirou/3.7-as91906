"""Module docstring for import rand"""
import random
import copy
import tkinter as tk
from tkinter import Label, Text, Button


# Item list.
item_list = {
    "Old Sword":{
        "weapon": "Old Sword",
        "weapon_desc": "An old rusty sword covered with dry blood of fallen soldiers.",
        "weapon_health": 10,
        "weapond_dmg": 3,
    },
    "Sword":{
        "weapon": "Sword",
        "weapon_desc": "A silver sword which was taken from a dead knight.",
        "weapon_health": 20,
        "weapond_dmg": 7,
    },
    "Legendary Dragon Slayer":{
        "weapon": "Legendary Dragon Slayer",
        "weapon_desc": "A legendary greatsword that weighs the same as the sky, but weightless to the One.",
        "weapon_health": 50, # max health of the sword.
        "weapond_dmg": 20,
    },
    "Silver Key to Floor 2":{
        "key_floor2": "Silver Key to Floor 2"
    },
    "Golden Key to Floor 3":{
        "key_floor3":  "Golden Key to Floor 3"
    }

}


# Location list.
# TODO fix random choices for items
NESTED_DICT_LIST = {
    "A":{
        "desc": "a battlefield filled with corpses and rusty swords.", # fight 
        "items": [item_list['Old Sword']['weapon']],
        "next_loc": ["B", "C"]
    },
    "B":{
        "desc": "a wooden shack",
        "items": [item_list['Sword']['weapon']],
        "next_loc": ["A","C", "D"]
    },
    "C":{
        "desc": "an old ruin of a shack.",
        "items": " ",
        "next_loc": ["B", "E",]
    },
    "D":{
        "desc": "a cave that hold an important treasure.",
        "items": [item_list['Silver Key to Floor 2']['key_floor2']],
        "next_loc": ["B"]
    },
    "E":{
        "desc": "Gate to Floor 2",
        "items": " ",
        "next_loc": ["C","F"]
    }}


class Player:
    """Player's attributes."""

    def __init__(self,num_tries):
        """
            Initialises inventory, number of tries and current location.
        """
        self.inv = []
        self.num_tries = num_tries
        self.current_location = "A"

    @property
    def new_location(self):
        """ Gets the location.

        Returns:
            str: Returns the current location of the player.
        """
        return self.current_location

    @new_location.setter
    def new_location(self, new_loc):
        """Sets the new location of the player based on where they chose to go.

        Args:
            new_loc (str): The new location of the player.
        """
        self.current_location = new_loc


    def inventory(self,item):
        """Method for adding items into the player's inventory.

        Returns:
            str: The items in the player's inventory.
        """
        if item in NESTED_DICT_LIST[self.current_location]['items']:
            self.inv.append(item)
            NESTED_DICT_LIST[self.current_location]['items'].remove(item)
            return self.inv
        return False

    def item_remove(self,remove):
        """Method for when the item is removed from inventory.

        Args:
            item (str): The item the player holds.
        """


    def inv_empty(self):
        """Return 'None' when inventory is empty.

        Returns:
            str: output for when the inventory is empty.
        """
        if not self.inv:
            return "You have nothing in your inventory."
        else:
            return f"Inventory: {self.inv}"


    def number_of_tries(self):
        """Checks how many paper, rubber and twink there are in player's inventory.
        """


    def move(self, dest):
        """Move method for player: Checks if the new location is
           available from the current location of the player.

        Returns:
            str: the new location of player.
        """
        # Checks if dest is in the value: 'next_loc' of the current location.
        if dest in NESTED_DICT_LIST[self.current_location]["next_loc"]:
            self.current_location = dest # Sets dest to the current location.
            return dest
        return False
    

class Map:
    """Map for the game."""

    def __init__(self):
        """Docstring for map."""
        self.map = []

# when taking away an item from the location, the constant 'nested_dict' doesnt change
# but the class location does.

class Location:
    """The locations and its attributes which changes, instead of the nested dict, which is a list.

    Returns:
        str: loc_name: The name of the location.
             desc: The description of the location.
             items: The items in the location which are obtainable.
             next_loc: The next locations the player can travel to from their current location.
    """

    # next_loc is the node and is set to 'None' by default
    def __init__(self):
        """Docstring for location."""
        self.loc_name = NESTED_DICT_LIST[player.current_location]
        self.desc = NESTED_DICT_LIST[player.current_location]['desc']
        self.items = NESTED_DICT_LIST[player.current_location]['items']
        self.next_loc = NESTED_DICT_LIST[player.current_location]['next_loc']

    def check_items(self):
        """Checks if there are any items in the location.
        """
        if NESTED_DICT_LIST[player.current_location]['items'] != ' ':
            return f"You have found: {''.join(NESTED_DICT_LIST[player.current_location]['items'])}"
        else:
            return "There are no obtainable items in this location."


    def __repr__(self):
        """Prints out location name, description and the next locations."""
        return f"{self.loc_name} {self.desc} {self.items} {self.next_loc}"


player = Player(0)
location = Location()


# —————————————————————Tkinter————————————————————— #


# Create tkinter window
root = tk.Tk()

# Title change
root.title('TOR')

# Window geometry
root.geometry('800x700')
# root.resizable('False','False')

# Title
title = Label(root, text = "Tower of Resuscitation")
title.config(font =("Courier", 25))
title.pack()


def toggle_location_buttons():
    """
        Creates a list of buttons to show the next locations available,
        to the player in their current location.
    """
     # Hides all the buttons first.
    for button in loc_buttons.values(): # Calls the values (buttons) in the dictionary.
        button.pack_forget()

    # Goes through the list of the value: 'next_loc', of the current location
    # to create the buttons of the new locations the player can travel to.
    for loc in NESTED_DICT_LIST[player.current_location]["next_loc"]:
        loc_buttons[loc].pack(side=tk.TOP)


def toggle_items_button():
    """ 
        This function creates a list of buttons to show the items 
        in the player's current location.
    """
    for button in item_buttons.values():
        button.pack_forget()

    items = NESTED_DICT_LIST[player.current_location]["items"]

   # Checks if items is a string or a list
    if isinstance(items, str):
        items = [items]

    for item in items:
        if item in item_list:  # Checks if the item exists in the item_list
            item_buttons[item].pack(side=tk.LEFT)


def update_player_loc(updated_loc):
    """
        Updates the player's location on the player's stats menu, as well as 
        the output text box.
    """
    # Changes the location of the player on the player's stats menu.
    player_stats.config(state='normal')  # Enables editing
    player_stats.delete('end-3l', tk.END)  # Clears the previous text
    player_stats.insert(tk.END,
                        (f"\nYou are currently in location: {updated_loc}")) # Insert current loc
    player_stats.config(state='disabled')  # Disable user editing

    # Notify's player that they have moved.
    output.config(state='normal')
    output.insert(tk.END,
                        (f"\nYou have moved to location: {updated_loc}\n"))
    output.insert(tk.END,
                (f"\n{show_location_info()}\n"))
    output.config(state='disabled')

    toggle_location_buttons() # Initialises the buttons to change & show
                              # whenever the player's location updates.


def update_player_inv(updated_inv):
    """
        Updates the player's inventory on the output text box.
    """
    player_stats.config(state='normal')
    player_stats.delete('2.0', '2.end')
    player_stats.insert(tk.END,
                        (f"Inventory: {updated_inv}"))
    player_stats.config(state='disabled')


def show_location_info():
    """Returns the location's description, items, and next possible locations."""
    # Matches the updated location to it's dictionary and takes it.
    loc_info = NESTED_DICT_LIST[player.current_location]
    desc = f"You are currently at: {loc_info['desc']}" # Takes the 'desc' of that location.
    items = location.check_items() # Takes the 'items' of that location.
    next_locs = f"Your next possible locations are: {' '.join(loc_info['next_loc'])}" # List to str.

    return f"{desc}\n{items}\n{next_locs}"


# Text box for the player's current location and items in inventory.
player_stats = Text(root, fg="white", height="13px")
player_stats.insert('1.0',
                    (f"\n{player.inv_empty()}\n"))
player_stats.insert('1.0',
                    (f"\nYou are currently in location: {player.current_location}\n"))
player_stats["state"]="disabled"


# Output text box for player's actions.
# TODO make the text box automatically scroll at the bottom. (scrollable)
output = Text(root, height=25, width=90, bg="black")
output.insert('1.0',
             (f"\nYou are currently in location: {player.current_location}\n")) # current location
# Inserts the location's atributtes (desc, items, next_loc)
output.insert(tk.END,
                (f"\n{show_location_info()}\n"))
output["state"]="disabled" # Disable user editing
output.see('end')

# Parent button which toggles the sub buttons for items.
start_pick_up = Button(root, text="Pick up item", command=toggle_items_button)

# Item buttons which are toggled by the parent button: start_pick_up
item_buttons = {
  "Old Sword": Button(root, 
                height=2,
                width=8,
                text="Old Sword",
                command=lambda: update_player_inv(player.inventory("Old Sword"))),
    "Sword": Button(root, 
                height=2,
                width=8,
                text="Sword",
                command=lambda: update_player_inv(player.inventory("Sword"))),
    "Legendary Dragon Slayer": Button(root,
                height=2,
                width=8,
                text="Legendary Dragon Slayer",
                command=lambda: update_player_inv(player.inventory("Legendary Dragon Slayer"))),
    "Silver Key to Floor 2": Button(root,
                height=10,
                width=10,
                text="Silver Key to Floor 2",
                command=lambda: update_player_inv(player.inventory("Silver Key to Floor 2"))),
    "Golden Key to Floor 3": Button(root,
                height=2,
                width=8,
                text="Golden Key to Floor 3",
                command=lambda: update_player_inv(player.inventory("Golden Key to Floor 3"))),
}


# Parent button which toggles the sub buttons for locations.
start_move = Button(root, text="Move", command=toggle_location_buttons)


# Location buttons which are toggled by the parent button: start_move.
# TODO create a button for all locations.
loc_buttons = {
    "A": Button(root, 
                height=2,
                width=8,
                text="A",
                command=lambda: update_player_loc(player.move("A"))),
    "B": Button(root, 
                height=2,
                width=8,
                text="B",
                command=lambda: update_player_loc(player.move("B"))),
    "C": Button(root,
                height=2,
                width=8,
                text="C",
                command=lambda: update_player_loc(player.move("C"))),
    "D": Button(root,
                height=2,
                width=8,
                text="D",
                command=lambda: update_player_loc(player.move("D"))),
    "E": Button(root,
                height=2,
                width=8,
                text="E",
                command=lambda: update_player_loc(player.move("E"))),
    "F": Button(root,
                height=2,
                width=8,
                text="F",
                command=lambda: update_player_loc(player.move("F"))),
}

player_stats.pack()
output.pack()
start_pick_up.pack()
start_move.pack()

root.mainloop()
