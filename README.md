# Lightwave RF Component (Platform) for Home Assistant
Here's an integration of LightwaveRF with Home Assistant (HASS).

It's very crude, but does work. It's been working for me for several years with the 1st generation of LightWave kit. I have not tested this with the newer (2nd gen) Lightwave products.

## Caveat
This code is provided as a starting point, but is not yet a complete solution. It may not work out of the box for you.

This code may show your devices in the Home Assistant UI, but it may not be able to control the lights for you. The code speaks directly to your Lightwave WiFi Link. Obviously, if you don't have a WiFi Link, then this isn't going to work for you.

Secondly, and most importantly, your device running home assistant (in my case a raspberry pi) needs to be "authorised" to send messages to the WiFi Link. This script does not handle this yet. If there's demand, I'll try to get this pairing / authorisation process into the HASS UI, so it's easy for everyone.

In the meantime, if you need help with the pairing part, let me know.

## Installation
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
