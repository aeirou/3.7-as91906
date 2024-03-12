from character import Player

#tutorial

locs_list = [
    {
    "locgit _name": "Spawn point",
    "desc": "Spawn point of the player",
    "items": " ",
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

    def add_locs(self):
        new_map = self.map.append(self.loc_name)
        return new_map
class Location:
    def __init__(self,loc_name,desc,items=None,next_loc=None,): #next_loc is the node and is set to 'None' by default — node will not lead to anywhere by default.
        self.loc_name = loc_name 
        self.desc = desc
        self.items = items
        self.next_loc = next_loc

    def __repr__(self): 
        return f"{self.loc_name} {self.desc} {self.next_loc}" 
    
    def get_loc(self):
        return self.loc_name

location = [Location(**locations) for locations in locs_list]
class Movement:
    def __init__(self):
        self.dirs = []
    
    def add_dirs(self):
        new_dirs = self.dirs.append()
        return new_dirs


    def player_move(self):
        pass
       
       
print(location)




