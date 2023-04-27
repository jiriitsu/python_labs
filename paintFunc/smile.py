import simple_draw as sd
def draw_smile (x, y, color):
    start_point = sd.get_point(x, y)
    sd.circle(start_point, 50, color, width = 1)
    sd.line(sd.get_point(x-10, y-20), sd.get_point(x+10, y-20), color, 2)
    sd.line(sd.get_point(x-15, y+20), sd.get_point(x-15, y+5), color, 2)
    sd.line(sd.get_point(x+15, y+20), sd.get_point(x+15, y+5), color, 2)
#sd.pause()