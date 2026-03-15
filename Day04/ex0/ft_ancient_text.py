if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        my_file = open('ancient_fragment.txt', 'r')
        print("Connection established...\n")
        print(my_file.read())
        my_file.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("Connection non established...\n")
        print("No file, No data, the files is not in the repertorie")
