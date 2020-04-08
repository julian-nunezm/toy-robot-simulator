from unittest import TestCase


class ToyRobotValidMovementTest(TestCase):

    def test_robot_does_not_fall_to_move_north(self):
        robot = Robot(4,0,'NORTH')
        robot.move()
        self.assertEqual(robot.get_location(), (4,1))
        self.assertIsNone(robot.warning)

    def test_robot_does_not_fall_to_move_south(self):
        robot = Robot(0,4,'SOUTH')
        robot.move()
        self.assertEqual(robot.get_location(), (0,3))
        self.assertIsNone(robot.warning)

    def test_robot_does_not_fall_to_move_east(self):
        robot = Robot(0,0,'EAST')
        robot.move()
        self.assertEqual(robot.get_location(), (1,0))
        self.assertIsNone(robot.warning)
    
    def test_robot_does_not_fall_to_move_west(self):
        robot = Robot(4,4,'WEST')
        robot.move()
        self.assertEqual(robot.get_location(), (3,4))
        self.assertIsNone(robot.warning)

class ToyRobotNotValidMovementTest(TestCase):

    def test_robot_could_fall_to_move_north(self):
        robot = Robot(4,4,'NORTH')
        robot.move()
        self.assertEqual(robot.get_location(), (4,4))
        self.assertIsNotNone(robot.warning)

    def test_robot_could_fall_to_move_south(self):
        robot = Robot(0,0,'SOUTH')
        robot.move()
        self.assertEqual(robot.get_location(), (0,0))
        self.assertIsNotNone(robot.warning)

    def test_robot_could_fall_to_move_east(self):
        robot = Robot(4,0,'EAST')
        robot.move()
        self.assertEqual(robot.get_location(), (4,0))
        self.assertIsNotNone(robot.warning)
    
    def test_robot_could_fall_to_move_west(self):
        robot = Robot(0,4,'WEST')
        robot.move()
        self.assertEqual(robot.get_location(), (0,4))
        self.assertIsNotNone(robot.warning)

class ToyRobotCommandsTest(TestCase):

    def test_place_function_at_the_beginning(self):
        first_command = 'PLACE 0,0,NORTH'
        robot = Robot()
        self.assertTrue(robot.read_command(first_command))

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
    
    def test_non_valid_command(self):
        non_valid_command = 'JUMP'
        robot = Robot()
        self.assertFalse(robot.read_command(non_valid_command))

    def test_non_valid_facing(self):
        robot = Robot(x=4, y=2, facing='BEHIND')
        self.assertIsNotNone(robot.warning)

    def test_valid_place_function_coordinates(self):
        robot = Robot(x=3, y=3, facing='EAST')
        self.assertIsNone(robot.warning)
    
    def test_non_valid_place_function_coordinates(self):
        robot = Robot(x=-1, y=5, facing='EAST')
        self.assertIsNotNone(robot.warning)
    
    def test_place_function(self):
        robot = Robot(x=4, y=4, facing='EAST')
        self.assertTrue(robot.get_location(), (4,4))
        self.assertTrue(robot.where_is_facing(), 'EAST')

    def test_move_function(self):
        robot = Robot(x=4, y=4, facing='WEST')
        robot.move()
        self.assertTrue(robot.get_location(), (3,4))
    
    def test_left_function(self):
        robot = Robot(x=4, y=4, facing='WEST')
        robot.left()
        self.assertTrue(robot.get_location(), (4,4))
        self.assertTrue(robot.where_is_facing(), 'SOUTH')
    
    def test_right_function(self):
        robot = Robot(x=0, y=1, facing='NORTH')
        robot.right()
        self.assertTrue(robot.get_location(), (0,1))
        self.assertTrue(robot.where_is_facing(), 'EAST')
    
    def test_report_function(self):
        robot = Robot(x=1, y=1, facing='SOUTH')
        robot.move()
        robot.move()
        robot.left()
        robot.move()
        report = robot.report()
        expected_report = '2,0,EAST'
        self.assertTrue(report, expected_report)
