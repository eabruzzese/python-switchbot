# switchbot-cloud

A Python library to control SwitchBot devices via the SwitchBot API. Requires devices to be connected to a SwitchBot hub.

This library was largely based on [`python-switchbot`](https://github.com/jonghwanhyeon/python-switchbot).

## Requirements
- Python 3.6.2+
- [A SwitchBot Token](https://github.com/OpenWonderLabs/SwitchBotAPI#getting-started)

## Installation
```python
pip install switchbot-cloud
```

## Usage
```python
from switchbot_cloud import SwitchBot

switchbot = SwitchBot(token="4fa1d41c2678e70dd02ccbdb004026a6bad75ccdeae01f61ffb81732ced302f3e07a2a18ff4567cebb795035b6e62bd5")

# List your devices.
devices = list(switchbot.devices())
# [Meter(device_id=C4A110CFED7A),
#  HubMini(device_id=CE1475742160),
#  Curtain(device_id=D33E65B08B2D),
#  Curtain(device_id=DBF2AF795AA2),
#  Curtain(device_id=DE04A942640F),
#  MotionSensor(device_id=DF9DABC7425A),
#  Bot(device_id=E0C2FA36B914),
#  ContactSensor(device_id=E4790F79C7BE),
#  Curtain(device_id=F7D9E52FD7A7),
#  Curtain(device_id=F7EF7A47682B),
#  Curtain(device_id=FC3CEAE7DC84),
#  Humidifier(device_id=FCF5C43DE5DA)]

# Exclude grouped and uncalibrated devices:
devices = list(switchbot.devices(ignore_grouped=True, ignore_uncalibrated=True))
# [Meter(device_id=C4A110CFED7A),
#  HubMini(device_id=CE1475742160),
#  Curtain(device_id=D33E65B08B2D),
#  Curtain(device_id=DBF2AF795AA2),
#  Curtain(device_id=DE04A942640F),
#  MotionSensor(device_id=DF9DABC7425A),
#  Bot(device_id=E0C2FA36B914),
#  ContactSensor(device_id=E4790F79C7BE),
#  Humidifier(device_id=FCF5C43DE5DA)]

# Fetch basic device information:
meter = devices[0]
meter.__dict__
# {'client': <switchbot_cloud.client.SwitchBotClient at 0x10b50dcd0>,
#  'device_id': 'C4A110CFED7A',
#  'device_name': 'Meter',
#  'device_type': 'Meter',
#  'hub_device_id': '000000000000'}

# Fetch device-specific attributes from the device status:
meter.status
# {'device_id': 'C4A110CFED7A',
#  'device_type': 'Meter',
#  'hub_device_id': 'CE1475742160',
#  'humidity': 42,
#  'temperature': 20.1}

# Status attributes can be accessed directly from the device if you know their names:
meter.humidity
# 42

# Send commands to your devices:
curtain = devices[2]
curtain.command("set_position", "0,ff,50")
# Some device classes have helpful methods for common commands:
curtain.set_position(50)
curtain.open()
curtain.close()
```
