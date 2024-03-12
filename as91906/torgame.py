from tkinter import Tk

locs_list = [
    {
    "loc_name": "Spawn point",
    "desc": "Spawn point of the player",
    "items": "None",
    "next_loc": "B"
},
{
    "loc_name": "Point B",
    "desc": "Area lies a hidden chest.",
    "items": "a sword",
    "next_loc": "C"
}
]

class Game:
    pass

class Map:
    def __init__(self):
        self.map = [] 

class Location:
    def __init__(self,loc_name,desc,items=None,next_loc=None,): #next_loc is the node and is set to 'None' by default — node will not lead to anywhere by default.
        self.loc_name = loc_name 
        self.desc = desc
        self.items = items
        self.next_loc = next_loc

    def __repr__(self): 
        return f"{self.loc_name} {self.desc} {self.items} {self.next_loc}" 

location = [Location(**locations) for locations in locs_list]

#names with leading underscore '_' eg 'self._name' means that, that attribute or method is intended to be used inside of the class.
class Player:
    def __init__(self, name, health, dmg, default_loc, current_loc):
        self._name = name
        self._health = health
        self._dmg = dmg
        self._default_loc = locs_list[0]
        self._location = location #current
    
    #gets the current location
    @property
    def location(self): return self._current_loc

    #sets the current location
    @location.setter
    def location(self, new_loc): self._current_loc = new_loc

player = Player("test", 100, 200, default_loc=locs_list[0], )


# print(Player.default_loc)
# print(location)





