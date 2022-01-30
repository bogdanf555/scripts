from pushbullet import Pushbullet
from time import sleep

pb = Pushbullet("here goes your pushbullet access token")

print(pb.devices)

phone = pb.get_device("here goes the device name")
phone.push_note("Test notification", "This is a test message!")
