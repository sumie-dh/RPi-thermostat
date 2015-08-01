# RPi-thermostat
Thermostat for RPi using  DS18B20 sensor, WiringPi and Tempita

configuration of DS18B20 sensor and stuff around "checktemp" command :http://www.reuk.co.uk/DS18B20-Temperature-Sensor-with-Raspberry-Pi.htm
download adn install Tempita: apt-get install python-tempita
download and install WiringPi: http://wiringpi.com/download-and-install/

connection of cables for controling your device by python script is on pin 13 and 14 (ground) of physical numbering , check numbering of pins on your own RPi with command: gpio readall and edit values in code if you need different settings.
