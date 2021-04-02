import os
import requests
import paramiko
#from os.path import expanduser


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
def connect_to_server():
    path_to_key = '~/.ssh/key_all.pem'
    client = SSH_connection('hub')
def parse_server(name):
    print('Server successfuly parsed')
commands = {
    'test' : test,
    'ssh'  : connect_to_server,
    'exit' : exit
}
def parse_config_string():

    return 1
class SSH_connection():
    server_name = ''
    ip = ''
    port = ''
    user = ''
    forwardx11 = ''
    compression = ''
    path_to_key = ''
    def __init__(self, name):
        config_key_words = {
            'Host' : 'server_name',
            'Hostname' : 'ip',
            'Port' : 'port',
            'User' : 'user',
            'ForwardX11' : 'forwardx11',
            'Compression' : 'compression',
            'IdentityFile' : 'path_to_key'
        }
        print(self)
        self.server_name = name
        path_to_config = '~/.ssh/config'
        path_to_config = os.path.expanduser(path_to_config)
        try:
            config_file = open(path_to_config,'r',encoding='utf-8')
        except requests.exceptions.RequestException:
            print("Can't open ssh_config_file")
        string = ''
        host_bool = False
        for string in config_file:
            string = string.strip()
            if string == 'Host ' + name:
                print('{} founded!'.format(name))
                string = config_file.readline().strip()
                host_bool = True
            if host_bool == True:
                parameter = string[:string.index(' ')]
                value = string[string.index(' ') + 1:]
                if parameter == 'Host':
                    break
                if parameter in config_key_words:
                    setattr(self,config_key_words[parameter],value)
        print('Подключение к {}@{} -p {} с параметрами path_to_key = {}, compression = {} forwardx11 = {}'.format(self.user,self.ip,self.port,self.path_to_key,self.compression,self.forwardx11))

            
        
        
        
        
                

if __name__ == "__main__":
    main()