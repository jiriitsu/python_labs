import dearpygui.dearpygui as dpg
from dearpygui_ext import logger
from my_package.speed_calc import hdd_speed, ssd_speed, flash_speed
from docx import Document
dpg.create_context()
def my_func(sender, data):
    total_memory = dpg.get_value(input_MB)  + (dpg.get_value(input_GB)*1024)
    print(total_memory, "MB")
    dpg.set_value('hdd', round(hdd_speed(total_memory), 2))
    dpg.set_value('ssd', round(ssd_speed(total_memory), 2))
    dpg.set_value('flash', round(flash_speed(total_memory), 2))

    print("Запись/чтение на HDD займет", round(hdd_speed(total_memory), 2), "секунд")
    print("Запись/чтение на SSD займет", round(ssd_speed(total_memory), 2), "секунд")
    print("Запись/чтение на Flash займет", round(flash_speed(total_memory), 2), "секунд")
#def data_heh(sender, data):
    #dpg.set_value('input1', hdd_speed)

def saving_results(sender, data):
    doc = Document()
    doc.save()

    

with dpg.window(height = 600, width=800):
    input_MB = dpg.add_input_int(
        label = "MB",
        on_enter = True,
    )
    input_GB = dpg.add_input_int(
        label = "GB",
        on_enter = True,
        )   
    dpg.add_button(label = "Calculate ", callback = my_func)
    dpg.add_text('Reading/recording time in sec')
    dpg.add_input_text(label='HDD', callback=my_func, tag='hdd')
    dpg.add_input_text(label='SSD', callback=my_func, tag='ssd')
    dpg.add_input_text(label='Flash', callback=my_func, tag='flash')
    dpg.add_button(label='Save results', callback =saving_results)


    dpg.add_text
dpg.create_viewport(title='Devices', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()