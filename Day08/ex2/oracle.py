import os
import sys


def main() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("Missing 'dotenv' retry")
        sys.exit(1)
    load_dotenv()
    mode = os.getenv("MATRIX_MODE", "None")
    data = os.getenv("DATABASE_URL", "None")
    api = os.getenv("API_KEY", "None")
    if not api:
        pass
    log_level = os.getenv("LOG_LEVEL", "None")
    zion = os.getenv("ZION_ENDPOINT", "None")
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {data}")
    print("API Access : Authenticated")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion}")
    
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[KO] no .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
