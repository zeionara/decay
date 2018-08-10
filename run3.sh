#! /bin/bash
echo 'Running unit tests for the server...' &&
python3 ./test/test_server.py && (
echo 'Running server...' &&
python3 ./src/server.py &
sleep 2 &&
echo 'Running client...' &&
python3 ./src/client.py)
