#this will split up the list of dictionary and pair the stuff in it with the stuff in the class 'Location'
#[
# { "name": A ==> self.name = name
#  "desc": "Spawn point" ==> self.desc = desc
#  "next_loc": A,B,C ==> self.next_loc = next_loc }
#]
# location = [Location(**locations) for locations in locs_list]