What started as a way to manage multiple servers on one system has grown into the way we develop, write code, ship applications, and coordinate large scale applications! Containers may have started as tools for the ops team, but now everyone needs to learn to build and use them. In this course you’ll learn, what containers are and how to create containers from scratch, how to run containers from Dockerhub, how to create your own containers with Docker files, best practices are for front-end and Node.js code in containers, and how to create development environments with containers.

Course Website https://btholt.github.io/complete-intro-to-containers/
Code Repo & Setup https://github.com/btholt/complete-intro-to-containers
Project Files https://github.com/btholt/projects-for-complete-intro-to-containers


Table of Contents
Introduction
Introduction
00:00:00 - 00:08:24
Introduction
Brian Holt gives an overview of the course, explains why containers are a relevant topic for any software engineer, discusses what needs to be installed to follow along, and shares where to file issues with the course. - https://btholt.github.io/complete-intro-to-containers/
Containers
Containers
00:08:25 - 00:21:53
Containers
Brian gives a brief history of why containers are useful tools that host controlled and isolated environments, thanks to a frozen file system. The latter allowed engineers to have access to ready to use containers without having to recreate all the dependencies and file system on a local machine. - https://btholt.github.io/complete-intro-to-containers/what-are-containers
chroot
00:21:54 - 00:34:45
chroot
Brian explains that chroot is a Linux kernel feature that allows the containment of processes, restricts a process to a certain file tree, and uses chroot to add bash commands to the bash directory. A chroot operation is necessary to understand how containers are layered to limit or deny access outside of a designated directory tree. - https://btholt.github.io/complete-intro-to-containers/chroot
chroot Exercise
00:34:46 - 00:35:40
chroot Exercise
Students are instructed to use the chroot process to make the bash command cat function within the bash directory.
chroot Solution
00:35:41 - 00:37:43
chroot Solution
Brian live codes the solution to the chroot exercise.
Namespaces
00:37:44 - 00:52:08
Namespaces
Brian explains that namespaces are useful to hide processes, networks, and other configurations from other environments, and demonstrates how to configure namespaces and use a command nammed unshare to seperate environments. The parent process has access to the child process, but the child cannot access the parent. - https://btholt.github.io/complete-intro-to-containers/namespaces
cgroups
00:52:09 - 01:09:20
cgroups
Brian explains that cgroups were invented by Google to limit what resources a process can access to avoid entire servers shutting down, and demonstrates how to manually use cgroups to restrict processes. - https://btholt.github.io/complete-intro-to-containers/cgroups
Docker
Getting Set Up with Docker
01:09:21 - 01:12:47
Getting Set Up with Docker
Brian explains that Docker is a command line tool that makes building and managing containers easier, and that has environments built in various languages. Docker allows engineers to build a container in less time and fewer lines of code because it manages chroot, namespaces, and cgroups for the engineer. - https://btholt.github.io/complete-intro-to-containers/getting-set-up-with-docker
Docker Images without Docker
01:12:48 - 01:20:01
Docker Images without Docker
Brian demonstrates how to download a container, unpack it, and run it on its own without involving Docker. - https://btholt.github.io/complete-intro-to-containers/docker-images-without-docker
Docker Images with Docker
01:20:02 - 01:31:20
Docker Images with Docker
Brian demonstrates how to use a one line command to build a container instead of using the longer process live coded in the previous section, explains that images take memory space, and shows how to prune them. - https://btholt.github.io/complete-intro-to-containers/docker-images-with-docker
Node.js on Docker
01:31:21 - 01:38:35
Node.js on Docker
Brian demonstrates how to create a Node.js container that uses Debian instead of Ubuntu after mentioning that there is a wide variety of containers using different libraries and laguages. Debian is used instead of Ubuntu because Node images were created in Debian. - https://btholt.github.io/complete-intro-to-containers/nodejs-on-docker
Tags
01:38:36 - 01:47:34
Tags
Brian explains that it is important to tie tags to specific versions when creating environments to avoid dependency issues that would break the code, and shares the rules of thumb when picking tags to build a container. - https://btholt.github.io/complete-intro-to-containers/tags
Docker CLI
01:47:35 - 02:02:46
Docker CLI
Brian shares a few commands in the Docker CLI that give the container's history, pause the container, erase the container, or run a container with, and how to prune stopped containers. - https://btholt.github.io/complete-intro-to-containers/docker-cli
The Dockerfile
Dockerfiles Preamble
02:02:47 - 02:14:41
Dockerfiles Preamble
Brian demonstrates how to create a Dockerfile, adds a series of instructions in the Dockerfile that will give information about how the container should run, and how to tag a container and run it. - https://btholt.github.io/complete-intro-to-containers/dockerfile
Build a Node.js App
02:14:42 - 02:23:19
Build a Node.js App
Brian demonstrates how to build a Node.js application within a container, and writes a Dockerfile for a Node app. - https://btholt.github.io/complete-intro-to-containers/build-a-nodejs-app
Run a Node.js App
02:23:20 - 02:30:39
Run a Node.js App
Brian explains how to add publishing ports, how to stop a running container, and how to set up a secure user within the container that is different from the root user.
Add Dependencies to a Node.js App
02:30:40 - 02:41:58
Add Dependencies to a Node.js App
Brian demonstrates how to install dependencies into the new Node.js app, making the app more complex, and adds a Dockerfile to the app. - https://btholt.github.io/complete-intro-to-containers/more-complicated-nodejs-app
EXPOSE
02:41:59 - 02:46:17
EXPOSE
Brian explains what port mapping is using EXPOSE, a Dockerfile command that explicitly instructs users to check a specific port, and demonstrates that it is more convinient to add this information to the markdown of a specific app, instead of Dockerfile. - https://btholt.github.io/complete-intro-to-containers/expose
Layers
02:46:18 - 02:50:53
Layers
Brian demonstrates that a Docker container is composed of layers, and explains how to add a COPY command to the Docker file that will cache the layers of the built container and skip right to the new added layers when rebuilding a container. - https://btholt.github.io/complete-intro-to-containers/layers
Docker Ignore
02:50:54 - 02:53:51
Docker Ignore
Brian demonstrates how to add a dockerignore file, and explains that the files mentioned within the dockerignore document are files that should not be copied from the host operating system into the container, but that are still necessary within a project.
Making Tiny Containers
Alpine Linux
02:53:52 - 03:02:00
Alpine Linux
Brian demonstrates how to use Alpine Linux, and explains that Alpine Linux is the smallest barebone distribution of Linux, it is therefore more secure because there are less files and less vulnerabilities. - https://btholt.github.io/complete-intro-to-containers/alpine-linux
Alpine Node.js Container
03:02:01 - 03:10:04
Alpine Node.js Container
Brian demonstrates how to build a container from scratch using Alpine Linux, and explains that the goal is to build a container that is smaller than the standard Alpine container, and simpler. A Node.js app is added to the container. - https://btholt.github.io/complete-intro-to-containers/making-our-own-alpine-nodejs-container
Multi-Stage Builds
03:10:05 - 03:17:47
Multi-Stage Builds
Brian demonstrates how to create a multistage build, and explains that it is more secure to build smaller Alpine Node.js containers and only gives the tools necessary to build the container. Multi-stage builds are useful to optimize Dockerfiles by keeping them easy to read and maintain. - https://btholt.github.io/complete-intro-to-containers/multi-stage-builds
Static Assets Project Exercise
03:17:48 - 03:27:54
Static Assets Project Exercise
Students are instructed to create a multi stage build, copy a React project, build it, and transfer it to an NGINX container. - https://btholt.github.io/complete-intro-to-containers/static-assets-project
Static Assets Project Solution
03:27:55 - 03:34:23
Static Assets Project Solution
Brian live codes the solution to the static assets project exercise.
Features in Docker
Bind Mounts
03:34:24 - 03:43:42
Bind Mounts
Brian explains that bind mounts ship files from the host computer into the container. Bind mounts allow access to preexisting development environments, which fast forwards the work of engineers. - https://btholt.github.io/complete-intro-to-containers/bind-mounts
Volumes
03:43:43 - 03:55:25
Volumes
Brian describes volume mounts as tools that maintain state between runs by saving the results from the previous run. - https://btholt.github.io/complete-intro-to-containers/volumes
Containers & Dev Environment
03:55:26 - 04:05:56
Containers & Dev Environment
Brian builds a Hugo static site within a container, and explains that containers can also be development environments, which makes them shareable and recreatable. - https://btholt.github.io/complete-intro-to-containers/dev-containers
Dev Containers with Visual Studio Code
04:05:57 - 04:21:16
Dev Containers with Visual Studio Code
Brian demonstrates how to set up dev containers using VS Code and explains that one can open a remote container using VS Code. - https://btholt.github.io/complete-intro-to-containers/visual-studio-code
Networks & Docker: MongoDB Container
04:21:17 - 04:28:50
Networks & Docker: MongoDB Container
Brian introduces networking in Docker by connecting multiple containers to each other, and builds a container using MongoDB. - https://btholt.github.io/complete-intro-to-containers/networking
Networks & Docker: Client Side Container
04:28:51 - 04:37:04
Networks & Docker: Client Side Container
Brian demonstrates how to connect two different containers by live coding a Node.js application in a container and connecting it to the container created in the previous section.
Multi Container Projects
Docker Compose
04:37:05 - 04:50:33
Docker Compose
Brian explains how to build a docker-compose.yml file which sets up multiple containers without needing to build a development environment for each container. - https://btholt.github.io/complete-intro-to-containers/docker-compose
Docker Compose & nodemon
04:50:34 - 04:57:44
Docker Compose & nodemon
Brian adds nodemon, a file watcher that restarts Node every time it notices a file change, making development more seemless, and demonstrates how to start multiple containers at the same time.
Kubernetes Fundamentals
04:57:45 - 05:05:58
Kubernetes Fundamentals
Brian explains that Kubernetes is used for production workload and is useful when a lot of containers and different services are involved with complex relationships with each other, and goes over the fundamental terminology and concepts of Kubernetes. - https://btholt.github.io/complete-intro-to-containers/kubernetes
Kubernetes & kubectl
05:05:59 - 05:12:02
Kubernetes & kubectl
Brian demonstates how to interact with Kubernetes, explains that using Kubernetes is a complex task that generally happens during production, and demonstrates how to use kubectl. Kubectl is a command line interface that manages a Kubernetes cluster.
Kompose
05:12:03 - 05:21:17
Kompose
Brian introduces the Kompose tool, and demonstrates how to convert docker-compose.yml into a Kubernetes file. Kompose is a conversion tool that transforms Docker Compose to container orchestrators such as Kubernetes. - https://btholt.github.io/complete-intro-to-containers/kompose
Multiple Containers with Kompose
05:21:18 - 05:27:07
Multiple Containers with Kompose
Brian demonstrates how to run multiple containers using Kompose, how to delete all of the newly created containers, and how to convert all files to Kubernetes files.
OCI
Buildah
05:27:08 - 05:34:16
Buildah
Brian explores alternatives to Docker, starting with Buildah. Buildah allows users to build containers using bash scripts or to build an OCI container with a Dockerfile via Buildah. - https://btholt.github.io/complete-intro-to-containers/buildah
Buildah & Docker
05:34:17 - 05:40:54
Buildah & Docker
Brian demonstrates how to build a Buildah container within a Docker container.
Podman
05:40:55 - 05:49:44
Podman
Brian introduces Podman which allows users to run OCI or Docker container, and runs the previously built container with Podman. - https://btholt.github.io/complete-intro-to-containers/podman
Wrapping Up
Wrapping Up
05:49:45 - 06:04:47
Wrapping Up
Brian wraps up the course by sharing additional topics that students can learn about, additional resources about non Docker containers, and information about orchestration systems such as Docker Swarm, Apache Mesos, and Hashicorp Nomad. Questions are fielded from the audience about container monitoring, using Gatsby with containers, and the difference between CMD and run. - https://btholt.github.io/complete-intro-to-containers/