from unittest import TestCase


class ToyRobotValidMovementTest(TestCase):

    # Validates that the robot moves one position facing north withouth any warnings
    def test_robot_does_not_fall_to_move_north(self):
        robot = Robot(4,0,'NORTH')
        robot.move()
        self.assertEqual(robot.get_location(), (4,1))
        self.assertIsNone(robot.warning)

    # Validates that the robot moves one position facing south withouth any warnings
    def test_robot_does_not_fall_to_move_south(self):
        robot = Robot(0,4,'SOUTH')
        robot.move()
        self.assertEqual(robot.get_location(), (0,3))
        self.assertIsNone(robot.warning)

    # Validates that the robot moves one position facing east withouth any warnings
    def test_robot_does_not_fall_to_move_east(self):
        robot = Robot(0,0,'EAST')
        robot.move()
        self.assertEqual(robot.get_location(), (1,0))
        self.assertIsNone(robot.warning)
    
    # Validates that the robot moves one position facing west withouth any warnings
    def test_robot_does_not_fall_to_move_west(self):
        robot = Robot(4,4,'WEST')
        robot.move()
        self.assertEqual(robot.get_location(), (3,4))
        self.assertIsNone(robot.warning)

class ToyRobotNotValidMovementTest(TestCase):

    # Validates that the robot could not move facing north and there is a warning
    def test_robot_could_fall_to_move_north(self):
        robot = Robot(4,4,'NORTH')
        robot.move()
        self.assertEqual(robot.get_location(), (4,4))
        self.assertIsNotNone(robot.warning)

    # Validates that the robot could not move facing south and there is a warning
    def test_robot_could_fall_to_move_south(self):
        robot = Robot(0,0,'SOUTH')
        robot.move()
        self.assertEqual(robot.get_location(), (0,0))
        self.assertIsNotNone(robot.warning)

    # Validates that the robot could not move facing east and there is a warning
    def test_robot_could_fall_to_move_east(self):
        robot = Robot(4,0,'EAST')
        robot.move()
        self.assertEqual(robot.get_location(), (4,0))
        self.assertIsNotNone(robot.warning)
    
    # Validates that the robot could not move facing west and there is a warning
    def test_robot_could_fall_to_move_west(self):
        robot = Robot(0,4,'WEST')
        robot.move()
        self.assertEqual(robot.get_location(), (0,4))
        self.assertIsNotNone(robot.warning)

class ToyRobotCommandsTest(TestCase):

    # Validates that PLACE command is a valid first command
    def test_place_function_at_the_beginning(self):
        first_command = 'PLACE 0,0,NORTH'
        robot = Robot()
        self.assertTrue(robot.read_command(first_command))

    # Validates that the other command options are not valid as the first command
    def test_other_functions_at_the_beginning(self):
        non_valid_first_commands = [
            'MOVE',
            'LEFT',
            'RIGHT',
            'REPORT'
        ]

        robot = Robot()
        for command in non_valid_first_commands:
            self.assertFalse(robot.read_command(command))
    
    # Validates that any non-defined command is not a valid one
    def test_non_valid_command(self):
        non_valid_command = 'JUMP'
        robot = Robot()
        self.assertFalse(robot.read_command(non_valid_command))

    # Validates that a non-valid facing value given as a parameter creates a warning
    def test_non_valid_facing(self):
        command = 'PLACE 4,2,BEHIND'
        robot = Robot()
        self.assertFalse(robot.read_command(command))
        self.assertIsNotNone(robot.warning)

    # Validates that the coordinates given are valid, the robot is placed, and there is not a warning
    def test_valid_place_function_coordinates(self):
        robot = Robot(x=3, y=3, facing='EAST')
        self.assertEqual(robot.get_location(), (3,3))
        self.assertEqual(robot.where_is_facing(), 'EAST')
        self.assertIsNone(robot.warning)
    
    # Validates that the robot is not placed and there is a warning
    def test_non_valid_place_function_coordinates(self):
        robot = Robot(x=-1, y=5, facing='EAST')
        self.assertEqual(robot.get_location(), (None, None))
        self.assertIsNone(robot.where_is_facing())
        self.assertIsNotNone(robot.warning)
    
    # Validates that the function creates and places the robot
    def test_place_function(self):
        robot = Robot(x=4, y=4, facing='EAST')
        self.assertTrue(robot.get_location(), (4,4))
        self.assertTrue(robot.where_is_facing(), 'EAST')

    # Validates that the function moves the robot one position towards its facing value
    def test_move_function(self):
        robot = Robot(x=4, y=4, facing='WEST')
        robot.move()
        self.assertTrue(robot.get_location(), (3,4))
    
    # Validates that the function rotates the robot to left and does not make it to advance
    def test_left_function(self):
        robot = Robot(x=4, y=4, facing='WEST')
        robot.left()
        self.assertTrue(robot.get_location(), (4,4))
        self.assertTrue(robot.where_is_facing(), 'SOUTH')
    
    # Validates that the function rotates the robot to right and does not make it to advance
    def test_right_function(self):
        robot = Robot(x=0, y=1, facing='NORTH')
        robot.right()
        self.assertTrue(robot.get_location(), (0,1))
        self.assertTrue(robot.where_is_facing(), 'EAST')
    
    # Validates that the function returns the information about where the robot is placed
    def test_report_function(self):
        robot = Robot(x=1, y=1, facing='SOUTH')
        robot.move()
        robot.move()
        robot.left()
        robot.move()
        report = robot.report()
        expected_report = '2,0,EAST'
        self.assertTrue(report, expected_report)
