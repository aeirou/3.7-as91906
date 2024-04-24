"""Module docstring for import rand"""
import random
import tkinter as tk
from tkinter import Label, Text, Button

# TODO fix random choices for items
NESTED_DICT_LIST = {
    "A":{
        "desc": "Spawn Point",
        "items": " ",
        "next_loc": ["B", "C"]
    },
    "B":{
        "desc": "Basement Classroom 1",
        "items": random.choice(["Paper", "Pen", "Paper", "Twink"]),
        "next_loc": ["A","C", "D"]
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
        "items": " ",
        "next_loc": ["C","F"]
    }}


class Map:
    """Map for the game."""

    def __init__(self):
        """Docstring for map."""
        self.map = []

# when taking away an item from the location, the constant 'nested_dict' doesnt change
# but the class location does.

class Location:
    """The locations and its attributes which changes instead of the nested dict, which is a list.

    Returns:
        str: loc_name: The name of the location.
             desc: The description of the location.
             items: The items in the location which are obtainable.
             next_loc: The next locations the player can travel to from their current location.
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
        """
            Initialises inventory, number of tries and current location.
        """
        self.inv = []
        self.num_tries = num_tries
        self.current_location = "A"

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

        # checks if the item is in 'items' in the current location
        # by indexing the current location and items
        if item in NESTED_DICT_LIST[self.current_location]['items']:
            self.inv.append(item) # adds the item that is picked up into the inv
            return self.inv

    def inv_empty(self):
        """Return 'None' when inventory is empty.

        Returns:
            str: when inventory is empty, it outputs none.
        """
        if not self.inv:
            return "You have nothing in your inventory."
        else:
            return f"Inventory: {self.inv}"

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
        """Prints out player inventory and current location."""
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

     # Empty list for the buttons that is going ot be displayed
    list_of_buttons_to_show = []

    # Hides all the buttons first.
    button_a.pack_forget()
    button_b.pack_forget()
    button_c.pack_forget()
    button_d.pack_forget()
    button_e.pack_forget()

    # Goes through the next locations of the current location to display on the list.
    # From the current location (player.current_location), it checks through the next locations
    # -available by going through the "next_loc".
    if "A" in NESTED_DICT_LIST[player.current_location]["next_loc"]:
        list_of_buttons_to_show.append(button_a) # appends that location into the list of buttons
    if "B" in NESTED_DICT_LIST[player.current_location]["next_loc"]:
        list_of_buttons_to_show.append(button_b)
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


def show_location_info():
    """Returns the location's description, items, and next possible locations."""
    # Matches the updated location to it's dictionary and takes it.
    loc_info = NESTED_DICT_LIST[player.current_location]
    desc = f"You are currently in: {loc_info['desc']}" # Takes the 'desc' of that location.
    items = loc_info['items'] # Takes the 'items' of that location.
    next_locs = f"Your next possible locations are: {' '.join(loc_info['next_loc'])}"  # Turns list into a string w/o '[,]'

    # Checks if there are obtainable items in the current location of the player.
    if items == " ":
        items = "There are no obtainable items in this location." # If there are no items.
    else:
        items = f"You have found the items: {loc_info['items']}" # If there are items.

    return f"{desc}\n{items}\n{next_locs}"


def update_player_inv(updated_inv):
    """
        Updates the player's inventory on the output text box.
    """
    player_stats.config(state='normal')
    player_stats.delete('2.0', '2.end')
    player_stats.insert(tk.END,
                        (f"Inventory: {updated_inv}"))
    player_stats.config(state='disabled')


# Text box for the player's current location and items in inventory.
player_stats = Text(root, fg="white", height="13px")
player_stats.insert('1.0',
                    (f"\n{player.inv_empty()}\n"))
player_stats.insert('1.0',
                    (f"\nYou are currently in location: {player.current_location}\n"))
player_stats["state"]="disabled"


# Output text box for player's actions.
output = Text(root, height=25, width=75, bg="black")
output.insert('1.0',
             (f"\nYou are currently in location: {player.current_location}\n")) # current location
# Inserts the location's atributtes (desc, items, next_loc)
output.insert(tk.END,
                (f"\n{show_location_info()}\n"))
output["state"]="disabled" # Disable user editing
output.see('end')


# Parent button which toggles the children buttons
start_move = Button(root, text="Move", command=toggle_location_buttons)


# Location buttons which are toggled by the parent button: start_move.
# TODO create a button for all locations.
button_a = Button(root,
                      height=2,
                      width=8,
                      text="A",
                      command=lambda: update_player_loc(player.move("A")))
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
