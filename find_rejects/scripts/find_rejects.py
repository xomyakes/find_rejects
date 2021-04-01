import os
import requests


def main():
    print('Hello, mothrfucker!')
    console()
def test():
    print('It works!')
def console():
    command = ''
    while True:
        command = str(input())
        try:
            if command in commands:
                commands[command]()
        except requests.exceptions.RequestException:
            print("Can't read command")
commands = {
    'test' : test,
    'exit' : exit
}


if __name__ == "__main__":
    main()