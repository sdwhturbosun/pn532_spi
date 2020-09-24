
import binascii
import sys

import Adafruit_PN532 as PN532


# Setup how the PN532 is connected to the Raspbery Pi/BeagleBone Black.
# It is recommended to use a software SPI connection with 4 digital GPIO pins.

# Configuration for a Raspberry Pi:
CS   = 8   #pn532_nss----->rpi_ce0:8
MOSI = 9   #pn532_mosi---->rpi__miso:9
MISO = 10  #pn532_miso---->rpi__mosi:10
SCLK = 11  #pn532_sck----->rpi_sclk:11

# Configuration for a BeagleBone Black:
# CS   = 'P8_7'
# MOSI = 'P8_8'
# MISO = 'P8_9'
# SCLK = 'P8_10'

# Create an instance of the PN532 class.
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)

# Call begin to initialize communication with the PN532.  Must be done before
# any other calls to the PN532!
pn532.begin()

# Get the firmware version from the chip and print(it out.)
ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

# Main loop to detect cards and read a block.

while True:
    print('Waiting for MiFare card...')
    # Check if a card is available to read.
    uid = pn532.read_passive_target()
    
    # Try again if no card is available.
    if uid is None:
        continue
    uid=format(binascii.hexlify(uid))
    print("UID:",uid)
    name=input("Input name:")
    phone=input("Input phone:")
    f=open("students","a")
    studentinfo=uid+"_"+name+"_"+phone
    f.write(studentinfo)
    f.close()
    print("ok")
    

