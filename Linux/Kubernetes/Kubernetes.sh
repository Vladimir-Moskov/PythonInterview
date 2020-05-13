# https://blog.alexellis.io/raspberry-pi-homelab-with-k3sup/
# Kubernetus for Raspbery pi4

# https://www.youtube.com/watch?v=FufPIABXdTw
# Real-Life Kubernetes 2: How to Install kubectl

# https://github.com/groovemonkey/project-based-kubernetes/blob/master/01-kubectl-setup.md
sudo apt-get update && sudo apt-get install -y apt-transport-https
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl

which kubectl
kubectl help

# https://www.youtube.com/watch?v=68yKslO2Pz0&list=PLtK75qxsQaMIZ2hZhBbnvNZNFQHGUPrvV&index=4
# The Kubernetes Master-Node Architecture

sudo apt install cpu-checker && sudo kvm-ok
