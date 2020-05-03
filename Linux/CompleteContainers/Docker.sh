# https://btholt.github.io/complete-intro-to-containers/docker-images-without-docker
# start docker contanier with docker running in it connected to host docker daemon
docker run -ti -v /var/run/docker.sock:/var/run/docker.sock --privileged --rm --name docker-host docker:18.06.1-ce
cat /etc/issue
# run stock alpine container inside this docker container/image
docker run --rm -dit --name my-alpine alpine:3.10 sh

# export running container's file system
docker export -o dockercontainer.tar my-alpine

# make container-root directory, export contents of container into it
mkdir container-root
tar xf dockercontainer.tar -C container-root/

# make a contained user, mount in name spaces
unshare --mount --uts --ipc --net --pid --fork --user --map-root-user chroot $PWD/container-root ash # this also does chroot for us
mount -t proc none /proc
mount -t sysfs none /sys
mount -t tmpfs none /tmp

# here's where you'd do all the cgroup rules making with the settings you wanted to

# https://btholt.github.io/complete-intro-to-containers/docker-images-with-docker
docker run --interactive --tty alpine:3.10
cat /etc/issue
docker run -it alpine:3.10
docker run alpine:3.10 ls
docker run alpine:3.10 cat /etc/issue

docker run ubuntu:bionic ls
docker run ubuntu:bionic cat /etc/issue
# run image in background
docker run --detach -it ubuntu:bionic
docker ps
docker attach <ID or name>
docker attach funny_shirley
docker kill <IDs or names of containers>

docker run -it --name my-alpine alpine:3.10
docker logs my-alpine
docker kill my-alpine
docker rm my-alpine

docker run -dit --name my-ubuntu ubuntu:bionic
docker kill my-ubuntu


# https://btholt.github.io/complete-intro-to-containers/nodejs-on-docker
# Node.js on Docker

docker run -it node:12-stretch

docker run -it node:12-stretch bash
cat /etc/issue

docker run ubuntu:bionic cat /etc/issue # hopefully this shouldn't surprise you
docker run node:12-stretch cat /etc/issue # ????

# https://btholt.github.io/complete-intro-to-containers/tags
# Tags
docker run -it node:8 bash
docker run node:12-alpine cat /etc/issue

# https://btholt.github.io/complete-intro-to-containers/docker-cli
# Docker CLI
