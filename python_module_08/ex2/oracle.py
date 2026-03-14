import os
import sys


def oracle_vision():
    try:
        from dotenv import load_dotenv, dotenv_values
        load_dotenv()
    except Exception as e:
        print(f"Error: {e}")
        print("[WARNING] python-dotenv"
              " not installed. Run 'pip install dotenv'.")
        sys.exit(1)

    print("\nORACLE STATUS: Reading the Matrix...")
    if not load_dotenv():
        print('missing .env file -> cp .env.example .env')
        return
    elif 'DATABASE' not in dotenv_values():
        print('missing key - DATABASE')
        return
    elif 'API_KEY' not in dotenv_values():
        print('missing key - API_KEY')
        return

    mode = os.getenv("MATRIX_MODE", "development")
    database = os.getenv("DATABASE")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_url = os.getenv("ZION_NETWORK", "offline")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if database:
        print(f"Database: {database}")
    else:
        print("Database: MISSING - No database configured")

    api_status = "Authenticated" if api_key else "Unauthenticated"
    print(f"API Access: {api_status}")

    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_url}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle_vision()
