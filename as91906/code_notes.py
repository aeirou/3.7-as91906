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
