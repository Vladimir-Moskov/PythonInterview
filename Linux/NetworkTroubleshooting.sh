#####################################################
# https://www.youtube.com/watch?v=PVOuff-p420


# uname - print system information
uname -a

#  ip - show / manipulate routing, network devices, interfaces and tunnels
# link | address | addrlabel | route | rule | neigh | ntable | tunnel | tuntap | maddress | mroute |
#                mrule | monitor | xfrm | netns | l2tp | tcp_metrics | token | macsec
ip link
# SYSTEM ip addressing
ip addr

# network assesability
ping 8.8.8.8 -c5
traceroute 8.8.8.8
ping www.google.ca

# install - sudo apt update && sudo apt install dnsutils
# DNS troubleshooting
dig www.apple.ca

netstat
netstat -l

ifup - bring a network interface up
ifdown - take a network interface down
ifquery - parse interface configuration



cat /etc/*-release
uptime -p
free -m
# list of open files
lsof -i
lsof -u

cat /proc/cpuinfo
cat /proc/meminfo
df -h
du -sh /
du -sh /boot
# list block device
lsblk
fdisk -l

# mount usb
mkdir /media/usb_32/
mount /dev/sda1 /media/usb_32/
mkfs.ext4 /dev/sdb1

mount /dev/sda1 /media/dick_a1/
mount /dev/sda2 /media/dick_a2/
umount /media/dick_a1/
umount /media/dick_a2/

sudo apt-get install smartmontools
sudo smartctl --scan
sudo smartctl --all /dev/sdb1

fsck.ext4 -f -C0 /dev/sdb1
e2fsck -b 8193 /dev/sdb1
e2fsck -b 32768 /dev/sdb1

ps aux
man -k pam.conf

apt-get install rpm
rpm -qa hhtpd
