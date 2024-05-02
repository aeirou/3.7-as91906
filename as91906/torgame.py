"""Docstring for the imported modules."""
import tkinter as tk

# Location list.
NESTED_DICT_LIST = {
    "A":{
        "desc": "a battlefield filled with corpses and rusty swords.", # fight 
        "items": [],
        "enemy": " ",
        "next_loc": ["B"]
    },
    "B":{
        "desc": "a cozy looking wooden shack.",
        "items": [],
        "next_loc": ["A","C", "D"]
    },
    "C":{
        "desc": "an old ruin of a shack.",
        "items": [],
        "enemy": " ",
        "next_loc": ["B", "E",]
    },
    "D":{
        "desc": "a cave that hold an important treasure.",
        "items": [],
        "enemy": " ",
        "next_loc": ["B"]
    },
    "E":{
        "desc": "Gate to Floor 2",
        "items": [],
        "enemy": " ",
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

        self.weapon = fist

    def attack(self, target):
        """Attack methods for the class: Character

        Args:
            target (str): Target is a parameter which the damage is dealt to.
        """
        target.health -= self.weapon.damage


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
        if item in NESTED_DICT_LIST[self.current_location]['items']:
            self.inv.append(item)
            NESTED_DICT_LIST[self.current_location]['items'].remove(item) # Remove item from loc
            return self.inv

    # add if statement
    def equip(self, weapon):
        """Equip method for the player.

        Args:
            weapon (str): The chosen weapon for the player.
        """
        if weapon in self.inv:
            self.weapon = weapon


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
                damage=50,
                value=6)


bow = Weapon(name="Bow",
             item_desc="A short bow used by the Gremlins that wander the forest.",
             damage=8,
             value=8)


club = Weapon(name="Club",
             item_desc="A huge club on carried by high orcs.",
             damage=9,
             value=9)


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
NESTED_DICT_LIST["A"]["items"] = [old_sword, dagger]
NESTED_DICT_LIST["B"]["items"] = [sword]
NESTED_DICT_LIST["D"]["items"] = [key_floor_2]


goblin = Enemy('Goblin', ['Dagger'], 100, NESTED_DICT_LIST["C"]['enemy'], dagger)


gremlin = Enemy('Gremlin', ['Bow'], 100, NESTED_DICT_LIST["D"]['enemy'], bow)


high_orcs = Enemy('High Orcs', ['Club'], 100, NESTED_DICT_LIST["E"]['enemy'], club)


NESTED_DICT_LIST["C"]["enemy"] = goblin
NESTED_DICT_LIST["D"]["enemy"] = gremlin
NESTED_DICT_LIST["E"]["enemy"] = high_orcs


player = Player(name='hero',inv=[],health=100)


class App(tk.Tk):
    """Main app for the GUI."""
    def __init__(self):
        super().__init__()

        self.player = player

        self.title('Tower of Resuscitation')
        self.geometry('1200x900')

        self.title_label = tk.Label(self, text='Tower of Resuscitation', font=("Courier", 25))
        self.title_label.pack()

        self._frame = None # by default, no frame
        self.switch_frame(MainInt)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class MainInt(tk.Frame):
    """Main interface for the game."""
    def __init__(self, parent):
        super().__init__(parent)

        self.player = parent.player

        # Output frame
        self.output_frame = tk.Text(self,
                                    height=25,
                                    width=90,
                                    bg="black",
                                    fg="white",
                                    state="disabled")
        self.output_frame.pack()

        # Player stats frame
        self.player_stats_frame = tk.Text(self,
                                          fg="white",
                                          height="13px",
                                          state="disabled")
        self.player_stats_frame.pack()

        # Move buttons frame
        self.move_frame = tk.Frame(self)
        self.move_frame.pack()
        self.move_button = tk.Button(self.move_frame,
                                     text="Move",
                                     command=self.toggle_loc_buttons)
        self.move_button.pack()
        self.location_buttons_frame = tk.Frame(self.move_frame)

        # PickUp frame
        self.pick_up_frame = tk.Frame(self)
        self.pick_up_frame.pack()
        self.pick_up_button = tk.Button(self.pick_up_frame,
                                        text="Pick up item",
                                        command=self.toggle_item_buttons)

        self.pick_up_button.pack()
        self.item_buttons_frame = tk.Frame(self.pick_up_frame)

        tk.Button(self, text="Fight",
                  command=lambda: parent.switch_frame(Combat)).pack()

        # order of display
        self.update_output()
        self.update_player_stats()
        self.update_move_buttons()
        self.update_pick_up_buttons()

    def update_output(self):
        """Updates the output box."""
        self.output_frame.config(state='normal')
        self.output_frame.delete(tk.END)
        self.output_frame.insert('1.0',
                f"\n{player.name} is currently in location: {player.current_location}\n")
        self.output_frame.insert(tk.END, f"\n{self.loc_info()}\n")
        self.output_frame.config(state='disabled')

    def update_player_stats(self):
        """Updates the player stats text box."""
        self.player_stats_frame.config(state='normal')
        self.player_stats_frame.delete('1.0', tk.END)
        self.player_stats_frame.insert('1.0',
                            f"\nYou are currently in location: {player.current_location}\n")
        self.player_stats_frame.insert('3.0', f"\nInventory: {player.inventory()}\n")
        self.player_stats_frame.config(state='disabled')

    def update_move_buttons(self):
        """Updates the visible location buttons for each possible route of a location."""
        for widget in self.location_buttons_frame.winfo_children():
            widget.destroy()  # Destroy existing buttons

        for loc in NESTED_DICT_LIST[player.current_location]['next_loc']:
            button = tk.Button(self.location_buttons_frame,
                               height=2,
                               width=8,
                               text=loc,
                               command=lambda loc=loc: self.update_player_loc(loc))
            button.pack(side=tk.TOP)

    def toggle_loc_buttons(self):
        """Determines the visibility of the location buttons."""
        if self.location_buttons_frame.winfo_ismapped():
            self.location_buttons_frame.pack_forget()
        else:
            self.location_buttons_frame.pack()
            self.location_buttons_frame.lift()
            self.update_move_buttons()

    def update_player_loc(self, updated_loc):
        """Updates the player's location."""
        player.move(updated_loc)
        self.update_output()
        self.update_player_stats()
        self.update_move_buttons()
        self.update_pick_up_buttons()

    def update_pick_up_buttons(self):
        """Updates the visible item buttons depending on the player's location."""
        for widget in self.item_buttons_frame.winfo_children():
            widget.destroy()  # Destroy existing buttons

        for item in NESTED_DICT_LIST[player.current_location]['items']:
            button = tk.Button(self.item_buttons_frame,
                               height=2,
                               width=8,
                               text=item,
                               command=lambda item=item: self.update_player_inv(item))
            button.pack(side=tk.TOP)

    def update_player_inv(self, item):
        """Updates the player's inventory."""
        player.pick_up(item)
        self.update_output()
        self.update_player_stats()
        self.update_move_buttons()
        self.update_pick_up_buttons()

    def toggle_item_buttons(self):
        """Shows the item buttons."""
        if self.item_buttons_frame.winfo_ismapped():
            self.item_buttons_frame.pack_forget()
        else:
            self.item_buttons_frame.pack()
            self.update_pick_up_buttons()

    def loc_info(self):
        """Returns the location's info."""
        loc_info = NESTED_DICT_LIST[player.current_location]
        desc = f"{player.name} is currently at {loc_info['desc']}"
        items = loc_info['items']
        next_locs = f"{player.name}'s next routes are: {' '.join(loc_info['next_loc'])}"
        return f"{desc}\n{items}\n{next_locs}"


class Combat(tk.Frame):
    """Combat frame for the player."""
    def __init__(self, parent):
        super().__init__(parent)


        self.player = parent.player
        self.switch_frames = parent.switch_frame

        tk.Label(self, text=f"{player.name} is fighting!",
                 font=("Courier", 20)).pack(side="top", fill="x", padx=50)

        # buttons and labels for the combat frame
        self.health = tk.Label(self, text=f"HP: {player.health}",
                 font=("Courier", 20))
        self.weapon_dmg = tk.Label(self, text=f"Damage: {player.weapon.damage}",
                 font=("Courier", 20))
        self.weapon = tk.Label(self, text=f"Weapon: {player.weapon.name}",
                 font=("Courier", 20))
        self.fight_frame = tk.Text(self,
                                    height=25,
                                    width=90,
                                    bg="black",
                                    fg="white",
                                    state="disabled")
        self.return_to_adventure = tk.Button(self, height=5,text="Return to adventure",
                                             command=lambda: parent.switch_frame(MainInt))
        self.flee = tk.Button(self, height=5,text="Flee",
                              command=lambda: parent.switch_frame(MainInt))
        self.attack = tk.Button(self, height=5,
                text="Attack",
                command=lambda: [player.attack(NESTED_DICT_LIST[player.current_location]['enemy']),
                                NESTED_DICT_LIST[player.current_location]['enemy'].attack(player),
                                self.update_stats(),
                                self.update_fight_frame(),
                                self.character_dead()])


        self.equip_buttons = []  # List to store Equip buttons for each item


        for item in self.player.inv:
            equip_button = tk.Button(self, height=5, text="Equip",
                    command=lambda item=item: [self.equip_item(item),self.update_stats()])
            self.equip_buttons.append(equip_button)

        for buttons in self.equip_buttons:
            buttons.pack(side='bottom')


        # shhow the buttons and labels
        self.health.pack(side="bottom", fill="x", padx=50 ,pady=10)
        self.weapon_dmg.pack(side="bottom", fill="x",padx=50 ,pady=10)
        self.weapon.pack(side="bottom", fill="x",padx=50 ,pady=10)
        self.fight_frame.pack(side="bottom",fill='both')
        self.return_to_adventure.pack(side=tk.TOP,expand=True, fill='both')
        self.flee.pack(side=tk.TOP, expand=True, fill='both',)
        self.attack.pack(side='top')


    def equip_item(self, item):
        """Method for when the player equips an item"""
        self.player.equip(item)


    def update_fight_frame(self):
        """Text output for the fight frame box."""
        self.fight_frame.config(state='normal')
        self.fight_frame.delete(tk.END)
        self.fight_frame.insert('1.0',
                                f"\n{player.name} has dealt {player.weapon.damage} to {NESTED_DICT_LIST[player.current_location]['enemy'].name} \n")
        self.fight_frame.insert('1.0',
                                f"\n{NESTED_DICT_LIST[player.current_location]['enemy'].name} has dealt {NESTED_DICT_LIST[player.current_location]['enemy'].weapon.damage} to {self.player.name} \n")
        self.fight_frame.config(state='disabled')

    def update_stats(self):
        """Updates the text label health of the player."""
        new_health = f"HP: {self.player.health}"
        self.health.configure(text=new_health)

        new_weapon = f"Weapon: {self.player.weapon.name}"
        self.weapon.configure( text=new_weapon)

        new_damage = f"Damage: {self.player.weapon.damage}"
        self.weapon_dmg.configure(text=new_damage)

    def character_dead(self):
        """swtiches frames when the player dies."""
        if self.player.health <= 0:
            self.switch_frames(GameOver)


class GameOver(tk.Frame):
    """A frame for when the player dies."""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        tk.Label(self, text="GAME OVER!",
                 font=("Courier", 50)).pack(side="top", fill="x", padx=50)
        



def main():
    """Create the main app"""
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
