from typing import Generator


def generator_for_players() -> Generator[str, None, int]:
    event = 1
    player = ["alice", "bob", "charlie", "pommeau_de_douche", "Hit",
              "Net", "Piegeamorues42"]
    level = [5, 12, 8, 9, 55, 7, 999]
    achivment = ['killed monster', 'found treasure', 'leveled up', 'noscope',
                 'kill himself', 'take health', 'take potion of invisibility']
    levl = 0
    tresure = 0
    for i in range(1000):
        if i == 0:
            msg = (f"Event 1: Player {player[0]} "
                   f"(level {level[0]}) {achivment[0]}")
            yield msg
        elif i == 1:
            msg = (f"Event 2: Player {player[1]} "
                   f"(level {level[1]}) {achivment[1]}")
            yield msg
            tresure += 1
            msg = (f"Event 3: Player {player[2]} "
                   f"(level {level[2]}) {achivment[2]}")
            yield msg
            levl += 1
        else:
            z = 0
            players = player[i % len(player)]

            while players != player[z]:
                z += 1
            achivment_now = achivment[i % 7]
            if achivment_now == 'leveled up':
                level[z] += 1
                levl += 1
            elif achivment_now == 'found treasure':
                tresure += 1
            yield f"Event {event}: Player {player} (level {z}) {achivment_now}"
        event += 1
    return (tresure, len(player), sum(level), levl)


def fibonacci(max_n: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    z = 0
    while z < max_n:
        yield a
        a, b = b, a + b
        z += 1


def prime(max_n: int) -> Generator[int, None, None]:
    n = 2
    while n <= max_n:
        i = 2
        is_prime = True
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            yield n
        n += 1


if __name__ == "__main__":

    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events..\n")
    generator = generator_for_players()
    y = 0
    try:
        while y < 1000:
            event = next(generator)
            if y < 3:
                print(event)
            y += 1
        while True:
            next(generator)
    except StopIteration as e:
        tresure, player_count, level_sum, level_up = e.value
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {y}")
    print(f"High-level players ({player_count}): {level_sum}")
    print(f"Treasure events: {tresure}")
    print(f"Level-up events: {level_up}\n")
    print("Memory usage: Constant (streaming)")
	calculer le temps d'exécution d'un programme python
    print("=== Generator Demonstration ===")
    lst = []
    for nombre in fibonacci(10):
        lst += [nombre]
    print("Fibonacci sequence (first 10): ", end="")
    print(*lst, sep=", ")
    print("Fibonacci sequence (first 10):")

    lst = []
    for nombre in prime(11):
        lst += [nombre]
    print("Prime numbers (first 5): ", end="")
    print(*lst, sep=", ")
