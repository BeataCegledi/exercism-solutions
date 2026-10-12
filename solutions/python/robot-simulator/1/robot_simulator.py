"""Robot simulator that tracks direction and position, responding to movement commands."""

# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot:
    
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        """Initialize robot with direction and starting coordinates.
        # direction defaults to NORTH
        # coordinates default to (0, 0)
        """
        self.direction = direction
        self.coordinates = (x_pos,y_pos)

    def move(self, movement):       
        """Process movement string and update direction or position.
        # 'R' turns right, 'L' turns left
        # 'A' advances one step in current direction
        # raises ValueError for invalid characters
        """
        if not set(movement) <= set("rlaRLA"):
            raise ValueError("Invalid movement")
        else:
            links = [EAST, NORTH, WEST, SOUTH]
            rechts = [EAST, SOUTH, WEST, NORTH]
            for letter in movement:
                if letter.upper() == "R":
                    self.direction = rechts[(rechts.index(self.direction)+1)%4]
                elif letter.upper() == "L":
                    self.direction = links[(links.index(self.direction)+1)%4]
                elif letter.upper() == "A":
                    self.coordinates = tuple(a + b for a, b in zip(self.coordinates, self.direction))
    