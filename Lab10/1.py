import dearpygui.dearpygui as dpg
# The main script must always:

# Create the context create_context

# Create the viewport create_viewport

# Setup dearpygui setup_dearpygui

# Show the viewport show_viewport

# Start dearpygui start_dearpygui

# Clean up the context destroy_context
def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):
    dpg.add_text("SSD")
    dpg.add_text
    dpg.add_text("HDD")
    dpg.add_text("Flash")
    dpg.add_input_text(label="GB")
    dpg.add_slider_float(label="float")
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()