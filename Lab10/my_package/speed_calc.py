#флешка 200-350 МБ/с сред. 300
#хдд 200-300 МБ/с сред. 250
#ссд 600-700 МБ/с сред. 650

def hdd_speed(MB_value):
    sec_hdd = MB_value / 250
    return sec_hdd

def ssd_speed(MB_value):
    sec_ssd = MB_value / 650
    return sec_ssd

def flash_speed(MB_value):
    sec_flash = MB_value / 300
    return sec_flash