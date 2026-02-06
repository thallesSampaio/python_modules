def main():
    vault_file = "vault_classified.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    with open(vault_file, "w") as file:
        file.write("[CLASSIFIED] Quantum encryption keys recovered\n")
        file.write("[CLASSIFIED] Archive integrity: 100%\n")

    print("\nSECURE EXTRACTION:")
    try:
        with open(vault_file, "r") as vault:
            content = vault.read()
            print(content.strip())
    except FileNotFoundError:
        print("[ERROR] Vault not found!")

    print("\nSECURE PRESERVATION:")
    with open(vault_file, "a") as vault:
        new_protocol = "[CLASSIFIED] New security protocols archived"
        vault.write(f"{new_protocol}\n")
        print(new_protocol)

    print("\nVault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
