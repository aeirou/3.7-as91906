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
class Map:
    def __init__(self):
        self.map = [] 

class Location:
    #next_loc is the node and is set to 'None' by default — node will not lead to anywhere by default.
    def __init__(self,loc_name,desc,items=None,next_loc=None,): 
        self.loc_name = loc_name 
        self.desc = desc
        self.items = items
        self.next_loc = next_loc

    def __repr__(self): return f"{self.loc_name} {self.desc} {self.items} {self.next_loc}" 
    
location = [Location(**locations) for locations in locs_list]

#names with leading underscore '_' eg 'self._name' means that, that attribute or method is intended to be used inside of the class.
class Player:
    def __init__(self, name, health, dmg, location):
        self._name = name
        self._health = health
        self._dmg = dmg
        self._default_loc = locs_list[0]
        self._location = location #current
    
    #gets the current location
    @property
    def location(self): return self._location

    #sets the current location -- sets the changed location.
    @location.setter
    def location(self, new_loc): self._location = new_loc

test = Player("B", 10, 10, "you are currently in location b")
print(test.location)
test.location = "you have moved onto location c"
print(test.location)
