#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
total_expenses = 0
parent_money = 0
month = 0
while(month < 10):
    if(month == 0):
        total_expenses = expenses
    elif(month >= 1):
        total_expenses = total_expenses * 1.03
    month+=1
    dif = round(total_expenses-educational_grant, 2)
    parent_money+=dif
print('Студенту надо попросить',parent_money,'рублей')
    