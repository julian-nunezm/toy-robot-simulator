from model.toy_robot import Robot


class Controller():

    def read_command(self, command): # TODO: Change to function dictionary
        split_command = command.upper().split()
        short_command = split_command[0]
        robot = Robot()
        if short_command in robot.COMMAND_OPTIONS:
            # PLACE Command
            if short_command == 'PLACE':
                return robot.place(split_command[1].split(','))

            if robot.get_x() and robot.get_y():
                # MOVE Command
                if short_command == 'MOVE':
                    return robot.move()

                # LEFT Command
                if short_command == 'LEFT':
                    robot.left()

                # RIGHT Command
                if short_command == 'RIGHT':
                    robot.right()

                # REPORT Command
                if short_command == 'LEFT':
                    robot.left()
        return False