import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    try:
        sys.stdout.write("Input Stream active. Enter archivist ID: ")
        sys.stdout.flush()
        archivist_id = sys.stdin.readline().strip()

        sys.stdout.write("Input Stream active. Enter status report: ")
        sys.stdout.flush()
        status_report = sys.stdin.readline().strip()
        if not archivist_id or not status_report:
            raise ValueError("Incomplete data. ID and Status are required.")
        sys.stdout.write(
            f"\n[STANDARD] Archive status from {archivist_id}: "
            f"{status_report}\n")

        sys.stderr.write(
            "[ALERT] System diagnostic: Communication channels verified\n")

        sys.stdout.write("[STANDARD] Data transmission complete\n")

        print("\nThree-channel communication test successful.")
    except KeyboardInterrupt:
        sys.stderr.write("\n[CRITICAL] Communication aborted by operator.\n")
        return
    except ValueError as e:
        sys.stderr.write(f"[ERROR] Protocol Violation: {e}\n")
    except Exception as e:
        sys.stderr.write(f"[SYSTEM FAILURE] Unexpected anomaly: {e}\n")


if __name__ == "__main__":
    main()
