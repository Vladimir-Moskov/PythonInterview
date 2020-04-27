
# Base repo
# https://github.com/btholt/projects-for-complete-intro-to-containers/tree/master/visual-studio-code
# https://github.com/btholt/complete-intro-to-containers

# Docker install - official
# https://docs.docker.com/engine/install/ubuntu/

# For Raspbery pi 4
# https://medium.com/faun/single-node-kubernetes-on-a-raspberry-pi-cb93a4300305
# https://www.youtube.com/watch?v=nBwJm0onzeo&t=211s

 docker run hello-world
 # -it - interactive mode, login in to shell of the image
 docker run -it ubuntu bash
 more /etc/os-release
 lscpu
 uname -a
 cd /usr/src
 docker run -it ubuntu top
 docker images
 # see existing images states
 docker container ls -a
 docker start -i 76757e1a74c0
  ls -lah /usr/src/
  # delete existing images states
  docker container prune

  # --rm - remove image state file after close
   docker run --rm -it ubuntu top

  docker run hello-world-gcc
  docker build -t hello-world-gcc .
  docker run --rm -it -p 4000:80 simple-node-webserver