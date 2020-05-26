############ 1. Monitoring and Troubleshooting Linux System Performance

# 1. Identifying System Resource Usage
cd /proc

ls -lah | less
ps aux | grep 78
ls -lah 78 | less
journalctl _PID=78
ls -p | grep -v / | column

less cpuinfo
less cpuinfo | grep processor
cat uptime
# or
uptime
# supportet filesystem types
less filesystems

# https://access.redhat.com/solutions/406773
less meminfo
free -k
free -h

# 2. Storage and Network Bandwidth Metrics
df -lah
df -t ext4
df -h | grep -v sys
# see inodes - amount free/used files count
df -ih
top
# network monitoring
apt-get install iftop
iftop
ip a
# from outside of the system
iftop -i eth0

# from inside of the system
apt-get install nethogs
nethogs eth0
curl https://www.pluralsight.com/

# 3. System Monitoring Solutions
apt-get install collectd
# collectd
# Nagios
# Munin
# Nmon
# cockpit

apt-get install cockpit
systemctl start cockpit
https://192.168.2.21:9090/dashboard
systemctl stop cockpit

# 4. Controlling System Resource Usage
systemctl status cockpit
systemctl status apache2
# limit service with current session only
systemctl disable apache2
# run service one every session only
systemctl enable apache2

# run 3 new processes in background
yes > /dev/null &
kill 26995
killall yes

# 5. Defining a Capacity Planning Strategy


########## 2. Building a Disaster Recovery Plan


########### 3. Maintaining System Integrity
# 0. Understanding Your System Profile
uname -a
dmidecode -q | less
sudo dmidecode -s chassis-type
sudo dmidecode -s baseboard-product-name
sudo dmidecode -s processor-frequency
sudo dmidecode -t bios | less

lshw | less
lshw -short
sudo lshw -C disk
sudo lshw -C network

apt-get install memtester
free -h
memtester 1500 1

# 1. Testing Your Hardware Integrity
apt-get install smartmontools
lsblk
smartctl /dev/mmcblk0
smartctl -i /dev/mmcblk
smartctl -A /dev/mmcblk
smartctl -l selftest /dev/mmcblk
smartctl -l xerror /dev/mmcblk
smartctl -l devstat /dev/mmcblk
smartctl -t short /dev/sda

# 2. Controlling Linux Kernels

cd /boot
ls -lah
nano /etc/default/grub
# remove older versions of kernel
apt --purge autoremove

##########  4. Building Software Packages for Linux

