import time


def event_generator(count: int):
    players: list[str] = ["alice", "bob", "charlie", "david"]
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, count + 1):
        player = players[i % len(players)]
        action = actions[i % len(actions)]
        level = (i * 7) % 20 + 1
        yield {"id": i, "player": player, "level": level, "action": action}


def fibonacci_gen(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_gen(n: int):
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


def main() -> None:
    print("=== Game Data Stream Processor ===")
    num_events: int = 1000
    print(f"Processing {num_events} game events...")

    total_processed: int = 0
    high_level_players: int = 0
    treasure_events: int = 0
    levelup_events: int = 0

    start_time = time.time()

    for event in event_generator(num_events):
        total_processed += 1
        if event["level"] >= 10:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        elif event["action"] == "leveled up":
            levelup_events += 1
        if event["id"] <= 3:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")

    end_time = time.time()

    print("...")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {levelup_events}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("=== Generator Demonstration ===")

    fib_list = [str(x) for x in fibonacci_gen(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    prime_list = [str(x) for x in prime_gen(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")


if __name__ == "__main__":
    main()
