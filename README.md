## Build container

`docker build -t build_system .`

## Run container

`docker run -p 8111:8111 build_system `

## CURL for get tasks

`curl -L -X POST 'http://localhost:8111/api/tasks/' -H 'Content-Type: application/json' --data-raw '{
    "build_name": "forward_interest"
}'`