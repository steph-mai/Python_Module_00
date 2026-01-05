#!/usr/bin/env python3

def ft_count_harvest_recursive():

    count = int(input("Days until harvest: "))

    def ft_recursive(current_day, count):
        if current_day > count:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        ft_recursive(current_day + 1, count)
    ft_recursive(1, count)
