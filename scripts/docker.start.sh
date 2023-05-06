

docker build . -t fastapi:latest
docker run --rm --name test-fastapi -p 8000:8000 fastapi:latest


