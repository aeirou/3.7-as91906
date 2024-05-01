"""Docstring for the imported modules."""
import tkinter as tk


# Location list.
# TODO fix random choices for items
NESTED_DICT_LIST = {
    "A":{
        "desc": "a battlefield filled with corpses and rusty swords.", # fight 
        "items": [],
        "next_loc": ["B", "C"]
    },
    "B":{
        "desc": "a cozy looking wooden shack.",
        "items": [],
        "next_loc": ["A","C", "D"]
    },
    "C":{
        "desc": "an old ruin of a shack.",
        "items": [],
        "next_loc": ["B", "E",]
    },
    "D":{
        "desc": "a cave that hold an important treasure.",
        "items": [],
        "next_loc": ["B"]
    },
    "E":{
        "desc": "Gate to Floor 2",
        "items": [],
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


    def inventory(self):
        """Checks if inventory is empty."""
        if self.inv:
            return self.inv
        else:
            return f"Nothing in {self.name}'s inventory."

    def pick_up(self, item):
        """Method for adding items into the player's inventory.

        Returns:
            str: The items in the player's inventory.
        """
        if 6 > len(self.inv):
            if item in NESTED_DICT_LIST[self.current_location]['items']:
                self.inv.append(item)
                NESTED_DICT_LIST[self.current_location]['items'].remove(item) # Remove item from loc
                return self.inv
        return f"{self.name} has reached the maximum inventory space! "


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
NESTED_DICT_LIST["A"]["items"] = [old_sword.name, dagger.name]
NESTED_DICT_LIST["B"]["items"] = [sword.name]
NESTED_DICT_LIST["D"]["items"] = [key_floor_2.name]


class Map:
    """Map for the game."""

    def __init__(self):
        """Docstring for map."""
        self.map = []


class Location:
    """The locations and its attributes which changes, instead of the nested dict, which is a list.

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

    def check_items(self, loc):
        """Checks if there are any items in the location.
        """
        if loc:
            if isinstance(loc, list):  # Check if loc is a list
                return f"{player.name} has found: {', '.join(loc)}"
        else:
            return "There are no obtainable items in this location."


    def __repr__(self):
        """Prints out location name, description and the next locations."""
        return f"{self.loc_name} {self.desc} {self.items} {self.next_loc}"


class App(tk.Tk):
    """Main app for the GUI."""
    def __init__(self):
        super().__init__()
        self.title('TOR')
        self.geometry('1100x900')

        self.title_label = tk.Label(self, text="Tower of Resuscitation", font=("Courier", 25))
        self.title_label.pack()

        self.player_stats_frame = Playerstats(self)
        self.player_stats_frame.pack()

        self.output_frame = Output(self)
        self.output_frame.pack()

        self.move_frame = Move(self)
        self.move_frame.pack()

        self.pick_up_frame = PickUp(self)
        self.pick_up_frame.pack()

        self.move_frame.update_buttons()


class Playerstats(tk.Frame):
    """A class frame for the player stats text box."""
    def __init__(self, master):
        super().__init__(master)
        self.player_stats = tk.Text(self, fg="white", height="13px", state="disabled")
        self.player_stats.pack()
        self.update_player_stats(player.inventory(), player.current_location) # default attributes

    def update_player_stats(self, inventory, loc):
        """Updates the player stats text box.

        Args:
            inventory (str)): the inventory of the player.
            location (str): the current location of the player.
        """
        self.player_stats.config(state='normal')
        self.player_stats.delete('1.0', tk.END)
        self.player_stats.insert('1.0', f"\nYou are currently in location: {loc}\n")
        self.player_stats.insert('3.0', f"\nInventory: {inventory}\n")
        self.player_stats.config(state='disabled')


class Output(tk.Frame):
    """A class frame for the output text box."""
    def __init__(self, master):
        super().__init__(master)
        self.output_text = tk.Text(self,
                                   height=25,
                                   width=90,
                                   bg="black",
                                   fg="white",
                                   state="disabled")
        self.output_text.pack()
        self.update_output(player.current_location)


    def update_output(self, current_location):
        """Updates the output box of the current_location

        Args:
            current_location (str): the current location of the player.
        """
        self.output_text.config(state='normal')
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0',
                                f"\n{player.name} is currently in location: {current_location}\n")
        self.output_text.insert(tk.END, f"\n{self.loc_info()}\n")
        self.output_text.config(state='disabled')
        self.output_text.see('end')


    def loc_info(self):
        """The format for the location's info."""
        loc_info = NESTED_DICT_LIST[player.current_location]

        desc = f"{player.name} is currently at {loc_info['desc']}"
        items = location.check_items(NESTED_DICT_LIST[player.current_location]['items'])
        next_locs = f"{player.name}'s next routes are: {' '.join(loc_info['next_loc'])}"

        return f"{desc}\n{items}\n{next_locs}"


class Move(tk.Frame):
    """A class for the location buttons and move button."""
    def __init__(self, master):
        super().__init__(master)

        self.app = master # referencing to the main app gui

        self.loc_buttons = {} # dict of buttons

        # sub frame location buttons frame
        self.location_buttons_frame = tk.Frame(self)

        # move button
        self.move_button = tk.Button(self, text="Move", command=self.toggle_loc_buttons)
        self.move_button.pack()

    def toggle_loc_buttons(self):
        """Determines the visibility of the location buttons."""
        if self.location_buttons_frame.winfo_ismapped():
            self.location_buttons_frame.pack_forget()
        else:
            self.location_buttons_frame.pack()
            self.location_buttons_frame.lift()
            self.update_buttons()

    def update_buttons(self):
        """Updates the visible location buttons for each possible route of a location."""
        for button in self.loc_buttons.values():
            button.destroy()  # destroys the existing buttons

        # creates the buttons for the next locations
        for loc in NESTED_DICT_LIST[player.current_location]['next_loc']:
            self.loc_buttons[loc] = tk.Button(self.location_buttons_frame,
                                              height=2,
                                              width=8,
                                              text=loc,
                                              command=lambda loc=loc:
                                              self.update_player_loc(loc))
            self.loc_buttons[loc].pack(side=tk.TOP)

    def update_player_loc(self, updated_loc):
        """Updates the player's location."""
        player.move(updated_loc)  # updates the player's location.
        self.app.output_frame.update_output(player.current_location)  # updates the output text box
        self.app.player_stats_frame.update_player_stats(player.inventory(), player.current_location)
        self.update_buttons()
        self.app.pick_up_frame.update_items()


class PickUp(tk.Frame):
    """A class for the frame containing item buttons and pick up button."""
    def __init__(self, master):
        super().__init__(master)

        self.app = master

        self.item_buttons = {}

        self.item_buttons_frame = tk.Frame(self)

        self.pick_up_button = tk.Button(self, text="Pick up item", command=self.toggle_item_buttons)
        self.pick_up_button.pack()

        self.update_items()

    def toggle_item_buttons(self):
        """Shows the item buttons."""
        if self.item_buttons_frame.winfo_ismapped():
            self.item_buttons_frame.pack_forget()
        else:
            self.item_buttons_frame.pack()
            self.update_items()

    def update_items(self):
        """Updates the visible item buttons depending on the player's location."""
        for button in self.item_buttons.values():
            button.destroy()

        # creates the item buttons
        for item in NESTED_DICT_LIST[player.current_location]['items']:
            button = tk.Button(self.item_buttons_frame,
                               height=2,
                               width=8,
                               text=item,
                               command=lambda item=item: self.update_player_inv(item))
            button.pack(side=tk.TOP)
            self.item_buttons[item] = button

    def update_player_inv(self, item):
        """Updates the player's inventory and item buttons."""
        player.pick_up(item)
        self.app.player_stats_frame.update_player_stats(player.inventory(), player.current_location)
        self.toggle_item_buttons()  # Toggle item buttons after picking up item


if __name__ == "__main__":
    player = Player('hero',['test','test','test','test','test','test'],100)
    goblin = Enemy('Goblin',[],100, 'A', dagger)
    gremlin = Enemy('Gremlin',[],100, 'A', bow)
    location = Location("A","a battlefield filled with corpses and rusty swords.",[],["B", "C"])
    app = App()
    app.mainloop()
