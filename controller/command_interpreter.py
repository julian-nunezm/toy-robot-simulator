from model.toy_robot import Robot


class Controller():

    def read_command(self, robot, command):
        split_command = command.upper().split()
        short_command = split_command[0]
        if short_command in robot.COMMAND_OPTIONS:
            # PLACE Command - It's valid at any moment
            if short_command == 'PLACE':
                parameters = split_command[1].split(',')
                return robot.place(parameters)

            # Other commands. Will be run only if a PLACE command has set X and Y coordinates.
            # Otherwise, they will be skipped
            if robot.get_x() is not None and robot.get_y() is not None:
                # Calls the validated method
                method_to_call = getattr(robot, short_command.lower())
                result = method_to_call()

                # Only a REPORT command will print the result
                if short_command == 'REPORT':
                    print(result)
                return result
        return False
    
    def play(self, commands):
        robot = Robot()
        for command in commands:
            self.read_command(robot, command)
