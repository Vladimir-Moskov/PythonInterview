# https://www.digitalocean.com/community/tutorials/how-to-perform-basic-administration-tasks-for-storage-devices-in-linux
df -h
df -h -x tmpfs -x devtmpfs

# sblk - list block devices
sudo lsblk
#  disk and partition management
sudo lsblk --fs
# topology
sudo lsblk -t
#
lsblk -h
#  findmnt - find a filesystem
findmnt /mnt
