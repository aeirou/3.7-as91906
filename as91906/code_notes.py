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