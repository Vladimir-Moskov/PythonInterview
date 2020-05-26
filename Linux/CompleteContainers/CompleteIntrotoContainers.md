
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
  # Purging All Unused or Dangling Images, Containers, Volumes, and Networks
  docker system prune -a
  # Remove images only
   docker rmi Image Image
  # Remove dangling images
   docker images purge


  # --rm - remove image state file after close
   docker run --rm -it ubuntu top

  docker run hello-world-gcc
  docker build -t hello-world-gcc .
  docker run --rm -it -p 4000:80 simple-node-webserver

# https://github.com/btholt/complete-intro-to-containers
# https://btholt.github.io/complete-intro-to-containers/

# chroot - use to be kernel / Linux jail
docker pull ubuntu:bionic
docker pull node:12-stretch
docker pull node:12-alpine
docker pull nginx:1.17
docker pull mongo:3
docker pull jguyomard/hugo-builder:0.55

# https://github.com/btholt/complete-intro-to-containers/blob/master/lessons/chroot.md
docker run -it --name docker-host --rm --privileged ubuntu:bionic

mkdir my-new-root
cat /etc/issue
cd my-new-root
cd ..
mkdir my-new-root/bin
# see all bash dependency libs
ldd bin/bash
# smart way to create 2 dirs lib and lib64
cp /bin/bash  /my-new-root/bin/
mkdir my-new-root/lib{,64}
# copy nash related libs into local env
cp /lib/arm-linux-gnueabihf/libtinfo.so.5  /lib/arm-linux-gnueabihf/libdl.so.2 /lib/arm-linux-gnueabihf/libc.so.6 /my-new-root/lib
cp /lib/ld-linux-armhf.so.3 /my-new-root/lib
cp /lib/ld-linux-armhf.so.1 /my-new-root/lib

chroot /my-new-root bash
pwd
exit
cp /bin/ls  /my-new-root/bin/
ldd /bin/ls
cp  /lib/arm-linux-gnueabihf/libselinux.so.1 /lib/arm-linux-gnueabihf/libc.so.6 /lib/ld-linux-armhf.so.3 /lib/arm-linux-gnueabihf/libpcre.so.3 /lib/arm-linux-gnueabihf/libdl.so.2 /lib/arm-linux-gnueabihf/libpthread.so.0 /my-new-root/lib

chroot /my-new-root bash
echo "very confidential message" > secret.txt
cp /lib/arm-linux-gnueabihf/libc.so.6 /lib/ld-linux-armhf.so.3 /my-new-root/lib
cp /bin/cat  /my-new-root/bin/

# namespaces
# https://btholt.github.io/complete-intro-to-containers/namespaces
tail -f /my-new-root/secret.txt
# connect to existing docker image
docker exec -it docker-host bash
# update image from inside
exit # from our chroot'd environment if you're still running it, if not skip this

# install debootstrap
apt-get update -y
apt-get install debootstrap -y
debootstrap --variant=minbase bionic /better-root

# head into the new namespace'd, chroot'd environment
unshare --mount --uts --ipc --net --pid --fork --user --map-root-user chroot /better-root bash # this also chroot's for us
mount -t proc none /proc # process namespace
mount -t sysfs none /sys # filesystem
mount -t tmpfs none /tmp # filesystem

# cgroups
# https://btholt.github.io/complete-intro-to-containers/cgroups
# outside of unshare'd environment get the tools we'll need here
apt-get install -y cgroup-tools htop

# create new cgroups
cgcreate -g cpu,memory,blkio,devices,freezer:/sandbox

# add our unshare'd env to our cgroup
ps aux # grab the bash PID that's right after the unshare one
cgclassify -g cpu,memory,blkio,devices,freezer:sandbox <PID>

# list tasks associated to the sandbox cpu group, we should see the above PID
cat /sys/fs/cgroup/cpu/sandbox/tasks

# show the cpu share of the sandbox cpu group, this is the number that determines priority between competing resources, higher is is higher priority
cat /sys/fs/cgroup/cpu/sandbox/cpu.shares

# kill all of sandbox's processes if you need it
# kill -9 $(cat /sys/fs/cgroup/cpu/sandbox/tasks)

# Limit usage at 5% for a multi core system
cgset -r cpu.cfs_period_us=100000 -r cpu.cfs_quota_us=$[ 5000 * $(getconf _NPROCESSORS_ONLN) ] sandbox

# Set a limit of 80M
cgset -r memory.limit_in_bytes=80M sandbox
# Get memory stats used by the cgroup
cgget -r memory.stat sandbox

# in terminal session #2, outside of the unshare'd env
htop # will allow us to see resources being used with a nice visualizer

# in terminal session #1, inside unshared'd env
yes > /dev/null # this will instantly consume one core's worth of CPU power
# notice it's only taking 5% of the CPU, like we set
# if you want, run the docker exec from above to get a third session to see the above command take 100% of the available resources
# CTRL+C stops the above any time

# in terminal session #1, inside unshare'd env
yes | tr \\n x | head -c 1048576000 | grep n # this will ramp up to consume ~1GB of RAM
# notice in htop it'll keep the memory closer to 80MB due to our cgroup
# as above, connect with a third terminal to see it work outside of a cgroup

