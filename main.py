from controller.command_interpreter import Controller


def main():
    file_name = 'test_data.txt'
    commands = []
    print('Toy Robot Simulator')
    
    # Reading file
    file = open(file_name, 'r')
    commands = [line.replace('\n', '') for line in file.readlines()]
    file.close()
    
    # Play the simulator
    simulator = Controller()
    simulator.play(commands)
    
    
if __name__ == '__main__':
    main()