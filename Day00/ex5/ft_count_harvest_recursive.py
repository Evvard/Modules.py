def ft_count_harvest_recursive() -> None:
    start = int(input("Days until harvest: "))
    i = 1
    ft_count_recursive(start, i)


def ft_count_recursive(start: int, i: int) -> None:
    if i <= start:
        print("Day", i)
        i = i + 1
        ft_count_recursive(start, i)
    else:
        print("Harvest time!")
