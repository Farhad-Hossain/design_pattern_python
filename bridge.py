from abc import ABC, abstractmethod

class Device(ABC):
    volume = 0

    @abstractmethod
    def get_name(self) -> str:
        pass

class Radio(Device):
    def get_name(self) -> str:
        return "Radio"

class TV(Device):
    def get_name(self) -> str:
        return "TV"

class Remote(ABC):
    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass
    
class BasicRemote(Remote):
    def __init__(self, device: Device):
        self.device = device

    def volume_up(self):
        self.device.volume += 1
        print(f"{self.device.get_name()} volume: {self.device.volume}")

    def volume_down(self):
        self.device.volume -= 1
        print(f"{self.device.get_name()} volume: {self.device.volume}")


if __name__ == "__main__":
    radio = Radio()
    tv = TV()
    
    remote = BasicRemote(radio)
    remote.volume_up()
    remote.volume_up()
    remote.volume_down()
    
    remote = BasicRemote(tv)
    remote.volume_up()
    remote.volume_up()
    remote.volume_down()