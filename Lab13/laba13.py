import tkinter as tk
from tkinter import ttk
from classes import *
class Application(tk.Tk):
    def __init__(self, storage_devices):
        super().__init__()
        self.title("Устройства памяти")
        self.geometry("500x400")

        self.storage_devices = storage_devices
        self.create_widgets()

    def create_widgets(self):
        self.device_var = tk.StringVar(self)
        self.device_var.set(self.storage_devices[0].name)

        self.volume_var = tk.DoubleVar(self)
        self.volume_var.set(0)

        self.unit_var = tk.StringVar(self)
        self.unit_var.set('Гб')

        device_option = ttk.OptionMenu(self, self.device_var, *(device.name for device in self.storage_devices))
        device_option.pack()

        volume_label = ttk.Label(self, text="Количество памяти:")
        volume_label.pack()

        volume_entry = ttk.Entry(self, textvariable=self.volume_var)
        volume_entry.pack()

        unit_option = ttk.OptionMenu(self, self.unit_var, 'Гб', 'Мб')
        unit_option.pack()

        calculate_button = ttk.Button(self, text="Рассчитать", command=self.calculate)
        calculate_button.pack()

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()

    def calculate(self):
        device_name = self.device_var.get()
        data_volume = self.volume_var.get()
        data_unit = self.unit_var.get()

        if data_unit == 'Мб':
            data_volume /= 1024

        device = next((device for device in self.storage_devices if device.name == device_name), None)
        if device is None:
            self.result_label['text'] = "Выберите устройство!"
            return

        time_required = device.calculate_time(data_volume)
        cost_per_gb = device.cost_per_gb()
        best_device = min(self.storage_devices, key=lambda device: device.cost_per_gb())

        self.result_label['text'] = f"Время записи/чтения: {round(time_required, 3)} сек\nСамое выгодное устройство: {best_device.name}"

hdd = HDD("HDD", 5000, 1000, 100)
ssd = SSD("SSD", 10000, 500, 200)
flash = Flash("Flash", 2000, 250, 150)

app = Application([hdd, ssd, flash])
app.mainloop()
