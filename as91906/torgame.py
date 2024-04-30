"""Module docstring for import rand"""
import tkinter as tk
from tkinter import *


# Location list.
# TODO fix random choices for items
NESTED_DICT_LIST = {
    "A":{
        "desc": "a battlefield filled with corpses and rusty swords.", # fight 
        "items": " ",
        "next_loc": ["B", "C"]
    },
    "B":{
        "desc": "a cozy looking wooden shack.",
        "items": " ",
        "next_loc": ["A","C", "D"]
    },
    "C":{
        "desc": "an old ruin of a shack.",
        "items": "",
        "next_loc": ["B", "E",]
    },
    "D":{
        "desc": "a cave that hold an important treasure.",
        "items": " ",
        "next_loc": ["B"]
    },
    "E":{
        "desc": "Gate to Floor 2",
        "items": "",
        "next_loc": ["C","F"]
    }}


class Character:
    """A superclass for characters such as the player and npc.
    """
    def __init__(self, name, inv, health, current_location):
        """ Instantiates the name, inv, health and current location of a character.

        Args:
            name (str): Used to differentiate the enemy and non-enemy characters.
            inv (list): A list of items the player currently holds.
            health (int): Current and max health of the characters.
            current_location (str): The current location of the player.
        """
        self.name = name
        self.inv = inv
        self.health = health
        self.health_max = health
        self.current_location = current_location

        self.weapon = old_sword

    def attack(self, target):
        """Attack methods for the class: Character

        Args:
            target (str): Target is a parameter which the damage is dealt to.
        """
        target.health -= self.weapon
        # Sets target health as max health and min to 0.
        target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} to {target.name} with {self.weapon.name}")


