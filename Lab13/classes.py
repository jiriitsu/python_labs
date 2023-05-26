from abc import ABC, abstractmethod

class StorageDevice(ABC):
    def __init__(self, name, price, size, speed):
        self._name = name
        self._price = price
        self._size = size
        self._speed = speed

    @abstractmethod
    def calculate_time(self, data_volume):
        pass

    @abstractmethod
    def cost_per_gb(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def size(self):
        return self._size

    @property
    def speed(self):
        return self._speed

    def __str__(self):
        return f"{self.name}: Цена: {self.price}, Размер: {self.size}, Скорость: {self.speed}"

    def __eq__(self, other):
        if not isinstance(other, StorageDevice):
            return NotImplemented
        return self.size == other.size and self.speed == other.speed


class HDD(StorageDevice):
    def calculate_time(self, data_volume):
        return data_volume / self.speed

    def cost_per_gb(self):
        return self.price / self.size


class SSD(StorageDevice):
    def calculate_time(self, data_volume):
        return data_volume / self.speed

    def cost_per_gb(self):
        return self.price / self.size


class Flash(StorageDevice):
    def calculate_time(self, data_volume):
        return data_volume / self.speed

    def cost_per_gb(self):
        return self.price / self.size
