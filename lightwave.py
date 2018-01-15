"""
homeassistant.components.light.lightwave
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Demo platform that implements lights.

"""
import random
import socket

from homeassistant.components.light import (
    Light, ATTR_BRIGHTNESS)


LIGHT_COLORS = [
    [237, 224, 33],
    [255, 63, 111],
]

LIGHT_TEMPS = [240, 380]

# Below are generic rooms, with sample lightwave device IDs e.g. R1D1.
# At the moment we have to manually configure your LightWave Devices. If you need help getting the codes for your devices, let me know.
# You could try my devices and see how they work. Basically R represents a switch. D represents a dimmer on the switch, as far as I can tell.

def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    """ Find and return lightwave lights """
    add_devices_callback([
        LRFLight("Guest Bedroom Light", False, 'R1D1'),
        LRFLight("Office Ceiling Light", False, 'R2D1'),
        LRFLight("Office Wall Light", False, 'R2D2'),
        LRFLight("Living Room Wall Light", False, 'R3D1'),
        LRFLight("Living Room Light", False, 'R3D2'),
        LRFLight("Master Bedroom Light", False, 'R4D1')
    ])


class LRFLight(Light):
    """ Provides a demo switch. """
    # pylint: disable=too-many-arguments
    def __init__(self, name, state, deviceid, brightness=255):
        self._name = name
        self._state = state
        #self._rgb = rgb or random.choice(LIGHT_COLORS)
        #self._ct = ct or random.choice(LIGHT_TEMPS)
        self._brightness = brightness
        self._deviceid = deviceid
        #self._device_id = device_id

    @property
    def should_poll(self):
        """ No polling needed for a demo light. """
        return False

    @property
    def name(self):
        """ Returns the name of the device if any. """
        return self._name

    @property
    def brightness(self):
        """ Brightness of this light between 0..255. """
        return self._brightness

    #@property
    #def rgb_color(self):
    #    """ rgb color value. """
    #    return self._rgb

    #@property
    #def color_temp(self):
    #    """ CT color temperature. """
    #    return self._ct

    @property
    def deviceid(self):
        """ The Lightwave Device ID """
        return self._deviceid

    @property
    def is_on(self):
        """ True if device is on. """
        return self._state


    def send_command(self, msg):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        #command = "666, !R2D1F1|Turn On|Babas Lights"
        #register = "666, !F*p"
        sock.sendto(msg.encode('UTF-8'), ('255.255.255.255', 9760))
        sock.close

    def calculate_brightness(self, brightness):
        # the scale is 0 to 255 so we need to normalise to 0 to 100 first.
        old_range = 255 # 255 - 0 = 255
        new_range = 100 # 100 - 9 = 100
        new_value = (((brightness - 0) * new_range) / old_range)
        brightness32 = round(new_value * 0.32)
        return brightness32


    def turn_on(self, **kwargs):
        """ Turn the device on. """
        self._state = True

        #if ATTR_RGB_COLOR in kwargs:
        #    self._rgb = kwargs[ATTR_RGB_COLOR]

        #if ATTR_COLOR_TEMP in kwargs:
        #    self._ct = kwargs[ATTR_COLOR_TEMP]

        if ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]
            brightness_value = self.calculate_brightness(self._brightness)
            msg = '666, !%sFdP%d|Lights %d|%s ' % (self._deviceid, brightness_value, brightness_value, self._name)
            self.send_command(msg)
 
        print("LIGHTWAVE: Turning Lights On")
        #F1 = Light on and F0 = light off. FdP[0..32] is brightness. 32 is full. We want that when turning the light on.
        msg = '666, !%sFdP32|Turn On|%s ' % (self._deviceid, self._name)
        self.send_command(msg)
        print("LIGHTWAVE: finished")

        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        """ Turn the device off. """ 
        print("LIGHTWAVE: Turning Lights Off")
        msg = "666, !%sF0|Turn Off|%s " % (self._deviceid, self._name)
        self.send_command(msg)
        print("LIGHTWAVE: finished")
        self._state = False
        self.schedule_update_ha_state()
