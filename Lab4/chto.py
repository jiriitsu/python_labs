import simple_draw as sd

sd.resolution = (600, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

for i in range(len(rainbow_colors)):
    def start_point(x=50):
        x += i * 30
        return x


    def end_point(x1=350):
        x1 += i * 30
        return x1


    sd.line(sd.get_point(start_point(), 50), sd.get_point(end_point(), 450), color=rainbow_colors[i], width=10)


sd.pause()