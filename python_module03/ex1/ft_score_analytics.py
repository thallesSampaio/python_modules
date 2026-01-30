import sys


def commnad_line_receiver() -> list[int]:
    numbers: list[int] = []
    argc: int = len(sys.argv)
    i: int = 1
    while i < argc:
        try:
            number = int(sys.argv[i])
            numbers.append(number)
        except ValueError:
            print(f"Error: '{sys.argv[i]}' is not a valid number.")
        i += 1
    return numbers


def score_analytics(scores: list[int]) -> None:
    print("=== Player Score Analytics ===")
    if not scores:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ...")
        return None
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    numbers: list[int] = commnad_line_receiver()
    score_analytics(numbers)
