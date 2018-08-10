#! /bin/bash
echo 'Running unit tests for the server...' &&
python ./test/test_server.py && (
echo 'Running server...' &&
python ./src/server.py &
sleep 2 &&
echo 'Running client...' &&
python ./src/client.py)
