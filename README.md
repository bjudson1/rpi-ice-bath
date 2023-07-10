# rpi-ice-bath
Contains code to run Raspberry Pi that controls ice bath


## Steps to Reproduce
1. sudo raspi-config
- Interface Optione
- Enable 1Wire

2. sudo nano /boot/config.txt

replace 
```dtoverlay=w1-gpio``` with ```dtoverlay=w1-gpio, gpiopin=4``` it should be the bottom line

3. pip3 install w1thermsensor