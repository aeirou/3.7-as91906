def foo():
    from torgame import locs_list, Location
    locs_list()

class Player:
    def __init__(self, name, health, dmg, current_loc):
        self.name = name
        self.health = health
        self.dmg = dmg
        self.current_loc = current_loc
    
    #makes the default location the spawn point for both the tutorial and the main game
    def default_loc(self):
        self.current_loc = locs_list[0]
