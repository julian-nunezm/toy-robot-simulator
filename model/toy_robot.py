class Robot():

    FACING_OPTIONS = [
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
    
    def __init__(self, x=None, y=None, facing=None):
        self._x = x
        self._y = y
        self._facing = facing

    def get_x(self):
        return self._x 
    
    def get_y(self):
        return self._y
    
    def get_facing(self):
        return self._facing
    
    def get_location(self):
        return (self._x, self._y)
    
    def is_valid_y_movement(self):
        return self._y in [0,1,2,3] if self._facing == 'NORTH' else self._y in [1,2,3,4]

    def is_valid_x_movement(self):
        return self._x in [0,1,2,3] if self._facing == 'EAST' else self._x in [1,2,3,4]
    
    def place(self, parameters):
        self._facing = parameters[2]
        if self._facing in self.FACING_OPTIONS:
            dimension = range(5)
            if int(parameters[0]) in dimension and int(parameters[1]) in dimension:
                self._x = int(parameters[0])
                self._y = int(parameters[1])
                return True
            else:
                self._x = None
                self._y = None
                self._facing = None
                return False
        return False
    
    def move(self):
        if self._facing == 'NORTH' and self.is_valid_y_movement():
            self._y += 1
            return True
        elif self._facing == 'EAST' and self.is_valid_x_movement():
            self._x += 1
            return True
        elif self._facing == 'SOUTH' and self.is_valid_y_movement():
            self._y -= 1
            return True
        elif self._facing == 'WEST' and self.is_valid_x_movement():
            self._x -= 1
            return True
        return False

    def left(self):
        try:
            index = self.FACING_OPTIONS.index(self._facing)
            new_index = (index - 1) % len(self.FACING_OPTIONS)
            self._facing = self.FACING_OPTIONS[new_index]
            return True
        except:
            return False
    
    def right(self):
        try:
            index = self.FACING_OPTIONS.index(self._facing)
            new_index = (index + 1) % len(self.FACING_OPTIONS)
            self._facing = self.FACING_OPTIONS[new_index]
            return True
        except:
            return False
    
    def report(self):
        return f'{self._x},{self._y},{self._facing}'
    