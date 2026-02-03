def recover_data(filePath: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file = None
    try:
        print(f"\nAccessing Storage Vault: {filePath}")
        file = open(filePath, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f"{file.read()}")
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(f"\nError: Storage unit '{filePath}' not found.")
    except PermissionError:
        print(f"\nAccess Denied: No permission to read '{filePath}'.")
    except Exception as e:
        print(f"\nRecovery failed: {e}")
    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    recover_data("ancient_fragment.txt")
