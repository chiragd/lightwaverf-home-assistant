# Lightwave RF Component (Platform) for Home Assistant
Here's an integration of LightwaveRF with Home Assistant (HASS).

It's very crude, but does work. It's been working for me for several years with the 1st generation of LightWave kit. I have not tested this with the newer (2nd gen) Lightwave products.

## Caveat
This code may show your devices in the Home Assistant UI, but it may not be able to control the lights for you. The code speaks directly to your Lightwave WiFi Link. Obviously, if you don't have a WiFi Link, then this isn't going to work for you.

Secondly, and most importantly your device running home assistant (in my case a raspberry pi) needs to be "authorised" to send messages to the WiFi Link. This script does not handle this yet. If there's demand, I'll try to get this pairing / authorisation process into the HASS UI, so it's easy for everyone.

## Installation
Take the file and drop it in with your home-assistant installation. Follow the instructions on the home-assistant website. If you need help, let me know.
