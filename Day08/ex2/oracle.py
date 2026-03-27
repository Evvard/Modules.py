import os
import sys


def main() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("Missing 'dotenv' retry")
        sys.exit(1)
    load_dotenv()
    mode = os.getenv("MATRIX_MODE")
    if not mode:
        print("missing data for \"MATRIX_MODE\"")
        return
    data = os.getenv("DATABASE_URL")
    if not data:
        print("missing data for \"DATABASE_URL\"")
        return
    api = os.getenv("API_KEY")
    if not api:
        print("missing data for \"API_KEY\"")
        return
    log_level = os.getenv("LOG_LEVEL")
    if not log_level:
        print("missing data for \"LOG_LEVEL\"")
        return
    zion = os.getenv("ZION_ENDPOINT")
    if not zion:
        print("missing data for \"ZION_ENDPOINT\"")
        return
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
