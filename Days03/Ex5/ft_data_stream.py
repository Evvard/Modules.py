from typing import Generator

def generator_for_players() -> Generator[str, None, None]:
    event = 1
    player = ["alice", "bob", "charlie", "pommeau_de_douche", "Hit", "Net", "Piegeamorues42"]
    level = [5, 12, 8, 9, 55, 7, 8, 999]
    achivment = ['killed monster', 'found treasure', 'leveled up', 'noscope',
                     'kill himself', 'take health', 'take potion of invisibility']
    tresure = 0
    for i in range(1000):
        if i == 0:
            yield f"Event 1: Player {player[1]} (level {level[1]}) {achivment[1]}"
        elif i == 1:
            yield f"Event 2: Player {player[2]} (level {level[2]}) {achivment[2]}"
            tresure += 1
        elif i == 2:
            yield f"Event 3: Player {player[3]} (level {level[3]}) {achivment[3]} "
            level += 1
        else:
            z = 0
            players = player[i % 3]

            while players != player[z]:
                z += 1
            achivment_now = achivment[i % 7]
            if achivment_now == "level up":
                level += 1
            elif achivment_now == "found treasure":
                tresure += 1
            yield f"Event {event}: Player {player} (level {z}) {achivment_now}"
        event += 1

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
    


next(), iter(), range(), len(), print(), typing.Generator










if __name__ == "__main__":

    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events..\n")
















    print("=== Generator Demonstration ===")
    lst = []
    for nombre in fibonacci(10)
        lst += [nombre]
    print("Fibonacci sequence (first 10): ", end="")
    print(*lst, sep=", ")
    print("Fibonacci sequence (first 10):")

    lst = []
    for nombre in prime(11):
        lst += [nombre]
    print("Prime numbers (first 5): ", end="")
    print(*lst, sep=", ")
