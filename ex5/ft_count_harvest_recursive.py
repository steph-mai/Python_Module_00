def ft_count_harvest_recursive() -> None:

    count: int = int(input("Days until harvest: "))

    def ft_recursive(current_day: int, max_days: int) -> None:
        if current_day > max_days:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        ft_recursive(current_day + 1, max_days)
    ft_recursive(1, count)
