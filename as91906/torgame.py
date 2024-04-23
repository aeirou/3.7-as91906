"""Module docstring for import rand"""
import random
import tkinter as tk
from tkinter import Label, Text, Button

# TODO fix random choices for items
NESTED_DICT_LIST = {
    "A":{
        "desc": "Spawn Point",
        "items": "None",
        "next_loc": ["B", "C"]
    },
    "B":{
        "desc": "Basement Classroom 1",
        "items": random.choice(["Paper", "Pen", "Paper", "Twink"]),
        "next_loc": ["C", "D"]
    },
    "C":{
        "desc": "Basement Classroom 2",
        "items": random.choice(["Paper", "Pen", "Paper", "Twink"]),
        "next_loc": ["B", "E",]
    },
    "D":{
        "desc": "Key Room",
        "items": "Floor One Key",
        "next_loc": ["B"]
    },
    "E":{
        "desc": "Gate to Floor 2",
        "items": "None",
        "next_loc": ["F"]
    }}


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


class Player:
    """Player's attributes."""

    def __init__(self,num_tries):
        """Docstring for Player."""
        self.inv = []
        self.num_tries = num_tries
        self.current_location = "A" # current

    @property
    def location(self):
        """ Gets the location.

        Returns:
            str: location of the player.
        """
        return self.current_location

    @location.setter
    def location(self, new_loc):
        self.current_location = new_loc

    def number_of_tries(self):
        """Checks how many paper, rubber and twink there are in player's inventory.
        """

    def pick_up_item(self):
        """Check if item is in the list.
        """

        item = input("What item(s) would you like to pick up? ")

        # checks if the item is in 'items' in the current location by indexing the current location and items
        if item in NESTED_DICT_LIST[self.current_location]['items']:
            self.inv.append(item) # adds the item that is picked up into the inv
            return self.inv

    def move(self, dest):
        """Move method for player.

        Returns:
            str: the new location of player.
        """
        # while true
        # if player's dest in next_loc
        if dest in NESTED_DICT_LIST[self.current_location]["next_loc"]:
            self.current_location = dest
            return dest
        return False

    def __repr__(self):
        """Prints out player name, health, dmg and current location."""
        return f"{self.inv} {self.current_location}"


player = Player(0)

# —————————————————————Tkinter————————————————————— #

# Create tkinter window
root = tk.Tk()

# Title change
root.title('TOR')

# Window geometry
root.geometry('800x700')
root.resizable('False','False')

# Title
title = Label(root, text = "Tower of Resuscitation")
title.config(font =("Courier", 25))
title.pack()


def toggle_location_buttons():
    """
        Creates a list of buttons to show the next locations available,
        to the player in their current location.
    """
    # Hides all the buttons
    button_b.pack_forget()
    button_c.pack_forget()
    button_d.pack_forget()
    button_e.pack_forget()

    # Empty list for the buttons that is going ot be displayed
    list_of_buttons_to_show = []

    # Goes through the next locations of the current location to display on the list.
    # From the current location (player.current_location), it checks through the next locations
    # -available by going through the "next_loc".
    if "B" in NESTED_DICT_LIST[player.current_location]["next_loc"]:
        list_of_buttons_to_show.append(button_b) # appends that location into the list of buttons
    if "C" in NESTED_DICT_LIST[player.current_location]["next_loc"]:
        list_of_buttons_to_show.append(button_c)
    if "D" in NESTED_DICT_LIST[player.current_location]["next_loc"]:
        list_of_buttons_to_show.append(button_d)
    if "E" in NESTED_DICT_LIST[player.current_location]["next_loc"]:
        list_of_buttons_to_show.append(button_e)

    # Show only the locations that are available from the current location.
    for button in list_of_buttons_to_show:
        button.pack(side=tk.TOP)


def update_player_loc(updated_loc):
    """
        Updates the player's location on the player's stats menu, as well as 
        the output text box.
    """
    # Changes the location of the player on the player's stats menu.
    player_stats.config(state='normal')  # Enables editing
    player_stats.delete('1.0', tk.END)  # Clears the previous text
    player_stats.insert(tk.END,
                        (f"\nYou are currently in location: {updated_loc}")) # Insert current loc
    player_stats.config(state='disabled')  # Disable user editing

    # Notify's player that they have moved.
    output.config(state='normal')
    output.insert(tk.END,
                        (f"\nYou have moved to location: {updated_loc}\n"))
    output.config(state='disabled')

    toggle_location_buttons() # Initialises to show the buttons.


def update_player_inv(updated_inv):
    """
        Updates the player's inventory on the output text box.
    """
    player_stats.config(state='normal')
    player_stats.delete('1.0', tk.END)
    player_stats.insert(tk.END,
                        (f"Inventory: {updated_inv}"))
    player_stats.config(state='disabled')


# Output text box for player's actions.
output = Text(root, height=25, width=75, bg="black")
output.insert('1.0',
             (f"\nYou are currently in location: {player.current_location}\n")) # Insert current location
output["state"]="disabled" # Disable user editing


# Text box for the player's current location and items in inventory.
player_stats = Text(root, fg="white", height="5px")
player_stats.insert('1.0',
                    (f"\nYou are currently in location: {player.current_location}"))
player_stats["state"]="disabled"


# Parent button which toggles the children buttons
start_move = Button(root, text="Move", command=toggle_location_buttons)


# Location buttons which are toggled by the parent button: start_move.
# TODO create a button for all locations.
button_b = Button(root,
                      height=2,
                      width=8,
                      text="B",
                      command=lambda: update_player_loc(player.move("B")))

button_c = Button(root,
                      height=2,
                      width=8,
                      text="C",
                      command=lambda: update_player_loc(player.move("C")))

button_d = Button(root,
                      height=2,
                      width=8,
                      text="D",
                      command=lambda: update_player_loc(player.move("D")))
button_e = Button(root,
                      height=2,
                      width=8,
                      text="E",
                      command=lambda: update_player_loc(player.move("E")))
button_f = Button(root,
                      height=2,
                      width=8,
                      text="F",
                      command=lambda: update_player_loc(player.move("F")))


player_stats.pack()
output.pack()
start_move.pack()

root.mainloop()
