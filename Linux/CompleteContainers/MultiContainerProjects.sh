# https://btholt.github.io/complete-intro-to-containers/docker-compose
# Docker Compose

npm init -y
npm install mongodb @hapi/hapi hapi-pino
npm install mongodb@3.3 # you need to add mongodb to your project
nano index.js

docker-compose up
docker-compose up --build
docker-compose build

# https://btholt.github.io/complete-intro-to-containers/kompose
# Kompose
kompose up
kubectl get all

kubectl scale --replicas=5 deployment/web
# convert/unpackage back from kompose config to kubectl congigs
kompose conver