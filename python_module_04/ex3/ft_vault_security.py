def main():
    vault_file = "classified_data.txt"
    security_protocols = "security_protocols.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    try:
        with open(vault_file, "r") as file:
            content = file.read()
            print(content.strip())
    except FileNotFoundError:
        print("[ERROR] Vault not found!")

    print("\nSECURE PRESERVATION:")
    try:
        with open(security_protocols, "r") as file:
            protocols = file.read()
            print(protocols.strip())
    except FileNotFoundError:
        print("[ERROR] Vault not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
