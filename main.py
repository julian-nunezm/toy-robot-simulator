from controller.command_interpreter import Controller


def main():
    folder = 'data/'
    data_files = [
        'example_a.txt',
        'example_b.txt',
        'example_c.txt',
        'example_k.txt',
        'example_s.txt',
        'test_data.txt',
    ]
    print('\nToy Robot Simulator\n')
    
    # Reading file
    for file_name in data_files:
        commands = []
        try:
            print(f'File name: {file_name}')
            file = open(folder + file_name, 'r')
            commands = [line.replace('\n', '') for line in file.readlines()]

            # Play the simulator
            simulator = Controller()
            simulator.play(commands)
        except:
            print(f'ERROR: An error over {file_name} occured. The file was ignored.')
        finally:
            file.close()
            print(f'{file_name}.... done!\n')
    
    
if __name__ == '__main__':
    main()