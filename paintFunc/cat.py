import simple_draw as sd

def draw_cat(x, y, color):
    # body
    sd.ellipse(left_bottom=sd.get_point(x-30, y-60), right_top=sd.get_point(x+30, y))
    
    sd.circle(center_position=sd.get_point(x, y+30), radius=30, color=color, width=0)
    
    sd.polygon([sd.get_point(x-30, y+30), sd.get_point(x-20, y+80), sd.get_point(x-10, y+50)], color=color)
    sd.polygon([sd.get_point(x+30, y+30), sd.get_point(x+20, y+80), sd.get_point(x+10, y+50)], color=color)

    sd.circle(center_position=sd.get_point(x-15, y+45), radius=5, color=sd.COLOR_BLACK, width=0)
    sd.circle(center_position=sd.get_point(x+15, y+45), radius=5, color=sd.COLOR_BLACK, width=0)
    sd.circle(center_position=sd.get_point(x-15, y+45), radius=2, color=sd.COLOR_WHITE, width=0)
    sd.circle(center_position=sd.get_point(x+15, y+45), radius=2, color=sd.COLOR_WHITE, width=0)
    
    sd.circle(center_position=sd.get_point(x, y+30), radius=3, color=sd.COLOR_BLACK, width=0)
    
    sd.line(start_point=sd.get_point(x-15, y+35), end_point=sd.get_point(x-35, y+35))
    sd.line(start_point=sd.get_point(x+15, y+35), end_point=sd.get_point(x+35, y+35))
    
    sd.line(start_point=sd.get_point(x+20, y-10), end_point=sd.get_point(x+40, y-50), width=3)
    
    sd.circle(center_position=sd.get_point(x-20, y-60), radius=10, color=color, width=0)
    sd.circle(center_position=sd.get_point(x+20, y-60), radius=10, color=color, width=0)
