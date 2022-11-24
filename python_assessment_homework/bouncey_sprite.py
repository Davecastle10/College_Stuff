
def bounce(sprite, vertical):
	"""Bounces an object of a Sprite class. Vertical is a boolean that
	indicates if it bounces of a vertical wall. If False, sprite bounces
	off a horizontal surface. The Sprite objects have attributes dx and
	dy to represent their horizontal and vertical velocities."""
	# I have no clue what this wants
    direc = ""
    if vertical == True:
        direc = "vertically"
    else:
        direc = "horizontally"
    out = (f"the sprite bounces{direc} with a horizontal velosicty of {sprite.dx} and a vertical velocity of {sprite.dy}")
    return out
    # i have no clue what you wanted with this question Dave, i probably should have asked but Archie already did.
    

