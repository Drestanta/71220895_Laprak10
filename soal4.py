# Meminta pengguna untuk memasukkan nama file
file_name = input("Masukkan nama file: ")

try:
    # Membuka file dan menghitung jumlah pesan dari setiap domain
    with open(file_name, 'r') as file:
        domain_count = {}
        for line in file:
            if line.startswith("From "):
                domain = line.split()[1].split('@')[1]
                domain_count[domain] = domain_count.get(domain, 0) + 1

    # Mencetak dictionary yang berisi jumlah pesan dari setiap domain
    print(domain_count)

except FileNotFoundError:
    print("File tidak ditemukan.")
