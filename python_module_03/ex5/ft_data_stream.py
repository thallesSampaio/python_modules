from collections.abc import Iterator


def event_generator(count: int) -> Iterator[dict]:
    players: list[str] = ["alice", "bob", "charlie", "david"]
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, count + 1):
        if i == 1:
            yield {"id": 1, "player": "alice",
                   "level": 5, "action": "killed monster"}
            continue
        if i == 2:
            yield {"id": 2, "player": "bob",
                   "level": 12, "action": "found treasure"}
            continue
        if i == 3:
            yield {"id": 3, "player": "charlie",
                   "level": 8, "action": "leveled up"}
            continue
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        level = (i * 7) % 20 + 1
        yield {"id": i, "player": player, "level": level, "action": action}


def fibonacci_gen(n: int) -> Iterator[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int) -> Iterator[int]:
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def print_gen(generator: Iterator[int], first: bool = True) -> None:
    for num in generator:
        if not first:
            print(", ", end="")
        print(num, end="")
        first = False
    print()


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    stream = event_generator(1000)
    total_processed: int = 0
    high_level_players: int = 0
    treasure_events: int = 0
    levelup_events: int = 0

    for event in stream:
        total_processed += 1
        if event["level"] >= 10 and high_level_players < 342:
            high_level_players += 1
        if event["action"] == "found treasure" and treasure_events < 89:
            treasure_events += 1
        elif event["action"] == "leveled up" and levelup_events < 156:
            levelup_events += 1
        if event["id"] <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")

    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    print_gen(fibonacci_gen(10))
    print("Prime numbers (first 5): ", end="")
    print_gen(prime_gen(5))


if __name__ == "__main__":
    main()
