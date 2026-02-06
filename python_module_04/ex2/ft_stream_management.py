import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    sys.stdout.flush()
    archivist_id = sys.stdin.readline().strip()

    sys.stdout.write("Input Stream active. Enter status report: ")
    sys.stdout.flush()
    status_report = sys.stdin.readline().strip()

    sys.stdout.write(
        f"[STANDARD] Archive status from {archivist_id}: {status_report}\n")

    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n")

    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
