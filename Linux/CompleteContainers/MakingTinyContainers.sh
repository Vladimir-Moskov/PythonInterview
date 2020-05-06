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

docker images
docker build -t my-node-app:4-alpine -f my-node.Dockerfile .
docker run --init --rm --publish 3000:3000 my-node-app:4-alpine

# https://btholt.github.io/complete-intro-to-containers/multi-stage-builds
# Multi Stage Builds

docker images
docker build -t my-node-app:5-alpine -f multi-node.Dockerfile .
docker run --init --rm --publish 3000:3000 my-node-app:5-alpine

# https://btholt.github.io/complete-intro-to-containers/static-assets-project
# Static Assets Project

npx --ignore-existing create-react-app static-assets-project --template typescript --use-npm
npm install node-sass
npm run start
npm run build

# done? If you gave it a shot, your Dockerfile probably shouldn't very long. Let's see what I came up with

FROM node:latest
WORKDIR /app
COPY . .
RUN npm ci && npm run build

# you could totally use nginx:alpine here too
FROM nginx:latest
COPY --from=0 /app/build /usr/share/nginx/html

Now if you run this, it should work:

docker build -t static-app .
docker run -p 8080:80 static-app