# Fungsi Operasi String
def hitung_panjang(string):
    return len(string)

# Fungsi Concat
def gabung_string(strings, jumlah_spasi):
    print("========================")
    print("Pilihan String yang Tersedia :")
    for i, string in enumerate(strings):
        print(f"{i+1}. {string}")
    print("========================")
    
    selected_strings = input("Masukkan nomor string yang ingin digabungkan (Misal : 1 2) : ")
    selected_strings = [int(idx) for idx in selected_strings.split()]
    
    hasil = ""
    for idx in selected_strings:
        hasil += strings[idx-1] + (" " * jumlah_spasi)
    return hasil


# Fungsi Delete
def operasi_delete(strings, start, end):
    print("Pilihan String yang Tersedia :")
    for i, string in enumerate(strings):
        print(f"{i+1}. {string}")

    selected_strings = input("Masukkan nomor string untuk operasi delete : ")
    selected_strings = [int(idx) for idx in selected_strings.split()]

    hasil = ""
    for idx in selected_strings:
        hasil += strings[idx-1][:start-1] + strings[idx-1][start + end-1:]
    return hasil

#Fungsi Substring
def operasi_substr(string, start,jumlah):
    print("Pilihan String yang Tersedia :")
    for i, string in enumerate(strings):
        print(f"{i+1}. {string}")

    selected_strings = input("Masukkan nomor string untuk operasi substring : ")
    selected_strings = [int(idx) for idx in selected_strings.split()]

    hasil = ""
    for idx in selected_strings:
        hasil += strings[idx-1][start-1:start-1+jumlah]
    return hasil

# Fungsi Insert
def operasi_insert(string, posisi):
    print("Pilihan String yang Tersedia :")
    for i, string in enumerate(strings):
        print(f"{i+1}. {string}")

    string_pilihan = int(input("Masukkan nomor string yang akan disisipkan : "))
    if 1 <= string_pilihan <= len(strings):
        substring_insert = strings[string_pilihan-1]
        
        print("Pilihan String tujuan :")
        for i, string in enumerate(strings):
            print(f"{i+1}. {string}")
        string_tujuan = int(input("Masukkan nomor string tujuan : "))
        
        hasil = ""
        
        if 1 <= string_tujuan <= len(strings):
            hasil += strings[string_tujuan-1][:posisi-1] + substring_insert + strings[string_tujuan-1][posisi-1:]
            return hasil
        
        else:
            print("Nomor string tujuan tidak valid")
            
    else:
        print("Nomor string yang akan disisipkan tidak valid")

# Fungsi Memperlihatkan Banyaknya String
def banyak_string(string):
    print("Pilihan String yang Tersedia :")
    for i, string in enumerate(strings):
        print(f"{i+1}. {string}")

# Fungsi Penyimpan String
def save_strings():
    n = int(input("Masukkan Berapa String yang akan anda input : "))
    strings = []
    
    for i in range(n):
        user_input = input(f"Masukkan String ke-{i+1} : ")
        strings.append(user_input)
    return strings

# Input User
if __name__ == "__main__":
    strings = save_strings()
    while True:
        print("Pilihan Fungsi :")
        print("1. Hitung Panjang String")
        print("2. Gabung String")
        print("3. Operasi Delete")
        print("4. Operasi Substring")
        print("5. Operasi Insert")
        print("6. Lihat String yang Tersedia")
        print("7. Keluar")

        choice = int(input("Pilih fungsi yang ingin Anda gunakan (1/2/3/4/5/6) : "))
        print("========================")
        
        # Operasi Len
        if choice == 1:
            for i, string in enumerate(strings):
                print(f"Panjang dari String-{i+1} :", hitung_panjang(string))
        
        # Operasi Concat
        elif choice == 2:
            jumlah_spasi = int(input("Masukkan jumlah spasi yang diinginkan : "))
            hasil_concat = gabung_string(strings, jumlah_spasi)
            strings.append(hasil_concat)
            print(f"Hasil Penggabungan String : {hasil_concat}")
        
        
        # Opearsi Delete
        elif choice == 3:
            start = int(input("Masukkan indeks awal untuk operasi delete : "))
            end = int(input("Masukkan banyaknya karakter yang ingin didelete : "))
            print("========================")
            hasil_delete = operasi_delete(strings, start, end)
            strings.append(hasil_delete)
            print(f"Hasil operasi Delete : {hasil_delete}")
                    
        # Operasi Substring
        elif choice == 4:
            start = int(input("Masukkan indeks awal untuk operasi Substring : "))
            end = int(input("Masukkan banyaknya karakter yang ingin diambil : "))
            print("========================")
            hasil_substr = operasi_substr(strings, start, end)
            strings.append(hasil_substr)
            print(f"Hasil operasi Substring : {hasil_substr}")
            
        # Opearsi Insert
        elif choice == 5:
            posisi_insert = int(input("Masukkan posisi untuk penyisipan: "))
            print("========================")
            hasil_insert = operasi_insert(strings, posisi_insert)
            strings.append(hasil_insert)
            print(f"Hasil operasi Insert : {hasil_insert}")
        
        # Memperlihatkan banyaknya string yang tersedia        
        elif choice == 6:
            hasil_string = banyak_string(strings)
            
        # Keluar Kalkulator
        elif choice == 7:
            print("Thanks for using this calculator !")
            break
        
        else:
            print("Pilihan fungsi tidak valid.")

        print("========================")
        continue_program = input("Apakah Anda ingin melanjutkan program? (y/n): ")
        if continue_program.lower() != 'y':
            break