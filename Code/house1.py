#! /usr/bin/python
"""house.py -- A house program.  """

class House(object):
    """Some stuff """
my_house = House() # class instantiation
my_house.number = 40 # data attribute
my_house.rooms = 8
my_house.garden = 1
	
print "My house is number", my_house.number
print "It has", my_house.rooms, "rooms"
if my_house.garden:
	garden_text = "has"
else:
	garden_text = "does not have"
	print "It", garden_text, "a garden"
