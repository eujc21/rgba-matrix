# 1) Configure micro controller with default values through bluetoo through bluetooth.https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md 
# 2) Check GPIO Pins either by sound or led.
# 3) Check internet connection by importing logo and displaying.(deadpool)
# 4)
import sh

class MicroController:
    def __init__(self, ssid, psk):
        self.ssid = ssid
        self.psk = psk
        self.wpa_conf = '/etc/wpa_supplicant/wpa_supplicant.conf'

    def modify_wpa_supplicant():
        sh.sed(
            '-i',
            f's/testing/${self.ssid}/',
            self.wpa_conf
        )
        sh.sed(
            '-i',
            f's/testingPassword/${self.psk}/',
            self.wpa_conf
        )
        return False
