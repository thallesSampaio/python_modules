def recover_data(filePath: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    file = None
    entries: list[str] = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]

    try:
        print(f"\nInitializing new storage unit: {filePath}")
        file = open(filePath, "w")
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        c: int = 1
        for content in entries:
            entry_header = (f"[ENTRY {c:03d}]")
            file.write(f"{entry_header} {content}\n")
            print(f"{entry_header} {content}")
            c += 1

        file.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive {filePath} ready for long-term preservation.")
    except Exception as e:
        print(f"CRITICAL FAILURE during inscription: {e}")


if __name__ == "__main__":
    recover_data("new_discovery.txt")
