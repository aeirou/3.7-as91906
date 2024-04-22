#this will split up the list of dictionary and pair the stuff in it with the stuff in the class 'Location'
#[
# { "name": A ==> self.name = name
#  "desc": "Spawn point" ==> self.desc = desc
#  "next_loc": A,B,C ==> self.next_loc = next_loc }
#]
# location = [Location(**locations) for locations in locs_list]


#class Location:
#location is the object which contains attributes and methods (defs')

#this code turns object into readable lines.
#def __repr__(self): 
        # return f"{self.name} {self.desc} {self.next_loc}"  — f strings

#names with leading underscore '_' eg 'self._name' means that, that attribute or method is intended to be used inside of the class.

# test = Player("B", 10, 10, "you are currently in location b")
# print(test.location)
# test.location = "you have moved onto location c"
# print(test.location)



# def move(self,locs_list):
#         """
#             A method so the player can move from locatioon to the other, based on the player's input.
#         """
#         next_loc = input(str("Where would you like to go? ")).upper()

#         for loc in locs_list:
#             if loc["loc_name"] == self._location:
#                 if next_loc in loc["next_loc"]:
#                     self._location = next_loc # <-- player's destination becomes player's current location.
#                     return next_loc
#         return False


#print player's destination and current location.
# for loc in locs_list:
#     if player.next_loc in loc["next_loc"]:
#         player = Player("aeirone",10,10, loc["next_loc"])
#         print(player)

# def player_move_loop():
#     """
#         Loop for player to move.
#     """
#     player = Player("aeirone", 10, 10, "Spawn Point")

#     for loc in locs_list:
#         dest = input(str("Where would you like to go?")).upper()

#         if dest in loc["next_loc"]:
#             player = Player("aeirone", 10, 10, dest)
#             print(player)

#         if dest not loc["next_loc"]:


# player_move_loop()

# class Player:
#     """ 
#     Player's attributes. 
#     """

#     def __init__(self, name, health, dmg, location):
#         self.name = name
#         self.health = health
#         self.max_health = health
#         self.dmg = dmg
#         self._location = location  # current

#     def attack(self, target):
#         """Attack method.

#         Returns:
#             target (str): Health of player and enemy. 
#         """
#         target.health -= self.dmg
#         target.health = max(target.health, 0) # prevents health from going below 0.

#     @property
#     def location(self):
#         """ Gets the location.
        
#         Returns:
#             str: location of the player.
#         """
#         return self._location

#     @location.setter
#     def location(self, new_loc):
#         self._location = new_loc

#     def move(self):
#         """Move method for player.

#         Returns:
#             str: new location of player
#         """
#         dest = input(str("Where would you like to go?")).upper()

#         for loc in locs_list:
#             # if player's dest in next_loc
#             if dest in loc["next_loc"]:
#                 self._location = dest

#                 return dest

#             return False

#     def __repr__(self):
#         """
#             Prints out player name, health, dmg and current location.
#         """
#         return f"{self.name} {self.health} {self.dmg} {self._location}"

# # def error():
# #     """
# #         If check loc is False
# #     """
# #     while check_loc is False:
# #         print("Sorry but this is an invalid location. Try again: ")
# #         player.move()
# #         if check_loc: # fix to break the loop.
# #             print(player)


# player = Player("aeirone", 100, 10, "Spawn Point")
# enemy = Player("marcus", 100, 5, "Spawn Point")

# while True:
#     player.attack(enemy)
#     enemy.attack(player)

#     print (f"The health of {player.name}: is {player.health}.")
#     print (f"The health of {enemy.name}: is {enemy.health}.")

#     input()


