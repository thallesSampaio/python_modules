def recover_data(file_path: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print(f"\nAccessing Storage Vault: {file_path}")
        with open(file_path, "r") as file:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(f"{file.read()}")
            print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(f"\nError: Storage unit '{file_path}' not found.")
    except PermissionError:
        print(f"\nAccess Denied: No permission to read '{file_path}'.")
    except Exception as e:
        print(f"\nRecovery failed: {e}")


if __name__ == "__main__":
    recover_data("ancient_fragment.txt")
