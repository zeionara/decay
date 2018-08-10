#! /bin/bash
echo 'Running unit tests for the server...' &&
python ./test_server.py && (
echo 'Running server...'
python ./server.py &
sleep 2 &&
echo 'Running client...'
python ./client.py)
