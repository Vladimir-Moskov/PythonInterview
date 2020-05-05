# https://btholt.github.io/complete-intro-to-containers/alpine-linux
# Alpine Linux6

docker inspect my-app
docker build -t my-node-app:3-alpine .
docker run --init --rm --publish 3000:3000 my-node-app:3-alpine

FROM node:12-alpine

USER node

RUN mkdir /home/node/code

WORKDIR /home/node/code

COPY --chown=node:node package-lock.json package.json ./

RUN npm ci

COPY --chown=node:node . .

CMD ["node", "index.js"]

# https://btholt.github.io/complete-intro-to-containers/making-our-own-alpine-nodejs-container
# Making Our Own Alpine Node.js Container

FROM alpine:3.10

RUN apk add --update nodejs npm