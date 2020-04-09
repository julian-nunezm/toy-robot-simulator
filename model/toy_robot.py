class Robot:

    _x = _y = None
    _facing = None
    warning = None
    # TODO: start = False ?

    FACING_OPTIONS = [
        # TODO: Move right = index + 1
        # TODO: Move left = index - 1
        'NORTH',
        'EAST',
        'SOUTH',
        'WEST'
    ]

    COMMAND_OPTIONS = [
        'PLACE',
        'MOVE',
        'LEFT',
        'RIGHT',
        'REPORT'
    ]

    def __init__(self, x, y, facing):
        self._x = x
        self._y = y
        self._facing = facing
    
    def get_location(self):
        return (self._x, self._y)
    
    def get_facing(self):
        return self._facing
    
    def move(self):
        if self._facing == 'NORTH' and self.is_valid_y_movement():
            self._y += 1
        elif self._facing == 'EAST' and self.is_valid_x_movement():
            self._x += 1
        elif self._facing == 'SOUTH' and self.is_valid_y_movement():
            self._y -= 1
        elif self._facing == 'WEST' and self.is_valid_x_movement():
            self._x -= 1
        else:
            self.warning = f'If I move to the {self._facing.capitalize()}, I could die. :('
            # print(self.warning)

    def is_valid_y_movement(self):
        return self._y in [1,2,3]

    def is_valid_x_movement(self):
        return self._x in [1,2,3] 