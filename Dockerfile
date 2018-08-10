FROM python:3
ADD src/client.py /
ADD src/server.py /
ADD test/test_server.py /
ADD run_from_docker.sh /
RUN chmod +x ./run_from_docker.sh
CMD ./run_from_docker.sh

