#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import time
import random
# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
sd.resolution = (1000, 1000)
o = sd.random_point
for _ in range(10):
    sd.circle(center_position=o, radius=40, color=sd.COLOR_GREEN)
    sd.circle(center_position=sd.Point(o.x - 20, o.y + 20), radius=10, color=sd.COLOR_BLACK)
    
    time.sleep(0.1)
sd.pause()

