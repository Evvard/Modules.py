import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    Id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report:")
    print()

    print(f"[STANDARD] Archive status from ARCH_7742: {Id}", file=sys.stdout)
    print(f"[ALERT] System diagnostic: {status}", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print("\nThree-channel communication test successful.")
