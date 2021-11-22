from typing import Iterable

from .client import SwitchBotClient
from . import devices


class SwitchBot:
    def __init__(self, token: str):
        self.client = SwitchBotClient(token)

    def devices(
        self, ignore_uncalibrated: bool = False, ignore_grouped: bool = False
    ) -> Iterable[devices.Device]:
        for device in self.client.get("devices")["body"]["device_list"]:
            calibrated = device.get("calibrate", True)
            master = device.get("master", True)
            grouped = device.get("group", False) and not master

            if ignore_uncalibrated and not calibrated:
                continue

            if ignore_grouped and grouped:
                continue

            device_cls = devices.Device
            try:
                device_member = getattr(devices, device["device_type"].replace(" ", ""))
                if issubclass(device_member, devices.Device):
                    device_cls = device_member
            except (TypeError, AttributeError):
                pass

            yield device_cls(client=self.client, **device)
