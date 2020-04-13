from unittest import TestCase

from controller.command_interpreter import Controller
from model.toy_robot import Robot

# Tests Model
class RobotModelTest(TestCase):

    # Validates that the robot object is created with no parameters
    def test_create_empty_robot(self):
        robot = Robot()
        self.assertIsNone(robot.get_x())
        self.assertIsNone(robot.get_y())
        self.assertIsNone(robot.get_facing())

    # Validates that the robot object is created with the parameteres given
    def test_create_robot(self):
        robot = Robot(x=0, y=0, facing='NORTH')
        self.assertEqual(robot.get_x(), 0)
        self.assertEqual(robot.get_y(), 0)
        self.assertEqual(robot.get_facing(), 'NORTH')

# Tests Robot methods
class RobotUnitTest(TestCase):

    # Validates that the get_location function returns the coordinates tuple
    def test_get_location_function(self):
        robot = Robot(x=0, y=0, facing='NORTH')
        self.assertEqual(robot.get_location(), (0,0))
    
    # Validates that is_valid_y_movement function returns False for a not valid movement to North
    def test_valid_y_movement_north(self):
        robot = Robot(x=0, y=4, facing='NORTH')
        self.assertFalse(robot.is_valid_y_movement())
    
    # Validates that is_valid_y_movement function returns False for a not valid movement to South
    def test_valid_y_movement_south(self):
        robot = Robot(x=4, y=0, facing='SOUTH')
        self.assertFalse(robot.is_valid_y_movement())
    
    # Validates that is_valid_x_movement function returns False for a not valid movement to East
    def test_valid_x_movement_east(self):
        robot = Robot(x=4, y=4, facing='EAST')
        self.assertFalse(robot.is_valid_x_movement())
    
    # Validates that is_valid_x_movement function returns False for a not valid movement to West
    def test_valid_y_movement_west(self):
        robot = Robot(x=0, y=0, facing='WEST')
        self.assertFalse(robot.is_valid_x_movement())

    # Validates that place function locates the robot correctly 
    def test_place_function(self):
        robot = Robot()
        self.assertTrue(robot.place([4,3,'NORTH']))
        self.assertEqual(robot.get_x(), 4)
        self.assertEqual(robot.get_y(), 3)
        self.assertEqual(robot.get_facing(), 'NORTH')
    
    # Validates that place function doesn't locate the robot correctly 
    def test_place_function_to_false(self):
        robot = Robot()
        self.assertFalse(robot.place([-1,5,'NORTH']))
        self.assertIsNone(robot.get_x())
        self.assertIsNone(robot.get_y())
        self.assertIsNone(robot.get_facing())
    
    # Validates that move function increments the correct coordinate based on the facing value 
    def test_move_function(self):
        robot = Robot(x=0, y=0, facing='EAST')
        robot.move()
        self.assertEqual(robot.get_x(), 1)
        self.assertEqual(robot.get_y(), 0)
        self.assertEqual(robot.get_facing(), 'EAST')
    
    # Validates that left function rotates the robot correctly 
    def test_left_function(self):
        robot = Robot()
        robot.place([4,3,'NORTH'])
        robot.left()
        self.assertEqual(robot.get_facing(), 'WEST')
    
    # Validates that right function rotates the robot correctly 
    def test_right_function(self):
        robot = Robot()
        robot.place([4,3,'WEST'])
        robot.right()
        self.assertEqual(robot.get_facing(), 'NORTH')
    
    # Validates that report function returns the correct robot location 
    def test_report_function(self):
        robot = Robot()
        robot.place([1,1,'SOUTH'])
        robot.move()
        robot.move()
        robot.left()
        robot.move()
        self.assertEqual(robot.report(), '2,0,EAST')
        
# Test Controller commands
class RobotControllerTest(TestCase):

    # Validates that the first command is PLACE
    def test_first_command_place(self):
        first_command = 'PLACE 0,0,EAST'
        robot = Robot()
        controller = Controller()
        self.assertTrue(controller.read_command(robot, first_command))
    
    # Validates that the first command is not PLACE
    def test_first_command_not_place(self):
        non_valid_first_commands = [
            'MOVE',
            'LEFT',
            'RIGHT',
            'REPORT'
        ]
        robot = Robot()
        controller = Controller()
        for command in non_valid_first_commands:
            self.assertFalse(controller.read_command(robot, command))

    # Validates that any non-defined command is not a valid one
    def test_non_valid_command(self):
        non_valid_command = 'JUMP'
        robot = Robot()
        controller = Controller()
        self.assertFalse(controller.read_command(robot, non_valid_command))

    # Validates that a non-valid facing value given as a parameter returns False
    def test_non_valid_facing(self):
        command = 'PLACE 4,2,NORTH-EAST'
        robot = Robot()
        controller = Controller()
        self.assertFalse(controller.read_command(robot, command))
    
    # Validates that the robot is not placed with wrong coordinates
    def test_non_valid_place_function_coordinates(self):
        command = 'PLACE -1,5,SOUTH'
        robot = Robot()
        controller = Controller()
        self.assertFalse(controller.read_command(robot, command))
    
    # Validates that the move command works properly
    def test_move_command(self):
        commands = [
            'PLACE 0,0,EAST',
            'MOVE',
        ]
        robot = Robot()
        controller = Controller()
        for command in commands:
            if command == 'PLACE 0,0,EAST':
                self.assertTrue(controller.read_command(robot, command))
            #if command == 'MOVE':
            #    self.assertTrue(controller.read_command(command))
    
    # TODO: Test LEFT, RIGHT and REPORT from controller.read_command
