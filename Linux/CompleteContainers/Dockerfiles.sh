# Dockerfiles
# https://btholt.github.io/complete-intro-to-containers/dockerfile
# Intro to Dockerfiles

FROM node:12-stretch

CMD ["node", "-e", "console.log(\"hi lol\")"]

docker build .

docker run 3e7e9389d788

It's a little inconvenient to always have to refer to it by ID, it'd be easier if it had a name. So let's do that! Try

docker build . --tag my-node-app ## or -t instead of --tag
docker run my-node-app

docker build -t my-node-app:1 .
docker run my-node-app:1

docker build -t my-node-app:2 .
docker run my-node-app:2
docker run my-node-app:1

# https://btholt.github.io/complete-intro-to-containers/build-a-nodejs-app
# Build a Node.js App
