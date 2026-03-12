if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", 'r+') as file:
            print("Vault connection established with failsafe protocols\n")
            print(file.read())

            file.close()
            file = open("classified_data.txt", 'w')

            file.write("SECURE PRESERVATION:\n")
            file.write("[CLASSIFIED] New security protocols archived")
            file.close()

            file = open("classified_data.txt", 'r')
            print(f"\n{file.read()}")

            print("Vault automatically sealed upon completion")
            print("\nAll vault operations completed with maximum security.")
    except FileNotFoundError:
        print("\nFiles missing, operation stop")
