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