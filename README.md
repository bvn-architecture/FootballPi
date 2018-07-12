# FootballPi
Repo for the football Raspberry Pis

## Flash OS
1. [Download Raspbian Stretch **Lite**](https://www.raspberrypi.org/downloads/raspbian/)
2. [Download and install etcher](https://etcher.io/)
3. Flash SD of 8 GB or more via etcher with Raspbian Stretch Lite

![Flashing SD card with etcher](https://etcher.io/static/screenshot.gif)

## Get MAC Address
1. Plug Pi with flashed SD into screen with HDMI, ethernet, and a keyboard.  
2. Install git with: `sudo apt-get install git`  
3. clone this repo: `git clone https://github.com/bvn-architecture/FootballPi/`
4. `cd FootballPi`
5.  get MAC address `bash get_MAC NAMEOFPI` and save it in MAC Adresses.csv.
6. enter git login details

*The bash script attempts to change the password but currently fails*

## Change password
`passwd`, enter default password: *raspberry*  
enter new password (twice)

DONE!
