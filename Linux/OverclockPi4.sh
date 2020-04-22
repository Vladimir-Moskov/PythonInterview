
1.open up a terminal window - Control, Alt,T

2.apt update && apt upgrade

3.sudo rpi-update

4.sudo reboot

5.open up a terminal window - Control, Alt,T

6.sudo nano /boot/config.txt

7. scroll down to the very end and insert

over_voltage=4
arm_freq=2000

You can also overclock the GPU if needed - gpu_freq=600

prees Ctrl - X and save by pressing Y

8. SUdo reboot

9. open up a terminal window - Control, Alt,T

10.Type- watch -n1 vcgencmd measure_clock arm
this will display the current CPU speed in real time.

sysbench --num-threads=8 --test=cpu --cpu-max-prime=1800 run