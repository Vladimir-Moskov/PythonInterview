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
docker build -t my-node-app .
docker run my-node-app

docker run --init --rm --publish 3000:3000 my-node-app # or you can use -p instead of --publish

# https://btholt.github.io/complete-intro-to-containers/more-complicated-nodejs-app
# A More Complicated Node.js App

npm init -y # this will create a package.json for you without asking any questions
npm install @hapi/hapi hapi-pino

docker build -t my-node-app .
docker run --init --rm --publish 3000:3000 my-node-app

# https://btholt.github.io/complete-intro-to-containers/expose
# A Note on EXPOSE

docker run --init --rm --detach -P my-node-app

# https://btholt.github.io/complete-intro-to-containers/layers
# Layers
FROM node:12-stretch

USER node

RUN mkdir /home/node/code

WORKDIR /home/node/code

COPY --chown=node:node package-lock.json package.json ./

RUN npm ci

COPY --chown=node:node . .

CMD ["node", "index.js"]





