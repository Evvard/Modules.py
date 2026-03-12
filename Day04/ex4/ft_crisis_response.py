if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")

    try:
        with open("lost_archive.txt", "r") as file:
            print("RESPONSE: Archive found in storage matrix")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("classified_vault.txt", "r") as file:
            print("RESPONSE: Security protocols autorise access")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except FileNotFoundError:
        print("RESPONSE: Classified_vault not found in storage matrix")
    print("STATUS: Crisis handled, security maintained\n")

    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as file:
            print("SUCCESS: Archive recovered - ``Knowledge preserved", end="")
            print(" for humanity\'\'")
    except FileNotFoundError:
        print("FAILED: Archive not recovered")
    print("STATUS: Normal operations resumed\n")
    print("All crisis scenarios handled successfully. Archives secure.")
