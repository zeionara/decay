import socket
import sys
import pickle

RESPONSE_SIZE = 128

PREAMBLE = '[CLIENT] '

SERVER_HOST = 'localhost'
SERVER_PORT = 1718
SERVER_ADDRESS = (SERVER_HOST, SERVER_PORT)

EXIT_CODE = 'exit'

HELLO_MSG = """Welcome to the factorization program! In order to exit
    you need to write '""" + EXIT_CODE + "' at any moment"
GOOD_BYE_MSG = 'Have a good luck! See you soon!'
TYPE_NUMBER_MSG = 'Please, type your number for factor and press <Enter>: '
INVALID_NUMBER_MSG = 'It is an invalid number, we need a positive integer one'
CONNECTING_MSG = 'Connecting to the server...'
CONNECTED_MSG = 'Connected to the server'


def main():
    print(PREAMBLE, HELLO_MSG)
    # create socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(PREAMBLE, CONNECTING_MSG)
    client_socket.connect(SERVER_ADDRESS)
    print(PREAMBLE, CONNECTED_MSG)
    try:
        while True:
            # get a new number for factorization
            # if user typed exit code instead of number - close program
            message = input(PREAMBLE + ' ' + TYPE_NUMBER_MSG)
            if message == EXIT_CODE:
                break
            # send number to the server
            client_socket.send(message.encode('utf-8'))
            # get result from server and unpickle it
            data = client_socket.recv(RESPONSE_SIZE)
            result = pickle.loads(data)
            # show result of fuctorization to user
            if not result:
                print(PREAMBLE, INVALID_NUMBER_MSG)
            else:
                print(PREAMBLE, '%s = %s' %
                      (message,
                       ' * '.join([str(item) for item in result])))
    finally:
        # disconnect from the server
        client_socket.close()

    print(PREAMBLE, GOOD_BYE_MSG)

if __name__ == "__main__":
    main()
