from collections import Counter
file_name = input("Masukkan nama file: ")

try:
    with open(file_name, 'r') as file:
        email_count = Counter(line.split()[1] for line in file if line.startswith("From "))
    print(email_count)

except FileNotFoundError:
    print("File tidak ditemukan.")