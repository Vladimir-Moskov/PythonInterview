# from the root directory of your CRA app
docker run --mount type=bind,source="$(pwd)"/build,target=/usr/share/nginx/html -p 8080:80 nginx

# Volumes
mkdir docker-volume
cd docker-volume
touch index.js Dockerfile

docker build --tag=incrementor .
docker run incrementor

docker run --env DATA_PATH=/data/num.txt --mount type=volume,src=incrementor-data,target=/data incrementor
docker volume ls
docker volume inspect incrementor-data

# Using Containers for your Dev Environment
git clone https://github.com/btholt/hugo-example.git
cd hugo-example/
# you could rewrite the --mount here as -v $PWD:/src
docker run --rm -it --mount type=bind,source="$(pwd)",target=/src -p 1313:1313 -u hugo jguyomard/hugo-builder:0.55 hugo server -w --bind=0.0.0.0

# Networking with Docker
docker network ls
docker network create --driver=bridge app-net
docker run -d --network=app-net -p 27017:27017 --name=db --rm mongo:3
docker run -it --network=app-net --rm mongo:3 mongo --host db

npm install mongodb@3.3 # you need to add mongodb to your project
docker build --tag=my-app-with-mongo .
docker run -p 3000:3000 --network=app-net --env MONGO_CONNECTION_STRING=mongodb://db:27017 my-app-with-mongo





