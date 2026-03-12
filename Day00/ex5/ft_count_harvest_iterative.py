def ft_count_harvest_iterative() -> None:
    i = 1
    count = int(input("Days until harvest: "))
    while i <= count:
        print("Day", i)
        i = i + 1
    print("Harvest time!")
