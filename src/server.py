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

#returns data converted to int unless it is invalid - in this case returns None
def check_data(data):
    try:
        number = int(data)
    except ValueError:
        return None
    if number <= 1:
        return None
    return number

#returns True if the given number is prime - in other case returns False
def is_prime(number):
    if not is_positive_integer(number):
        raise ValueError

    if number == 1:
        raise ValueError
    
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def is_positive_integer(number):
    try:
        if (number - int(number) != 0) or (number <= 0):
            return False
    except ValueError:
        return False
    return True

#returns possible prime numbers which are less than half of the given number
def get_possible_primes(number):
    result = []
    
    if not is_positive_integer(number):
        raise ValueError

    if number == 1:
        raise ValueError

    for i in range(2, number // 2 + 1):
        if is_prime(i):
            result.append(i)
    return result

#returns tuple of integers as a result of factorization
def factorize(number):
    if number == 1:
        raise ValueError

    if not is_positive_integer(number):
        raise ValueError
    
    factors = []
    current_prime_index = 0
    primes = get_possible_primes(number)
    
    while number > 1 and current_prime_index < len(primes):
        current_prime = primes[current_prime_index]
        if number % current_prime == 0:
            number = number // current_prime
            factors.append(current_prime)
            current_prime_index = 0
            continue
        current_prime_index += 1
    
    if number > 1:
        factors.append(number)
    
    return tuple(factors)

def main():
    print(PREAMBLE, STARTING_SERVER_MSG)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(SERVER_ADDRESS)
    print(PREAMBLE, STARTED_MSG)
    server_socket.listen(1)

    while True:
        print(PREAMBLE, WAITING_MSG)
        connection, client_address = server_socket.accept()
        try:
            print(PREAMBLE, GOT_CONNECTION_MSG % client_address)

            while True:
                data = connection.recv(REQUEST_SIZE)
                print(PREAMBLE, RECEIVED_MSG % data.decode('utf-8'))
                number = check_data(data)
                result = None
                if number:
                    result = factorize(number)
                connection.send(pickle.dumps(result))
                if not data:
                    print(PREAMBLE, NO_MORE_DATA_MSG % client_address)
                    break
        finally:
            connection.close()



if __name__ == "__main__":
    main()
