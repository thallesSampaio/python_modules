def recover_data(file_path: str) -> None:
    try:
        if file_path != "new_discovery.txt":
            raise ValueError(
                f"Unauthorized Path: '{file_path}'"
                " violates preservation protocols.")
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
        entries: list[str] = [
            "New quantum algorithm discovered",
            "Efficiency increased by 347%",
            "Archived by Data Archivist trainee"]

        print(f"Initializing new storage unit: {file_path}")
        with open(file_path, "w") as file:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")

            counter: int = 1
            for content in entries:
                entry_header = (f"[ENTRY {counter:03d}]")
                file.write(f"{entry_header} {content}\n")
                print(f"{entry_header} {content}")
                counter += 1

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive {file_path} ready for long-term preservation.")
    except ValueError as e:
        print(e)
    except PermissionError:
        print(f"Security protocols deny write access to {file_path}")
    except Exception as e:
        print(f"CRITICAL FAILURE during inscription: {e}")


if __name__ == "__main__":
    recover_data("new_discovery.txt")
