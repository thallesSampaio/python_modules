def handle_crisis(file_path: str) -> None:
    """Função mestre para gerenciar tentativas de acesso e crises."""

    if file_path == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{file_path}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{file_path}'...")

    try:
        with open(file_path, "r") as archive:
            content = archive.read().strip()
            print(f"SUCCESS: Archive recovered - {content}")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly - {e}")
        print("STATUS: Crisis handled, system stable")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    handle_crisis("lost_archive.txt")

    print("")

    handle_crisis("classified_vault.txt")

    print("")

    handle_crisis("standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
