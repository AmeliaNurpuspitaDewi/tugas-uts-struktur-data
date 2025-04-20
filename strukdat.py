import pandas as pd
import os

# Fungsi untuk load data dari file Excel
def load_data(filename):
    df = pd.read_excel(filename)

    # Semua kolom jadi string dulu
    df['Tahun Terbit'] = df['Tahun Terbit'].apply(lambda x: str(int(float(x))) if pd.notnull(x) else 'N/A')

    return df.to_dict(orient='records')

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Linear Search
def linear_search(data, field, keyword):
    return [row for row in data if keyword.lower() in str(row[field]).lower()]

# Binary Search (mengembalikan semua data yang cocok)
def binary_search(data, field, target):
    target_str = str(target).lower()

    # Urutkan data
    data_sorted = sorted(data, key=lambda x: str(x[field]).lower() if pd.notnull(x[field]) else "")
    
    results = []
    low, high = 0, len(data_sorted) - 1

    # Cari satu posisi yang cocok dulu
    while low <= high:
        mid = (low + high) // 2
        mid_value = str(data_sorted[mid][field]).lower()

        if mid_value == target_str:
            # Cari semua hasil yang cocok di kiri dan kanan
            left = mid
            while left >= 0 and str(data_sorted[left][field]).lower() == target_str:
                left -= 1
            right = mid
            while right < len(data_sorted) and str(data_sorted[right][field]).lower() == target_str:
                right += 1
            return data_sorted[left+1:right]  # Kembalikan semua yang cocok
        elif mid_value < target_str:
            low = mid + 1
        else:
            high = mid - 1

    return []  # Tidak ditemukan

# Fungsi tampilkan hasil
def tampilkan_data(r, index):
    print(f"\n--- #{index+1} ---")
    print(f"Judul Paper   : {r.get('Judul Paper', 'N/A')}")
    print(f"Tahun Terbit  : {r.get('Tahun Terbit', 'N/A')}")
    print(f"Nama Penulis  : {r.get('Nama Penulis', 'N/A')}")
    print(f"Abstrak       : {r.get('Abstrak (langusung copas dari paper)', 'N/A')}")
    print(f"Kesimpulan    : {r.get('Kesimpulan (Langusung copas dari paper)', 'N/A')}")
    print(f"Link Paper    : {r.get('Link Paper', 'N/A')}")
    print("-" * 40)

# Program utama
def main():
    filename = r".vscode/UTS STRUKTUR DATA/Struktur_Data_Dataset_Kelas_A_B_C (6).xlsx"
    data = load_data(filename)

    fields = {
        "1": "Judul Paper",
        "2": "Tahun Terbit",
        "3": "Nama Penulis"
    }

    while True:
        clear_screen()
        print("=== PROGRAM PENCARIAN DATA PAPER ===")
        print("Pilih metode pencarian:")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Keluar")
        method = input("Pilihan (1/2/3): ")

        if method == "3":
            print("Terima kasih! Program selesai.")
            break

        print("\nPilih berdasarkan kolom:")
        print("1. Judul Paper")
        print("2. Tahun Terbit")
        print("3. Nama Penulis")
        field_option = input("Pilihan (1/2/3): ")

        if field_option not in fields:
            print("Pilihan kolom tidak valid.")
            input("Tekan Enter untuk kembali ke menu...")
            continue

        field = fields[field_option]
        keyword = input(f"Masukkan keyword untuk pencarian {field}: ")

        if method == "1":
            result = linear_search(data, field, keyword)
            print(f"\nHasil Linear Search pada '{field}':")
            if result:
                for i, r in enumerate(result):
                    tampilkan_data(r, i)
            else:
                print("Tidak ditemukan.")
        elif method == "2":
            result = binary_search(data, field, keyword)
            print(f"\nHasil Binary Search pada '{field}':")
            if result:
                for i, r in enumerate(result):
                    tampilkan_data(r, i)
            else:
                print("Tidak ditemukan.")
        else:
            print("Metode pencarian tidak valid.")

        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()


