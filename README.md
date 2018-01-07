# Lightwave RF Component (Platform) for Home Assistant
Here's an integration of LightwaveRF with Home Assistant (HASS).

It's very crude, but does work. It's been working for me for several years with the 1st generation of LightWave kit. I have not tested this with the newer (2nd gen) Lightwave products.

## Caveat
This code is provided as a starting point, but is not yet a complete solution. It may not work out of the box for you.

This code may show your devices in the Home Assistant UI, but it may not be able to control the lights for you. The code speaks directly to your Lightwave WiFi Link. Obviously, if you don't have a WiFi Link, then this isn't going to work for you.

Secondly, and most importantly, your device running home assistant (in my case a raspberry pi) needs to be "authorised" to send messages to the WiFi Link. This script does not handle this yet. If there's demand, I'll try to get this pairing / authorisation process into the HASS UI, so it's easy for everyone.

In the meantime, if you need help with the pairing part, let me know.

If you feel like trying, open a terminal on the device running home assistant and run the following command.

```
echo -ne "100,\!F*p." | nc -u -w1 192.168.1.110 9760
```

This should then show a message on your WiFi Link asking you to pair the device. Push the button on the WiFi Link to accept this. Once done, you should be able to control your lights via Home Asssistant.

## Installation
### Edit the Lightwave.Py file
You'll see at the top of the file there are a list of rooms and devices. If you want to, edit this to match your lightwaverf app. In the app you'll see a list of rooms. They are in order. The first room is R1. The second is R2 and so on. If you tap into a room on the lightwave app, you'll see a list of devices in that room. Again, these are in order. The first is D1, the second is D2 and so on. This allows you to determine the identifier for each device.

For example if the first room in my list is 'Kitchen' (R1) and within this room I have 3 light devices(D1), ceiling(D2), wall and cabinet (D3). Then my devices would be R1D1, R1D2, R1D3 respectively.

Remember you don't need to edit the file. Just note that all of your switches may not show and also that the naming may be wrong if you do not.


### Adding the Lightwave Component to Home Assistant
The lightwave.py file needs to be placed in the installation directory of Home Assistant. For me this is something like
```
/usr/local/share/lib/python3.4/homeassistant/component/lights/
``` 
There are instructions to follow on the instructions on the home-assistant website. If you need help, let me know.

### Adding LightwaveRF to your configuration file
Now that the component is installed you will need to add the setup to you configuration file.

```
light:
  - platform: lightwave
   
```

I think you'll also need to add your devices here. I'll update this section when I'm next near my home-assistant.
