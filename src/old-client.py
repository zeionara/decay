import socket
import sys
import pickle

SERVER_HOST = 'localhost'
SERVER_PORT = 1717
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT)

EXIT_CODE = 'exit'

HELLO_MSG = 'Welcome to the program! In order to exit you need to write "' + EXIT_CODE + '" at any moment'
GOOD_BYE_MSG = 'Have a good luck! See you soon!'
TYPE_NUMBER_MSG = 'Please, type your number for factor and press <Enter>: '
INVALID_NUMBER_MSG = 'It is an invalid number, we need a positive integer one'


#returns a positive integer given by user unless exit code has been entered - in this case returns None
def get_number():
    #repeat typing while haven't got a valid number
    while True:
        stringified_number = input(TYPE_NUMBER_MSG)
        if stringified_number == EXIT_CODE:
            return None
        try:
            number = int(stringified_number)
        except ValueError:
            print(INVALID_NUMBER_MSG)
            continue
        if number > 0:
            return number
        else:
            print(INVALID_NUMBER_MSG)

def main():
    print(HELLO_MSG)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)
    while True:
        message = input(TYPE_NUMBER_MSG) #get_number()
        #if not number:
        #    break
        print('Sending %s' % message)
        client_socket.send(message.encode('utf-8'))

        data = client_socket.recv(128)
        result = pickle.loads(data)
        
        if not result:
            print(INVALID_NUMBER_MSG)
        else:
            print('Result:')
            print(result)
    client_socket.close()
    print(GOOD_BYE_MSG)

if __name__ == "__main__":
    main()
