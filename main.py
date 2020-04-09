def main():
    print('Toy Robot Simulator')
    with open('test_data.txt', 'r', encoding='utf8') as commands_file:
        for line in commands_file:
            print(line)
    

if __name__ == '__main__':
    main()