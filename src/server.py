import socket
import sys
import pickle

PREAMBLE = '[SERVER] '

REQUEST_SIZE = 128
HOST = 'localhost'
PORT = 1718
SERVER_ADDRESS = (HOST, PORT)

STARTING_SERVER_MSG = 'Starting at %s:%s...' % (HOST, PORT)
STARTED_MSG = 'Started. Listening for incoming connections...'
WAITING_MSG = 'Waiting...'
GOT_CONNECTION_MSG = 'Got connection from %s:%s'
RECEIVED_MSG = 'Received %s'
NO_MORE_DATA_MSG = 'No more data from %s:%s'


# returns True if the given value is a positive integer and False in other case
def is_positive_integer(number):
    try:
        if (number - int(number) != 0) or (number <= 0):
            return False
    except ValueError:
        return False
    return True


# checks that the given value is a positive integer which is not equal to 1
# if it is not right, raises a ValueError
def validate_number(number):
    if not is_positive_integer(number):
        raise ValueError

    if number == 1:
        raise ValueError


# returns data converted to int unless it is invalid
# in other case returns None
def check_data(data):
    try:
        number = int(data)
    except ValueError:
        return None
    if number <= 1:
        return None
    return number


# returns True if the given number is prime - in other case returns False
def is_prime(number):

    validate_number(number)

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


# get least prime number which is more than a given one
def get_next_prime(number):
    if not is_prime(number):
        raise ValueError

    while True:
        number += 1
        if is_prime(number):
            return number


# returns tuple of integers as a result of factorization
def factorize(number):
    validate_number(number)

    factors = []
    current_prime = 2

    while number > 1:
        if number % current_prime == 0:
            number = number // current_prime
            factors.append(current_prime)
        else:
            current_prime = get_next_prime(current_prime)

    return tuple(factors)


def main():
    print(PREAMBLE, STARTING_SERVER_MSG)
    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    print(PREAMBLE, STARTED_MSG)
    server_socket.listen(1)
    # listen for incoming connections
    while True:
        print(PREAMBLE, WAITING_MSG)
        # connect to client
        connection, client_address = server_socket.accept()
        try:
            print(PREAMBLE, GOT_CONNECTION_MSG % client_address)
            # start to handle requests
            while True:
                data = connection.recv(REQUEST_SIZE) 
                if not data:
                    print(PREAMBLE, NO_MORE_DATA_MSG % client_address)
                    break
                print(PREAMBLE, RECEIVED_MSG % data.decode('utf-8'))
                # check number and factorize it if it is a valid one
                number = check_data(data)
                result = None
                if number:
                    result = factorize(number)
                # return result and try to handle next request
                connection.send(pickle.dumps(result))
        finally:
            connection.close()


if __name__ == "__main__":
    main()
