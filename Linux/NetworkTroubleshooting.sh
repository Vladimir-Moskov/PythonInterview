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




