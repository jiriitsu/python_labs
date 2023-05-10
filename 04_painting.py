#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать (или при необходимости написать) функции отрисовки
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
from paintFunc import rainbow, house, tree, rain, sun, smile, tree1, cat


sd.resolution = (1920, 1080)

sd.ellipse(sd.Point(-180, -250), sd.Point(2100, 250), color=sd.COLOR_GREEN)

rainbow_start = sd.Point(760, -150)
rainbow_rad = 1300
rainbow_width = 15
rainbow.draw_rainbow(rainbow_start, rainbow_rad, rainbow_width)

house_height = 400
house_width = 400
house_start = 560
house_lines_color = sd.COLOR_WHITE
house_color = sd.COLOR_DARK_ORANGE
house.draw_house(house_height+150, house_width, house_start, house_lines_color, house_color)

sun_start = sd.Point(300, 900)
sun_radius = 80
sun.drawing_sun(sun_start, sun_radius)

smile_color = sd.COLOR_DARK_GREEN
smile.draw_smile(1200, 300, smile_color)

tree_leaves_color = sd.COLOR_RED
tree_color = sd.COLOR_DARK_ORANGE
tree_start = sd.Point(1400, 150)
tree.draw_tree(tree_start, tree_leaves_color, tree_color)

tree1_leaves_color = sd.COLOR_PURPLE
tree1_color = sd.COLOR_DARK_ORANGE
tree1_start = sd.Point(1600, 50)
tree1.draw_tree(tree1_start, tree1_leaves_color, tree1_color)

cat_x = 1100
cat_y = 200
cat_color = sd.COLOR_DARK_YELLOW
cat.draw_cat(cat_x, cat_y, cat_color)
rain.draw_rain()

sd.pause()