class Player(Character):

    """Player's attributes."""

    def __init__(self, name, inv, health):
        super().__init__(name=name, inv=inv, health=health, current_location='A')

        self.default_weapon = self.weapon

    def inventory(self,item):
        """Method for adding items into the player's inventory.

        Returns:
            str: The items in the player's inventory.
        """

        if item in NESTED_DICT_LIST[self.current_location]['items']:

            item_instance = NESTED_DICT_LIST[self.current_location]['items']

            if isinstance(item_instance, list):
                item_instance = item_instance[0] # Only one weapon per location.

            self.inv.append(item_instance)
            NESTED_DICT_LIST[self.current_location]['items'] = []  # Removes item from the location.
            update_pick_up_button()
            output.config(state='normal')
            output.insert(tk.END,
                        (f"\nYou have picked up the item: {item}!\n"))
            return self.inv

        if not self.inv:
            return "There is nothing in your inventory."
        else:
            pass

    # add if statement
    def equip(self, weapon):
        """Equip method for the player.

        Args:
            weapon (str): The chosen weapon for the player.
        """
        if weapon in self.inv:
            self.weapon = weapon
            print(f"{self.name} has equipped {self.weapon.name}!")

    def drop(self):
        """Drop method for the player.
        """
        print(f"{self.name} has dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon


    def move(self, dest):
        """Move method for player: Checks if the new location is
           available from the current location of the player.

        Returns:
            dest (str): The new location of the player.
        """
        # Checks if dest is in the value: 'next_loc' of the current location.
        if dest in NESTED_DICT_LIST[self.current_location]["next_loc"]:
            self.current_location = dest # Sets dest to the current location.
            return dest
        return False

class Enemy(Character):
    """A subclass for the character class — the enemy. 
    """
    def __init__(self, name, inv, health, current_location, weapon):
        super().__init__(name, inv, health, current_location)
        self.weapon = weapon


class Item:
    """Docstring for the weapons the characters use.
    """
    def __init__(self, name, item_desc, damage, value):
        self.name = name
        self.item_desc = item_desc
        self.damage = damage
        self.value = value

    def __str__(self):
        """String representation of the Weapon object."""
        return f"{self.name}, {self.item_desc}, {self.damage}, {self.value}"

class Weapon(Item):
    """Subclass for weapons.

    Args:
        Item (str)): Item is a superclass which the Weapon class uses as a blueprint.
    """
    def __init__(self, name, item_desc, damage, value):
        # Calls back to the superclass.
        super().__init__(name=name, item_desc=item_desc, damage=damage, value=value)

# Default weapon of the player.
fist = Weapon(name="Fist",
                   item_desc="Fists",
                   damage=1,
                   value=2)

old_sword = Weapon(name="Old Sword",
                   item_desc="An old rusty sword covered with dry blood of fallen soldiers.",
                   damage=3,
                   value=5)

dagger = Weapon(name="Dagger",
                item_desc="A sharp dagger soaked with bright red blood.",
                damage=5,
                value=6)

bow = Weapon(name="Bow",
             item_desc="A short bow used by the Gremlins that wander the forest.",
             damage=9,
             value=8)

sword = Weapon(name="Sword",
                   item_desc="A silver sword which was taken from a dead knight.",
                   damage=10,
                   value=10)


dragon_slayer = Weapon(name="Legendary Dragon Slayer",
                   item_desc="A greatsword that weighs similar to Earth but weightless to the One.",
                   damage=20,
                   value=20)


key_floor_2 = Item(name="Silver Key",
                   item_desc="A silver key to Floor 2",
                   damage=0,
                   value=20)


key_floor_3 = Item(name="Gold Key",
                   item_desc="A gold key to Floor 3",
                   damage=0,
                   value=20)


# Update the 'items' values in the NESTED_DICT_LIST with weapon instances
NESTED_DICT_LIST["A"]["items"] = old_sword.name  # Assign the old_sword instance to location A
NESTED_DICT_LIST["B"]["items"] = sword.name  # Assign the sword instance to location B
NESTED_DICT_LIST["D"]["items"] = key_floor_2.name  # Assign the silver_key instance to location D


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

    def check_items(self, loc):
        """Checks if there are any items in the location.
        """
        if loc:
            if isinstance(loc, list):  # Check if loc is a list
                return f"You have found: {', '.join(loc)}"
            else:
                return f"You have found: {loc}"
        else:
            return "There are no obtainable items in this location."


    def __repr__(self):
        """Prints out location name, description and the next locations."""
        return f"{self.loc_name} {self.desc} {self.items} {self.next_loc}"


player = Player('hero',[],100)
goblin = Enemy('Goblin',[],100, 'A', dagger)
gremlin = Enemy('Gremlin',[],100, 'A', bow)
location = Location()


# —————————————————————Tkinter————————————————————— #


# Create tkinter window
root = tk.Tk()

# Title change
root.title('TOR')

# Window geometry
root.geometry('1100x900')
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

    if isinstance(items, str):
        items = [items]
    elif isinstance(items, Item):
        items = [items]

    for item in items:
        item_name = item  # Access the name attribute of the Weapon object
        item_buttons[item_name].pack(side=tk.LEFT)


def update_pick_up_button():
    """ This function shows the 'start_pick_up' button 
        if there are items in the location.
    """
    items = NESTED_DICT_LIST[player.current_location]["items"]
    if any(items) and any(item.strip() for item in items):
        start_pick_up.pack()
    else:
        start_pick_up.pack_forget()


def update_player_loc(updated_loc):
    """
        Updates the player's location on the player's stats menu, as well as 
        the output text box.
    """
    # Changes the location of the player on the player's stats menu.
    player_stats.config(state='normal')  # Enables editing
    player_stats.delete('1.0', '3.0')  # Clears the previous text
    player_stats.insert('1.0',
                        (f"\nYou are currently in location: {updated_loc}\n")) # Insert current loc
    player_stats.config(state='disabled')  # Disable user editing

    # Notifies player that they have moved.
    output.config(state='normal')
    output.insert(tk.END,
                        (f"\nYou have moved to location: {updated_loc}\n"))
    output.insert(tk.END,
                (f"\n{show_location_info()}\n")) # Prints the location's info
    output.config(state='disabled')

    toggle_location_buttons() # Initialises the buttons to change & show -
                              # whenever the player's location updates.

    update_pick_up_button() # Checks if there are items in the location.


def update_player_inv(updated_inv):
    """
        Updates the player's inventory on the player's stats text box.
    """
    player_stats.config(state='normal')
    player_stats.delete('3.0', tk.END)
    player_stats.insert('3.0',
                        (f"\nInventory:  {' , '.join(updated_inv)}\n"))
    player_stats.config(state='disabled')
    player_stats.see('end')

    # Checks if item has been picked up - removes the item button.
    for item in updated_inv:
        if item in item_buttons:  # Checks if the item exists in the item_list
            item_buttons[item].pack_forget()


def show_location_info():
    """Returns the location's description, items, and next possible locations."""
    # Matches the updated location to it's dictionary and takes it.
    loc_info = NESTED_DICT_LIST[player.current_location]
    desc = f"You are currently at: {loc_info['desc']}" # Takes the 'desc' of that location.
    items = location.check_items(NESTED_DICT_LIST[player.current_location]['items']) # Takes the 'items' of that location.
    next_locs = f"Your next possible locations are: {' '.join(loc_info['next_loc'])}" # List to str.

    return f"{desc}\n{items}\n{next_locs}"


# Default info for the text box for the player's current location and items in inventory.
player_stats = Text(root, fg="white", height="13px")
player_stats.insert('3.0',
                    (f"\n{player.inventory('none')}\n"))
player_stats.insert('1.0',
                    (f"\nYou are currently in location: {player.current_location}\n"))
player_stats["state"]="disabled"


# Default info for the output text box for player's actions.
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
    "Silver Key": Button(root,
                height=10,
                width=10,
                text="Silver Key",
                command=lambda: update_player_inv(player.inventory("Silver Key"))),
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
start_move.pack()

root.mainloop()
