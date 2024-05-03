"""A short RPG game text-based game using Tkinter as a GUI.
By Aeirone Felipe

Last modified: 3 May 2024
"""
import tkinter as tk

# Location list.
NESTED_DICT_LIST = {
    "A":{
        "desc": "a battlefield filled with corpses and rusty swords.", 
        "items": [],
        "enemy": '',
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
        "enemy": '',
        "next_loc": ["B", "E",]
    },
    "D":{
        "desc": "a cave that hold an important treasure.",
        "items": [],
        "enemy": '',
        "next_loc": ["B"]
    },
    "E":{
        "desc": "Gate to the top",
        "items": [],
        "enemy": '',
        "next_loc": ["C"]
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
        self.current_location = current_location

        self.weapon = fist # default weapon is fist

    def attack(self, target):
        """Attack methods for the class: Character

        Args:
            target (str): Target is a parameter which the damage is dealt to.
        """
         # target's health - the damage output of the weapon
        target.health -= self.weapon.damage


class Player(Character):

    """Player's attributes."""

    def __init__(self, name, inv, health):
        super().__init__(name=name, inv=inv, health=health, current_location='A')

        self.default_weapon = self.weapon # sets the default weapon


    def inventory(self):
        """Checks if inventory is empty."""
        if self.inv:
        # check if the inventory contains instances of Weapon
            weapon_names = [item.name for item in self.inv if isinstance(item, Weapon)]
            if weapon_names:
                return f"{', '.join(weapon_names)}"
            else:
                return f"Nothing in {self.name}'s inventory."
        return f"Nothing in {self.name}'s inventory."

    def pick_up(self, item):
        """Method for adding items into the player's inventory.

        Returns:
            str: The items in the player's inventory.
        """
        # checks if the item is in the list of the items in the current location of the player.
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
        # checks if weapon is in the player's inventory then sets it as the weapon
        if weapon in self.inv:
            self.weapon = weapon

    def move(self, dest):
        """Move method for player: Checks if the new location is
           available from the current location of the player.

        Returns:
            dest (str): The new location of the player.
        """
        # checks if dest is in the value: 'next_loc' of the current location
        if dest in NESTED_DICT_LIST[self.current_location]["next_loc"]:
            self.current_location = dest # sets dest to the current location
            return dest
        return False

    def check_items(self, loc):
        """Checks if there are any items in the location.
        """
        if loc:
            if isinstance(loc, list):  # check if loc is a list
                item_names = []
                for item in loc:
                    if isinstance(item, Weapon):
                        item_names.append(item.name)
                    else:
                        item_names.append(str(item))  # Convert non-Weapon items to string
                return f"{self.name} has found: {', '.join(item_names)}"
        return "There are no obtainable items in this location."


class Enemy(Character):
    """A subclass for the character class — the enemy. 
    """
    def __init__(self, name, inv, health, current_location, weapon):
        """_summary_

        Args:
            name (str): the name of the enemy.
            health (int): the health of the enemy
            current_location (str): the current location of the enemy (where they are set to).
            weapon (object): the weapon object the enemy holds.
        """
        super().__init__(name, inv, health, current_location)
        self.weapon = weapon


class Item:
    """The items (including weapons) the character use."""
    def __init__(self, name, item_desc, damage, value):
        """Initialises name, item_desc, damage and value

        Args:
            name (str): name of the item
            item_desc (str): the description of the item
            damage (int): the damage input of the item
            value (int): the value of the item
        """
        self.name = name
        self.item_desc = item_desc
        self.damage = damage
        self.value = value

    def __str__(self):
        """String representation of the Weapon object."""
        return f"{self.name}, {self.item_desc}, {self.damage}, {self.value}"


class Weapon(Item):
    """Subclass for weapons from the superclass Items.

    Args:
        Item (str)): Item is a superclass which the Weapon class uses as a blueprint.
    """
    def __init__(self, name, item_desc, damage, value):
        super().__init__(name=name, item_desc=item_desc, damage=damage, value=value)

    def __str__(self):
        """String representation of the Weapon object."""
        return f"{self.name}, {self.item_desc}, {self.damage}, {self.value}"


# weapon and item objects for the player and the enemies
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
             damage=8,
             value=8)


club = Weapon(name="Club",
             item_desc="A huge club on carried by high orcs.",
             damage=10,
             value=9)


sword = Weapon(name="Sword",
                   item_desc="A silver sword which was taken from a dead knight.",
                   damage=11,
                   value=11)


key_floor_3 = Item(name="Gold Key",
                   item_desc="A gold key to Floor 3",
                   damage=0,
                   value=20)


# adds the items into the 'items' key of the specific location.
NESTED_DICT_LIST["A"]["items"] = [old_sword, dagger]
NESTED_DICT_LIST["B"]["items"] = [sword]
NESTED_DICT_LIST["D"]["items"] = [key_floor_3]


# enemy objects for the enemy subclass - the enemies the player will encounter.
goblin = Enemy(name='Goblin',
               inv=["Dagger"],
               health=100,
               current_location=NESTED_DICT_LIST["D"]['enemy'],
               weapon=dagger)


gremlin = Enemy(name='Gremlin',
                inv=["Bow"],
                health=100,
                current_location=NESTED_DICT_LIST["C"]['enemy'],
                weapon=bow)


high_orc = Enemy(name='High Orc',
                 inv=["Club"],
                 health=100,
                 current_location=NESTED_DICT_LIST["E"]['enemy'],
                 weapon=club)

# adds the enemy into the 'enemy' key of the specific location.
NESTED_DICT_LIST["C"]["enemy"] = goblin
NESTED_DICT_LIST["D"]["enemy"] = gremlin
NESTED_DICT_LIST["E"]["enemy"] = high_orc


# instantiates the player subclass
player = Player(name='Hero',inv=[],health=100)


class App(tk.Tk):
    """Main app for the GUI."""
    def __init__(self):
        super().__init__()

        # calls the instance: player
        self.player = player

        self.title('Tower of Resuscitation') # window title
        self.geometry('1400x800') # window size
        self.resizable(False, False) # makes the window fixed

        # the grid of the window
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # label
        self.title_label = tk.Label(self,
                                    text='Tower of Resuscitation',
                                    font=("Courier", 40),
                                    pady=30)
        self.title_label.pack()

        # a method to swtich frames currently shown
        self._frame = None # by default, no frame

        # passes the frames as a parameter
        self.switch_frame(StartWindow)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None: # if a frame is showing, it destroys it
            self._frame.destroy()
        self._frame = new_frame # sets the frame to the new frame
        self._frame.pack() # shows the frame


class StartWindow(tk.Frame):
    """Starting interface for the game."""
    def __init__(self, parent):
        super().__init__(parent)

        self.switch_frame = parent.switch_frame

        tk.Label(self, text="Welcome to TOR!",
                 font=("Courier", 20)).grid(row=0, column=0, padx=50, pady=10)
        tk.Label(self, text="Press 'Play' to start.",
                 font=("Courier", 20)).grid(row=1, column=0, padx=50, pady=10)

        # this button destroys the frame and switches it with the frame EnterName
        tk.Button(self,
                  height=3,
                  text="Play",
                  command=lambda: self.switch_frame(EnterName)).grid(row=2,
                                                                     column=0,
                                                                     padx=50,
                                                                     pady=50)


class EnterName(tk.Frame):
    """Frame for the player's name."""
    def __init__(self, parent):
        super().__init__(parent)

        # inherits the instantiation from the class App.
        self.player = parent.player

        # inherits the method switch_frame() to switch frame
        self.switch_frame = parent.switch_frame

        # take the player's name input
        tk.Label(self, text="Enter your name:",
                 font=("Courier", 20)).grid(row=0, column=0, padx=50, pady=50)
        player_name = tk.StringVar() # passes it to StringVar()
        self.player_name_entry = tk.Entry(self, bg='white',
                                          fg='black',
                                          textvariable=player_name,
                                          font=('calibre', 10, 'normal'))
        self.player_name_entry.grid(row=1, column=0, pady=50)

        tk.Button(self, text="Enter", height=4,
                  command=lambda name_var=player_name: self.submit(name_var)).grid(row=2, column=0)

    def submit(self, name_var):
        """Sets the name of the player."""
        # from the variable name_var, it gets the player's name input.
        self.player.name = name_var.get()
        self.switch_frame(MainInt) # switches frame to MainInt


class MainInt(tk.Frame):
    """Main interface for the game."""
    def __init__(self, parent):
        super().__init__(parent)

        self.player = parent.player

        # Output frame - main text box for the MainInt
        self.output_frame = tk.Text(self,
                                    height=25,
                                    width=84,
                                    bg="gray",
                                    fg="black",
                                    state="disabled")
        self.output_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # creates a scrollbar for the output box text frame.
        self.text_scrollbar = tk.Scrollbar(self,
                                           orient="vertical",
                                           command=self.output_frame.yview)
        self.text_scrollbar.grid(row=0, column=2, sticky="ns")
        self.output_frame.config(yscrollcommand=self.text_scrollbar.set) # scroll command

        # Player stats frame which contains inv and player's current loc
        self.player_stats_frame = tk.Text(self,
                                          fg="white",
                                          height="13px",
                                          state="disabled")
        self.player_stats_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        # frame for the move button
        self.move_frame = tk.Frame(self)
        self.move_frame.grid(row=2, column=0, pady=10)
        self.move_button = tk.Button(self.move_frame,
                                     text="Move",
                                     command=self.toggle_loc_buttons)
        self.move_button.grid(row=0, column=0, padx=10)

        # frame for the chilren buttons which are toggled by the parent: self.move_button
        self.location_buttons_frame = tk.Frame(self.move_frame)

        # PickUp frame
        self.pick_up_frame = tk.Frame(self)
        self.pick_up_frame.grid(row=2, column=1, pady=10)
        self.pick_up_button = tk.Button(self.pick_up_frame,
                                        text="Pick up item",
                                        command=self.toggle_item_buttons)
        self.pick_up_button.grid(row=0, column=0, padx=10)
        # frame for the chilren buttons which are toggled by the parent: self.pick_up_button
        self.item_buttons_frame = tk.Frame(self.pick_up_frame)

        # fight button which switches the frame into class Combat()
        self.fight_button = tk.Button(self,
                                      text="Fight",
                                      command=lambda: parent.switch_frame(CombatFrame))


        # initiates the methods
        self.update_output()
        self.update_player_stats()
        self.update_move_buttons()
        self.update_pick_up_buttons()

    def check_for_enemy(self, current_location):
        """Check if there is an enemy in the current location to show the fight button."""
        if NESTED_DICT_LIST[current_location].get('enemy'):
            self.fight_button.grid(row=3, column=0, columnspan=2, pady=10)
            self.output_frame.config(state='normal')
            self.output_frame.insert(tk.END,
                                     f"\nYou have found a {NESTED_DICT_LIST[self.player.current_location]['enemy'].name}! Click 'fight' to initiate battle!\n")
            self.output_frame.config(state='disabled')
            self.output_frame.yview_moveto(1.0) # scrolls to the most recent text in the text box.
        else:
            self.fight_button.grid_forget() # if no enemy, it hides the button

    def update_output(self):
        """Updates the content output box."""
        self.output_frame.config(state='normal')
        self.output_frame.insert(tk.END, f"\n{self.loc_info()}\n")
        self.output_frame.config(state='disabled')

        # automatically scroll down to the bottom
        self.output_frame.yview_moveto(1.0) # scrolls to the most recent text in the text box.

    def update_player_stats(self):
        """Updates the content in player stats text box."""
        self.player_stats_frame.config(state='normal') # enables editing
        self.player_stats_frame.delete('1.0', tk.END) # deletes everything from line 1 to end
        self.player_stats_frame.insert('1.0',
                                       f"\nYou are currently in location: {player.current_location}\n")
        self.player_stats_frame.insert('3.0', f"\nInventory: {player.inventory()}\n") # inserts player's inventory
        self.player_stats_frame.config(state='disabled') # disables editing

    def update_move_buttons(self):
        """Updates the visible location buttons for each possible route of a location."""

        # this destroys the buttons made from the previous 'next locations'
        for widget in self.location_buttons_frame.winfo_children(): # a list containing widgets
            widget.destroy()  # destroys those existing widgets

        # creates a for loop to create each buttons for each locs available from the current loc.
        for loc in NESTED_DICT_LIST[player.current_location]['next_loc']:
            button = tk.Button(self.location_buttons_frame,
                               height=2,
                               width=8,
                               text=loc,
                               command=lambda loc=loc: [self.update_player_loc(loc), # moves player
                                                # checks if there are enemies in the loc
                                                self.check_for_enemy(self.player.current_location)])
            button.pack(side="left", padx=5, pady=5)

    def toggle_loc_buttons(self):
        """Determines the visibility of the location buttons."""

        # if the buttons are mapped, they are hidden
        if self.location_buttons_frame.winfo_ismapped():
            self.location_buttons_frame.grid_forget()
        else:
            self.location_buttons_frame.grid(row=2, column=1, pady=10, sticky="w")
            self.update_move_buttons()

    def update_player_loc(self, updated_loc):
        """Updates the player's location."""
        # calls the method from the class Player() to move the player
        player.move(updated_loc)
        self.update_output()
        self.update_player_stats()
        self.update_move_buttons()
        self.update_pick_up_buttons()

    def update_pick_up_buttons(self):
        """Updates the visible item buttons depending on the player's location."""
        # check if there are items in the current location
        if NESTED_DICT_LIST[player.current_location]['items']:
            # destroys the previous item buttons of the previous location
            for widget in self.item_buttons_frame.winfo_children():
                widget.destroy()

            # creates buttons for each item vlues present in the key 'items'
            for item in NESTED_DICT_LIST[player.current_location]['items']:
                button = tk.Button(self.item_buttons_frame,
                                height=2,
                                width=8,
                                text=item.name,
                                command=lambda item=item: self.update_player_inv(item))
                button.pack(side="left", padx=5, pady=5)
            
            # display the pick up button
            self.pick_up_button.grid(row=0, column=0, padx=10)
            self.item_buttons_frame.grid(row=1, column=0, pady=10, sticky="w")
        else:
            # if there are no items hide the pick up button
            self.pick_up_button.grid_forget()
            self.item_buttons_frame.grid_forget()


    def update_player_inv(self, item):
        """Updates the player's inventory."""
        # uses the method from the Player() to pick up an item
        player.pick_up(item)
        self.update_output()
        self.update_player_stats()
        self.update_move_buttons()
        self.update_pick_up_buttons()

    def toggle_item_buttons(self):
        """Shows the item buttons."""
        # if the item buttons are shown, it hides it
        if self.item_buttons_frame.winfo_ismapped():
            self.item_buttons_frame.grid_forget()
        else:
            self.item_buttons_frame.grid(row=3, column=1, pady=10, sticky="w")
            self.update_pick_up_buttons()

    def loc_info(self):
        """Returns the location's info."""
        # a method for the current location's information
        loc_info = NESTED_DICT_LIST[self.player.current_location] # calls player's current location
        location = f"{self.player.name} is currently in location: {self.player.current_location}\n"
        desc = f"{self.player.name} is currently at {loc_info['desc']}"
        items = player.check_items(loc_info['items'])
        next_locs = f"{self.player.name}'s next routes are: {' '.join(loc_info['next_loc'])}"

        return f"{location}\n{desc}\n{items}\n{next_locs}"


class CombatFrame(tk.Frame):
    """Combat frame for the player."""
    def __init__(self, parent):
        super().__init__(parent)

        # inherits the player class
        self.player = parent.player
        # inherits the switch_frames method
        self.switch_frames = parent.switch_frame

        tk.Label(self, text=f"{player.name} is fighting {NESTED_DICT_LIST[self.player.current_location]['enemy'].name}!",
                 font=("Courier", 20)).grid(row=1, column=1, padx=100, pady=10)

        # buttons and labels for the combat frame
        # player's health
        self.health = tk.Label(self, text=f"HP: {self.player.health}",
                               font=("Courier", 20))
        # enemy's health
        self.enemy_health = tk.Label(self,
                                     text=f"{NESTED_DICT_LIST[self.player.current_location]['enemy'].name} HP: {NESTED_DICT_LIST[self.player.current_location]['enemy'].health}",
                               font=("Courier", 20))
        # weapon damage display
        self.weapon_dmg = tk.Label(self, text=f"Damage: {self.player.weapon.damage}",
                                   font=("Courier", 20))
        # weapon currently is being used
        self.weapon = tk.Label(self, text=f"Weapon: {self.player.weapon.name}",
                                font=("Courier", 20))
        # text box for the fight info
        self.fight_frame = tk.Text(self,
                                   height=25,
                                   width=90,
                                   bg="black",
                                   fg="white",
                                   state="disabled")
        # scroll bar for the text box
        self.text_scrollbar = tk.Scrollbar(self,
                                           orient="vertical",
                                           command=self.fight_frame.yview)
        self.text_scrollbar.grid(row=4, column=0, sticky="ns")
        self.fight_frame.config(yscrollcommand=self.text_scrollbar.set) # scroll command

        # attack button which updates stats, text box, checks if player is dead and if player won
        self.attack = tk.Button(self, height=5,
                                text="Attack",
                                command=lambda: [self.player.attack(NESTED_DICT_LIST[self.player.current_location]['enemy']),
                                                 NESTED_DICT_LIST[player.current_location]['enemy'].attack(player),
                                                 self.update_stats(),
                                                 self.update_fight_frame(),
                                                 self.character_dead(),
                                                 self.if_win()])

        # a list to store the weapons button to equip
        self.equip_buttons = []

        # creates button for each item in the inventory
        for item in self.player.inv:
            equip_button = tk.Button(self, height=4, text=item.name,
                                      command=lambda item=item: [self.equip_item(item),
                                                                 self.update_stats()])
            self.equip_buttons.append(equip_button) # appends to the list of buttons

        # displays the list of buttons
        for index, button in enumerate(self.equip_buttons):
            button.grid(row=index + 4, column=3)

        # order of the widgets
        self.health.grid(row=1, column=0, padx=50,)
        self.enemy_health.grid(row=2, column=0, padx=50,)
        self.weapon.grid(row=2, column=1, padx=50, pady=10)
        self.weapon_dmg.grid(row=2, column=2, padx=50,)
        self.fight_frame.grid(row=4, column=0, columnspan=3)
        self.attack.grid(row=5, column=0, columnspan=2)

    def equip_item(self, item):
        """Method for when the player equips an item"""
        # calls the method from the player class to set the player's weapon to the parameter: item
        self.player.equip(item)

    def update_fight_frame(self):
        """Text output for the fight frame box."""
        self.fight_frame.config(state='normal') # enables editing
        self.fight_frame.insert(tk.END,
        f"\n{player.name} has dealt {player.weapon.damage} to {NESTED_DICT_LIST[player.current_location]['enemy'].name} \n")
        self.fight_frame.insert(tk.END,
        f"\n{NESTED_DICT_LIST[player.current_location]['enemy'].name} has dealt {NESTED_DICT_LIST[player.current_location]['enemy'].weapon.damage} to {self.player.name} \n")
        self.fight_frame.config(state='disabled') # disables editing

    def update_stats(self):
        """Updates the text label health of the player."""
        # updates the health of player
        new_health = f"HP: {self.player.health}"
        self.health.configure(text=new_health)

        # updates the health of the enemy
        new_enemy_health = f"{NESTED_DICT_LIST[self.player.current_location]['enemy'].name} HP: {NESTED_DICT_LIST[self.player.current_location]['enemy'].health}"
        self.enemy_health.configure(text=new_enemy_health)

        # updates the weapon being used
        new_weapon = f"Weapon: {self.player.weapon.name}"
        self.weapon.configure(text=new_weapon)

        # updates the new damage output of the player
        new_damage = f"Damage: {self.player.weapon.damage}"
        self.weapon_dmg.configure(text=new_damage)

    def character_dead(self):
        """swtiches frames when the player dies."""

        # if player's health is equal or below 0, frame switches to the class frame Gameover
        if self.player.health <= 0:
            self.switch_frames(GameOver)
        # if enemy's health is equal or below 0, can return and continue adventure
        elif NESTED_DICT_LIST[self.player.current_location]['enemy'].health <= 0:
            self.return_adventure = tk.Button(self,
                                              height=4,
                                              text="Return",
                                              command=lambda: self.switch_frames(MainInt))
            self.return_adventure.grid(row=6, column=0, columnspan=2)
            self.fight_frame.config(state='normal')
            self.fight_frame.insert('1.0',
            f"\nYou have defeated {NESTED_DICT_LIST[player.current_location]['enemy'].name}! \n")
            self.fight_frame.config(state='disabled')
            enemy_dead = f"{NESTED_DICT_LIST[self.player.current_location]['enemy'].name} has died"
            self.enemy_health.configure(text=enemy_dead) # changes enemy health to - enemy's death
            self.attack.grid_forget() # hides the attack button


    def if_win(self):
        """Switches window when the player beats the boss."""
        # when the boss's health equals to 0 or goes below 0, player wins
        if high_orc.health <= 0: 
            self.switch_frames(WinFrame) # swtiches frames when conditions are met

class WinFrame(tk.Frame):
    """A frame for when the player beats the boss - wins the game."""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # label for when the player wins the game.
        tk.Label(self, text="YOU HAVE REACHED THE TOP OF THE TOWER!",
                 font=("Courier", 50)).pack(side="top", fill="x", padx=50)

class GameOver(tk.Frame):
    """A frame for when the player dies."""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # label for when the player loses to any enemies
        tk.Label(self, text="GAME OVER!",
                 font=("Courier", 50)).pack(side="top", fill="x", padx=50)


def main():
    """Create the main app"""
    app = App() # instantiates the class App
    app.mainloop()


if __name__ == "__main__":
    main() # iterates the class App.
